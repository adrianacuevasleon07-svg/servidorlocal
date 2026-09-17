from django.shortcuts import HttpResponse
from utils import limpiar_texto
from django.shortcuts import render



def index(request):
    hola = "m a l o"
    texto = hola + "::"+ limpiar_texto(hola)
    
    return render(request, "code.html", {"text": limpiar_texto(hola)} )

    
# Create your views here.
