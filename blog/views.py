from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.urls import reverse_lazy
from blog.forms import PostForm, CommentForm, UserCreateForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView, FormView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
User = get_user_model()

#todo- automatic login after signup
class Signup(FormView):
    form_class = UserCreateForm
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('post_list')


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # this method defines how to grab the objects of the class
        return Post.objects.filter(published_date__lte=timezone.localtime()).order_by('-published_date')
        # search field lookup in django documentation for more info


class PostDetailView(DetailView):
    model = Post

# by admin only
class CreatePostView(AdminStaffRequiredMixin,CreateView):
    login_url = '/login/'
# login_url is URL that users who don’t pass the test/authentication will be redirected to.
# redirect_field_name attribute should be set to URL the user should be redirected to after a successful login.
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# admin
class PostUpdateView(AdminStaffRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

    

# admin
class DraftListView(AdminStaffRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# admin
class PostDeleteView(AdminStaffRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Post
    success_url = reverse_lazy('post_list')

#######################################
## Functions that require a pk match ##
#######################################

# admin
@user_passes_test(lambda u: u.is_superuser)
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

# users
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    # because we are deleting the comment
    comment.delete()
    return redirect('post_detail', pk=post_pk)

