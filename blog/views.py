from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from .models import Blog,Comment,Author

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


from .forms import CommentCreateForm, CommentUpdateForm

from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'blog/index.html'

class ProblemView(TemplateView):
    template_name = 'blog/problems.html'

class AllBlogsView(ListView):
    model = Blog
    template_name = 'blog/all_blogs.html'

    def get_queryset(self):
        return Blog.objects.all().order_by('-pub_date')


class BlogDetailView(DetailView):
    model = Blog

class AllBloggersView(ListView):
    """
    Accessed by everyone.
    """

    model = Author
    template_name = 'blog/all_bloggers.html'


class BloggerDetailView(DetailView):
    """
    Accessed by everyone.
    """

    model = Author
    template_name = 'blog/author_profile.html'

@login_required
def CommentCreateView(request, pk):
    """
    Comments can only be created by logged-in users.
    """

    blog = get_object_or_404(Blog, pk=pk)
    user = User.objects.get(username=request.user.username)

    if request.method=="POST":
        form = CommentUpdateForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data['text']
            comment = Comment.objects.create(text=text, blog=blog, commenter=user)
            comment.save()
            return redirect('blog_detail', pk)

    else:
        form = CommentUpdateForm()

    return render(request, 'blog/comment_form.html', {'form':form, 'blog':blog})

@login_required
def CommentUpdateView(request,blogid,commentid):

    """Comments can only be updated by own commenter."""

    blog = get_object_or_404(Blog, pk=blogid)
    user = User.objects.get(username=request.user.username)

    comment = get_object_or_404(Comment, pk=commentid)
    commenter = comment.commenter

    if not user==commenter:
        return redirect('problem')

    else:

        if request.method == "POST":
            form = CommentCreateForm(request.POST)
            if form.is_valid():

                text = form.cleaned_data['text']
                comment.text = text
                comment.save()
                return redirect('blog_detail', blogid)
        else:
            form = CommentCreateForm()

        return render(request, 'blog/comment_update_form.html', {'form':form, 'blog':blog, 'comment':comment})


@login_required
def CommentDeleteView(request,blogid,commentid):

    """Comments can only be deleted by own commenter or blog author"""

    blog = get_object_or_404(Blog, pk=blogid)
    author = blog.blogger

    user = User.objects.get(username=request.user.username)

    comment = get_object_or_404(Comment, pk=commentid)
    commenter = comment.commenter

    if user==commenter or user==author:
        comment.delete()
        return redirect('blog_detail', blog.pk)

    else:
        return render(request, 'blog/problems.html')
