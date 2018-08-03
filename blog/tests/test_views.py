from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from blog.models import Blog,Comment,Author

class HomeViewTest(TestCase):

    def test_blogpage_is_ok_and_uses_correct_template(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'blog/index.html')

    #test redirection of main page
    def test_index_page_is_redirected(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code,302)

    def test_index_page_has_link_to_blog_page(self):
        resp = self.client.get('/blog/')
        url = reverse('all_blogs')
        self.assertContains(resp,url)


class BlogListViewTest(TestCase):


    def setUp(self):
        #create user
        testuser = User.objects.create_user(username='testuser', password='12345')
        testuser.save()

        testauthor = Author.objects.create(user=testuser, bio="bioooooo")

        #create blog
        testblog = Blog.objects.create(title='testblog1',text="blabla",blogger=testuser)
        testblog.save()

    def test_detail_link_is_on_list_page(self):
        resp = self.client.get('/blog/blogs/')
        url = reverse('blog_detail', kwargs={'pk':1})
        self.assertContains(resp,url)

    # def test_author_link_is_on_list_page(self):
    #     resp = self.client.get('/blog/blogs/')
    #     url = reverse('author_detail', kwargs={'pk':1})
    #     self.assertContains(resp,url)
    #
