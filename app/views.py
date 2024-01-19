from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Participacao
from .filters import OrderFilter


def index(request):
    usuarios = User.objects.all()

    myFilter = OrderFilter(
        request.GET, 
        queryset=Participacao.objects.select_related('ministro', 'missa'))

    context = {"usuarios": usuarios, "myFilter": myFilter}
    return render(request, "pages/home.html", context)

    # todas_escalas = Escala.objects.all()
    # return HttpResponse(todas_escalas[1].id)

# Create your views here.


def teste(request):
    return render(request, 'pages/teste.html')