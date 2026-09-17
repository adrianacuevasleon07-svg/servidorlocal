from django.shortcuts import HttpResponse



def gato(request):
    return HttpResponse('<h1>hola! esta es la pagina principal de Encuestas.</h1>')