from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields=('text',)

class CommentUpdateForm(forms.ModelForm):
        class Meta():
            model = Comment
            fields=('text',)
