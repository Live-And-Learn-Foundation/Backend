from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(content="The course service is up and healthy.")
