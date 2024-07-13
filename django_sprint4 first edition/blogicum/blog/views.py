from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.urls import reverse
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from blog.forms import PostForm

User = get_user_model()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'blog/create.html' 

    def get_success_url(self):
        return reverse(
            'blog:post_detail', 
            kwargs={'username': self.object.author.username, 'id': self.object.id} 
        )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'username': self.request.user.author, 'id': self.object.id} 
        )


def post_select_related():
    return Post.objects.select_related(
        'author', 'location', 'category'
    ).filter(
        pub_date__lte=now(),
        is_published=True,
        category__is_published=True)


def index(request):
    template = 'blog/index.html'
    posts = post_select_related().order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    posts = post_select_related().filter(
        category=category,
    ).order_by('-pub_date')
    context = {'post_list': posts, 'category': category}
    return render(request, template, context)


def post_detail(request, id):
    post = get_object_or_404(
        post_select_related(), id=id)
    context = {'post': post}
    template = 'blog/detail.html'
    return render(request, template, context)


def profile_view(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(author=user)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'profile.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author__id=self.kwargs['author_id'])


class ProfileDetailView(DetailView):
    model = User
    template_name = 'blog/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object)
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'blog/profile.html'
    fields = ['first_name', 'last_name', 'email']
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.object.username})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            return redirect('profile', username=obj.username)
        return super().dispatch(request, *args, **kwargs)
