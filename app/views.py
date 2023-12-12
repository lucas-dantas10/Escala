from django.shortcuts import render
from django.http import HttpResponse
from app.models import Escala

def index(request):
    return render(request, "pages/home.html")

    # todas_escalas = Escala.objects.all()
    # return HttpResponse(todas_escalas[1].id)

# Create your views here.
