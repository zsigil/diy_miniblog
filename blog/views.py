from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Blog,Comment,Author

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .forms import CommentCreateForm

from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    template_name = 'blog/index.html'

class AllBlogsView(ListView):
    model = Blog
    template_name = 'blog/all_blogs.html'

    def get_queryset(self):
        return Blog.objects.all().order_by('-pub_date')


class BlogDetailView(DetailView):
    model = Blog

class AllBloggersView(ListView):
    model = Author
    template_name = 'blog/all_bloggers.html'


class BloggerDetailView(DetailView):
    model = Author
    template_name = 'blog/author_profile.html'

@login_required
def CommentCreateView(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    user = User.objects.get(username=request.user.username)

    print(blog)
    if request.method=="POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            comment = Comment.objects.create(text=text, blog=blog, commenter=user)
            comment.save()
            return redirect('blog_detail', pk)

    else:
        form = CommentCreateForm()

    return render(request, 'blog/comment_form.html', {'form':form, 'blog':blog})
