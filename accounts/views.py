from django.shortcuts import render,redirect
from .forms import SignUpForm, AuthorCreationForm
from django.contrib.auth.models import User
from blog.models import Author

from django.contrib.auth.models import Permission
permission = Permission.objects.get(name='Blog author')
# Create your views here.
def SignUpView(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form':form})


def AuthorCreateView(request):
    user = User.objects.get(username=request.user.username)
    if user.has_perm('can_write_blog'):
        return redirect('all_bloggers')


    if request.method == "POST":

        form = AuthorCreationForm(request.POST)

        if form.is_valid():
            bio = form.cleaned_data.get('bio')
            author = Author.objects.create(user=user, bio=bio)
            author.user.user_permissions.add(permission)
            author.save()
            return redirect('all_bloggers')

    else:
        form = AuthorCreationForm()


    return render(request, 'registration/authorcreate.html', {'form':form})
