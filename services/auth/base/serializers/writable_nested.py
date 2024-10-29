import inflect
from base.utils.model_meta import get_field_info, get_unique_fields
from django.db import transaction
from django.db.models.fields.related_descriptors import (
    ManyToManyDescriptor,
    ForwardManyToOneDescriptor,
    ReverseManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ReverseOneToOneDescriptor
)
from rest_framework import serializers

p = inflect.engine()

related_descriptors = [
    ManyToManyDescriptor,
    ForwardManyToOneDescriptor,
    ReverseManyToOneDescriptor,
    ForwardOneToOneDescriptor,
    ReverseOneToOneDescriptor
]


class WritableNestedSerializer(serializers.ModelSerializer):
    @transaction.atomic
    def create(self, validated_data):
        return self.deep_create(self, validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        return self.deep_update(self, instance, validated_data)

    def deep_create(self, serializer, validated_data):
        data = validated_data.copy()
        relationships_data = {}
        ModelClass = serializer.Meta.model
        try:
            nested_create_fields = (
                serializer.Meta.nested_create_fields
                if serializer.Meta is not None and serializer.Meta.nested_create_fields is not None
                else list()
            )
        except:
            nested_create_fields = list()
        info = get_field_info(ModelClass)
        forward_relations = info.forward_relations
        forward_relation_keys = forward_relations.keys()
        reverse_relations = info.reverse_relations
        reverse_relation_keys = reverse_relations.keys()

        # Filter relationship data
        for key, value in data.items():
            if key in forward_relation_keys:
                relation = forward_relations[key]
                if not relation.to_many:
                    # Create forward related object
                    related_serializer = serializer._declared_fields.get(key)
                    if related_serializer is not None:
                        RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                        if RelatedModelClass is not None and isinstance(value, dict):
                            if key in nested_create_fields:
                                related_object = self.deep_create(
                                    related_serializer, value)
                                validated_data.update({key: related_object})
                            else:
                                del validated_data[key]
                else:
                    relationships_data[key] = validated_data.get(key)
                    del validated_data[key]
            elif key in reverse_relation_keys:
                relationships_data[key] = validated_data.get(key)
                del validated_data[key]

        # Create object
        instance, created = ModelClass.objects.update_or_create(
            **validated_data)
        if (len(relationships_data.keys()) == 0):
            return instance

        # Create reverse objects
        for key, value in relationships_data.items():
            if key in reverse_relations:
                relation = reverse_relations[key]
                if not relation.to_many:
                    related_serializer = serializer._declared_fields.get(key)
                    if related_serializer is not None:
                        RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                        if RelatedModelClass is not None and isinstance(value, dict):
                            related_field = relation.field_name
                            value.update({related_field: instance})
                            self.deep_create(related_serializer, value)
                else:
                    # Create reverse objects if it does not exist
                    related_objects = []
                    related_serializer = serializer._declared_fields.get(
                        key).child
                    RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                    if RelatedModelClass is not None:
                        for item in value:
                            if isinstance(item, dict):
                                if key in nested_create_fields:
                                    new_item = self.deep_create(
                                        related_serializer, item)
                                    related_objects.append(new_item)
                            else:
                                related_objects.append(item)
                        field = getattr(instance, key)
                        field.set(related_objects)
            else:
                # Foward many to many relationship
                relation = forward_relations[key]
                related_objects = []
                related_serializer = serializer._declared_fields.get(key).child
                RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                if RelatedModelClass is not None:
                    for item in value:
                        if isinstance(item, dict):
                            if key in nested_create_fields:
                                new_item = self.deep_create(
                                    related_serializer, item)
                                related_objects.append(new_item)
                        else:
                            related_objects.append(item)
                field = getattr(instance, key)
                field.set(related_objects)
        if (serializer == self):
            instance.refresh_from_db()
        return instance

    def deep_update(self, serializer, instance, validated_data):
        data = validated_data.copy()
        relationships_data = {}
        info = get_field_info(instance)
        forward_relations = info.forward_relations
        forward_relation_keys = forward_relations.keys()
        reverse_relations = info.reverse_relations
        reverse_relation_keys = reverse_relations.keys()
        try:
            nested_update_fields = (
                serializer.Meta.nested_update_fields
                if serializer.Meta is not None and serializer.Meta.nested_update_fields is not None
                else list()
            )
        except:
            nested_update_fields = list()

        # Filter relationship data
        for key, value in data.items():
            if key in forward_relation_keys:
                relation = forward_relations[key]
                if not relation.to_many:
                    # Create forward related object
                    related_serializer = serializer._declared_fields.get(key)
                    if related_serializer is not None:
                        RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                        if RelatedModelClass is not None and isinstance(value, dict):
                            if key in nested_update_fields:
                                if value.get('id', None) is None:
                                    related_object = self.deep_create(
                                        related_serializer, value)
                                    validated_data.update({key: related_object})
                                    setattr(instance, key, related_object)
                                else:
                                    related_id = value.get('id')
                                    del value['id']
                                    related_object = RelatedModelClass.objects.get(
                                        pk=related_id)
                                    new_item = self.deep_update(
                                        related_serializer, related_object, value)
                                    validated_data.update({key: new_item})
                                    setattr(instance, key, new_item)
                            else:
                                del validated_data[key]
                        else:
                            setattr(instance, key, value)
                else:
                    relationships_data[key] = validated_data.get(key)
                    del validated_data[key]
            elif key in reverse_relation_keys:
                relationships_data[key] = validated_data.get(key)
                del validated_data[key]
            else:
                setattr(instance, key, value)

        # Create object
        instance.save()
        if (len(relationships_data.keys()) == 0):
            return instance

        # Create reverse objects
        for key, value in relationships_data.items():
            if key in reverse_relations:
                relation = reverse_relations[key]
                if not relation.to_many:
                    related_serializer = serializer._declared_fields.get(key)
                    if related_serializer is not None:
                        RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                        if RelatedModelClass is not None and isinstance(value, dict):
                            related_field = relation.field_name
                            value.update({related_field: instance})
                            self.deep_create(related_serializer, value)
                else:
                    # Create reverse objects if it does not exist
                    related_objects = []
                    related_serializer = serializer._declared_fields.get(
                        key).child
                    RelatedModelClass = related_serializer.Meta.model if related_serializer.Meta else None
                    if RelatedModelClass is not None:
                        for item in value:
                            if isinstance(item, dict):
                                if item.get('id', None) is None:
                                    if key in nested_update_fields:
                                        related_field = relation.field_name
                                        new_item = self.deep_create(
                                            related_serializer, item)
                                        related_objects.append(new_item)
                                else:
                                    related_id = item.get('id')
                                    del item['id']
                                    related_object = RelatedModelClass.objects.get(
                                        pk=related_id)
                                    new_item = self.deep_update(
                                        related_serializer, related_object, item)
                                    related_objects.append(new_item)
                            else:
                                related_objects.append(item)
                        field = getattr(instance, key)
                        field.set(related_objects)
            else:
                # Foward many to many relationship
                field = getattr(instance, key)
                field.set(value)

        if (serializer == self):
            instance.refresh_from_db()
        return instance

    def to_internal_value(self, data):
        # Replace forward nested data by it instance if the related instance already exist.
        ModelClass = self.Meta.model
        try:
            nested_create_fields = (
                self.Meta.nested_create_fields
                if self.Meta is not None and self.Meta.nested_create_fields is not None
                else list()
            )
        except:
            nested_create_fields = list()
        try:
            nested_update_fields = (
                self.Meta.nested_update_fields
                if self.Meta is not None and self.Meta.nested_update_fields is not None
                else list()
            )
        except:
            nested_update_fields = list()

        info = get_field_info(ModelClass)
        forward_relations = info.forward_relations
        forward_relation_keys = forward_relations.keys()
        reverse_relations = info.reverse_relations
        reverse_relation_keys = reverse_relations.keys()
        items = data.copy().items()
        relationships_data = {}
        for key, value in items:
            if key in forward_relation_keys:
                RelatedModel = forward_relations[key].related_model
                unique_fields = get_unique_fields(RelatedModel)
                unique_keys = unique_fields.keys()
                if self.instance is None and key in nested_create_fields and isinstance(value, dict):
                    if len(unique_keys) > 0:
                        for k, v in value.items():
                            if k in unique_keys:
                                try:
                                    related_object = RelatedModel.objects.get(
                                        **{k: v})
                                except RelatedModel.DoesNotExist:
                                    related_object = None
                                if related_object is not None:
                                    data.update(
                                        {f'{key}_id': related_object.id.urn[9:]})
                                    del data[key]
                elif isinstance(value, list):
                    related_ids = []
                    for item in value:
                        if isinstance(item, dict) and item.get("id", None) is not None:
                            related_ids.append(item.get("id"))
                    data.update({f'{p.singular_noun(key)}_ids': related_ids})
                    del data[key]
            elif key in nested_update_fields and key in reverse_relation_keys:
                # Todo: validate related data
                if isinstance(value, dict):
                    relationships_data[key] = data.get(key)
                    del data[key]
                elif isinstance(value, list):
                    relationships_data[key] = data.get(key)
                    del data[key]

        valid_data = super().to_internal_value(data)
        for key, value in relationships_data.items():
            if isinstance(value, list) or isinstance(value, dict):
                valid_data[key] = relationships_data.get(key)

        return valid_data
