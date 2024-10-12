from rest_framework import status, viewsets
from rest_framework.response import Response
from django.db import transaction
from django.db.models import Q


class BaseViewSet(viewsets.ModelViewSet):
    queryset_map = {}
    search_map = {}
    serializer_class = None
    required_alternate_scopes = {}
    serializer_map = {}

    def get_queryset(self):
        """
        Get action's queryset base on `queryset_map`
        :return: QuerySet
        """
        return self.queryset_map.get(self.action, self.queryset)

    def clear_querysets_cache(self):
        """
        Cleand the cache
        Use this in cacses you have update the data somewhere
        """
        if self.queryset is not None:
            self.queryset._result_cache = None

        for action, queryset in self.queryset_map.items():
            queryset._result_cache = None

    def get_serializer_class(self):
        """
        Get action's serializer base on `serializer_map`
        :return: Serializer
        """
        return self.serializer_map.get(self.action, self.serializer_class)

    def limitBusiness(self, data, **kwargs):
        data = data.copy()
        businesses_pk = kwargs.get('businesses_pk')
        if businesses_pk:
            serializer_class = self.get_serializer_class()
            fields = (
                serializer_class.Meta.fields
                if serializer_class.Meta and serializer_class.Meta.fields
                else []
            )
            if 'business_id' in fields:
                if isinstance(data, list):
                    for item in data:
                        item.update({"business_id": businesses_pk})
                else:
                    data.update({"business_id": businesses_pk})
        return data

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data = self.limitBusiness(data, **kwargs)
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            self.clear_querysets_cache()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(self.get_object(), data=data)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            self.clear_querysets_cache()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        params = request.query_params

        keyword = params.get("keyword")
        if keyword and len(self.search_map) > 0:
            query = Q()
            for field, op in self.search_map.items():
                kwargs = {'{0}__{1}'.format(field, op): keyword}
                query |= Q(**kwargs)
            queryset = queryset.filter(query)

        if params.get('page_size') is not None:
            page = self.paginate_queryset(queryset)
            data = self.get_serializer(page, many=True).data
            return self.get_paginated_response(data)
        else:
            data = self.get_serializer(queryset, many=True).data
            return Response(data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        self.clear_querysets_cache()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def multiple_delele(self, request, *args, **kwargs):
        """
        Delete multiple items.
        :return: Response
        """
        ids = request.data.get("ids")
        ModelClass = self.get_serializer_class().Meta.model
        manager = ModelClass._default_manager
        with transaction.atomic():
            instances = manager.filter(id__in=ids)
            if instances:
                instances.delete()
        self.clear_querysets_cache()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  Just use this viewset


class MultipleUpdateViewSet(BaseViewSet):
    def create(self, request, *args, **kwargs):
        """
        Create mutile items at once.
        :return: Response
        """
        data = self.limitBusiness(request.data, **kwargs)
        try:
            serializer = self.get_serializer(
                data=data, many=isinstance(data, list))
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                self.clear_querysets_cache()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def sync(self, request, *args, **kwargs):
        """
        Sync data from client to server. The item without id will be created.
        The item does not exist in client request will be removed.
        The others items will be updated.
        Only use this method for the small table where all data can be fit on one page.
        :return: Response
        """
        data = self.limitBusiness(request.data, **kwargs)
        try:
            queryset = self.get_queryset()
            if queryset:
                serializer = self.get_serializer(
                    queryset, data=data, many=isinstance(data, list), allow_null=True)
            else:
                serializer = self.get_serializer(
                    data=data, many=isinstance(data, list))
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                self.clear_querysets_cache()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            raise e
