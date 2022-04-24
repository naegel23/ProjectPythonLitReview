from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm, CommentForm, CritiqueForm, EditCritiqueForm
from .models import Post, Comment, Critique, Profile


# Create your views here.


# def post_of_following_profiles(request):
#     # get logged in user profile
#     profile = Profile.objects.get(user=request.user)
#     # check who we are following
#     users = [user for user in profile.following.all()]
#     # initial values for variables
#     posts = []
#     qs = None
#     # get the posts of people who we are following
#     for u in users:
#         p = Profile.objects.get(user=u)
#         p_posts = p.post_set.all()
#         posts.append(p_posts)
#     # our posts
#     my_posts = profile.profiles_posts()
#     posts.append(my_posts)
#     # sort and chain queryset and unpack the posts lists
#     if len(posts)>0:
#         qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
#     return render(request, 'home.html', {'profile': profile, 'posts': qs})


class HomeView(ListView):
    template_name = 'home.html'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['my_posts'] = Post.objects.filter(author=profile)
        context['my_critiques'] = Critique.objects.filter(author=profile)
        # context['posts'] = Post.objects.all()
        context['critiques'] = []
        context['posts'] = []
        for follower in profile.following.all():
            # context['posts'].append(Post.objects.filter(author=follower.id).all())
            tmp = Post.objects.filter(author=follower.id).all()
            tmc = Critique.objects.filter(author=follower.id).all()
            for t in tmp:
                context['posts'].append(t)
            for c in tmc:
                context['critiques'].append(c)

        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'


class FollowersListView(ListView):
    model = Profile
    template_name = 'followers_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        context['profile'] = profile
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(FollowersListView, self).get_context_data(**kwargs)
    #     view_profile = Profile.objects.filter(user=self.request.user.id)
    #     my_profile = Profile.objects.get(user=self.request.user)
    #     following_list = []
    #     for follower in view_profile:
    #         print(follower)
    #     if view_profile in my_profile.following.all():
    #         follow = True
    #     else:
    #         follow = False
    #     # context['followers'] = Profile.objects.filter(following=self.request.user.id)
    #     context["follow"] = follow
    #     context["view_profile"] = view_profile
    #
    #     return context


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


# def follow_unfollow_profile(request):
#     if request.method == "POST":
#         my_profile = Profile.objects.get(user=request.user)
#         pk = request.POST.get('pk')
#         obj = Profile.objects.get(pk=pk)
#
#         if obj.user in my_profile.following.all():
#             my_profile.following.remove(obj.user)
#         else:
#             my_profile.following.add(obj.user)
#         return redirect(request.META.get('HTTP_REFERER'))
#     return redirect('user_profile.html')


# class ShowProfilePageView(DetailView):
#     template_name = 'user_profile.html'
#     queryset = User.objects.all()
#
#     def get_object(self, **kwargs):
#         pk = self.kwargs.get('pk')
#         view_profile = Profile.objects.get(pk=pk)
#         return view_profile
#
#     def get_context_data(self, profile_id, *args, **kwargs):
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         view_profile = self.get_object()
#         my_profile = Profile.objects.get(user=self.request.user)
#         if view_profile.user in my_profile.following.all():
#             follow = True
#         else:
#             follow = False
#         profile = User.objects.get(pk=profile_id)
#         context["follow"] = follow
#         context["profile"] = profile
#
#         return context
