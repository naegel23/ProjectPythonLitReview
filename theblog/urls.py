from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCommentView,\
    AddCritiqueView, UpdateCritiqueView, DeleteCritiqueView, CritiqueDetailView, show_profile, FollowersListView,\
    welcome, PostsView


urlpatterns = [
    path('', welcome, name="welcome"),
    path('home/', HomeView.as_view(), name="home"),
    path('posts/', PostsView.as_view(), name="posts"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
    path('search_user', views.search_user, name='search-user'),
    path('critique/<int:pk>', CritiqueDetailView.as_view(), name="critique-detail"),
    path('add_critique/', AddCritiqueView.as_view(), name='add-critique'),
    path('article/edit_critique/<int:pk>', UpdateCritiqueView.as_view(), name='update-critique'),
    path('article/<int:pk>/delete_critique', DeleteCritiqueView.as_view(), name='delete-critique'),
    path('profile/<profile_id>', show_profile, name='show-profile-page'),
    path('following_list/', FollowersListView.as_view(), name="following-list"),

]
