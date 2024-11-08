from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, UserUpdateForm, PostForm, CommentForm  # Ensure this is a registration form
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.db.models import Q

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

def home_view(request):
    return render(request, 'blog/home.html')

def posts_view(request):
    return render(request, 'blog/posts.html')

# View to list all blog posts
class PostListView(ListView):
    model = Post  # Specify the model to be used
    template_name = 'blog/post_list.html'  # Template to render the list
    context_object_name = 'posts'  # Name for the list in the template
    ordering = ['-published_date']  # Order posts by newest first

# View to display a single blog post in detail
class PostDetailView(DetailView):
    model = Post  # Specify the model to be used
    template_name = 'blog/post_detail.html'  # Template to render the detail view

# View to create a new blog post, requires the user to be logged in
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Specify the model to be used
    form_class = PostForm  # Use a custom form for the Post model
    template_name = 'blog/post_form.html'  # Template for the form

    # Automatically set the author of the post to the current logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        tags = form.cleaned_data.get('tags')
        return super().form_valid(form)

# View to update an existing blog post, requires the user to be logged in and the author of the post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Specify the model to be used
    form_class = PostForm  # Use a custom form for the Post model
    template_name = 'blog/post_form.html'  # Template for the form

    # Automatically set the author of the post to the current logged-in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        tags = form.cleaned_data.get('tags')
        return super().form_valid(form)

    # Check if the current user is the author of the post before allowing updates
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# View to delete an existing blog post, requires the user to be logged in and the author of the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Specify the model to be used
    template_name = 'blog/post_confirm_delete.html'  # Template to confirm deletion
    success_url = reverse_lazy('post-list')  # Redirect to post list after successful deletion

    # Check if the current user is the author of the post before allowing deletion
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()  

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()    

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})             

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        return Post.objects.filter(tags__slug=tag_slug)