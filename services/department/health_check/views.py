from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(content="The department service is up and healthy.")
