from django.urls import path
from .views import UserRegisterView, UserEditView



urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    # path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
]
