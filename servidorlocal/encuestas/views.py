from django.shortcuts import HttpResponse
from utils import limpiar_texto
from django.shortcuts import render
from .models import Musician
from django.views.decorators.csrf import csrf_exempt



def index(request):
    hola = "m a l o"
    texto = hola + "::"+ limpiar_texto(hola)
    
    return render(request, "code.html", {"text": limpiar_texto(hola)} )
    
@csrf_exempt
def musico(request):
    if request.method == "POST":
        nombre = request.POST.get("first_name")
        especialidad = request.POST.get("last_name")
    
        instrumento = request.POST.get("instrument")
        musico=Musician(first_name=nombre, last_name=especialidad, instrument=instrumento)
        musico.save()
    
            
            
            
    



    
# Create your views here.
