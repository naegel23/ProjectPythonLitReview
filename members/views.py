from django.views import generic
# from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
# from django.views.generic import DetailView
from .forms import SignupForm


# Create your views here.


# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'registration/user_profile.html'
#
#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#
#         context["page_user"] = page_user
#         return context


class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


