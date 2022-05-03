from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm, CritiqueForm, EditCritiqueForm
from .models import Post, Comment, Critique, Profile
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html', {})


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['my_posts'] = Post.objects.filter(author=profile).order_by('-post_date')
        context['my_critiques'] = Critique.objects.filter(author=profile)
        context['critiques'] = []
        context['posts'] = []
        for follower in profile.following.all():
            tmp = Post.objects.filter(author=follower.id).all().order_by('-post_date')
            tmc = Critique.objects.filter(author=follower.id).all()
            for t in tmp:
                context['posts'].append(t)
            for c in tmc:
                context['critiques'].append(c)

        return context


class PostsView(ListView):
    template_name = 'posts.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostsView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['my_posts'] = Post.objects.filter(author=profile)
        context['my_critiques'] = Critique.objects.filter(author=profile)

        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class FollowersListView(ListView):
    template_name = 'followers_list.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        my_profile = Profile.objects.get(user=self.request.user)
        all_profile = Profile.objects.all()
        profiles_list = list(all_profile)
        context['followings'] = []
        context['followers'] = []

        # Get followings
        for prof in profiles_list:
            if my_profile == prof:
                profiles_list.remove(my_profile)
        for profile in my_profile.following.all():
            context['followings'].append(profile)

        # Get followers
        for prof in profiles_list:
            if my_profile == prof:
                profiles_list.remove(my_profile)
        for prof in profiles_list:
            for p in prof.following.all():
                if my_profile.id == p.id:
                    context['followers'].append(prof)

        return context


class CritiqueDetailView(DetailView):
    model = Critique
    template_name = 'critique_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCritiqueView(CreateView):
    model = Critique
    form_class = CritiqueForm
    template_name = 'add_critique.html'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class UpdateCritiqueView(UpdateView):
    model = Critique
    form_class = EditCritiqueForm
    template_name = 'update_critique.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class DeleteCritiqueView(DeleteView):
    model = Critique
    template_name = 'delete_critique.html'
    success_url = reverse_lazy('home')


def search_user(request):
    if request.method == "POST":
        searched = request.POST['searched']
        users = User.objects.filter(username__contains=searched)
        return render(request, 'search_user.html', {'searched': searched, 'users': users})
    else:
        return render(request, 'search_user.html', {})


def show_profile(request, profile_id):
    profile = User.objects.get(pk=profile_id)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.following.add(profile)
        else:
            current_user_profile.following.remove(profile)
        current_user_profile.save()
    return render(request, 'user_profile.html', {'profile': profile})
