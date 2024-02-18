from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import UpdateView
from app.models import Participacao
from django.urls import reverse_lazy


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(
                username=new_user.username,
                password=request.POST['password1']
                )
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'pages/register.html', context)

    
class MinistroUpdateView(UpdateView):
    # Edita o form
    model = Participacao
    fields = ["ministro", "missa"]
    success_url = reverse_lazy("home")