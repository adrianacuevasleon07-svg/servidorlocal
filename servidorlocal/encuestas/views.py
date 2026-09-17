from django.shortcuts import HttpResponse



def index(request):
    return HttpResponse('<h1>hola! esta es la pagina principal de Encuestas.</h1>')

# Create your views here.
