from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
]
