from django.shortcuts import render
from django.views import View
from django.models import Persona

class ListarPersonas(View):
    template_name= "repasoej/lista_de_personas.html"    
    
    def get(self, request):
        personas = Persona.objects.all()
        return render(request, self.template_name)
# Create your views here.
