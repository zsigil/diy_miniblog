from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    last_edit = models.DateField(auto_now=True)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta():
        permissions = (
            ('can_write_blog', 'Blog author'),
        )

class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:40]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text='To become an author, we need your bio.')

    def __str__(self):
        return '{} - blog author'.format(self.user.username)
