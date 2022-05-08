from django.views import generic
from django.urls import reverse_lazy
from .forms import SignupForm
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
