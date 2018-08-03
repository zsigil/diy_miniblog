from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from blog.models import Author

class SignUpForm(UserCreationForm):

    class Meta():
        model = User
        fields=('username', 'password1', 'password2')

        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-control'}),
        #     'password1': forms.PassWordInput(attrs={'class':'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        # }

class AuthorCreationForm(forms.ModelForm):

    class Meta():
        model = Author
        fields = ('bio',)

        widgets = {
            'bio': forms.Textarea(attrs={'cols':'80', 'rows':'10'}),
        }
