from django.test import TestCase

class HomeViewTest(TestCase):

    def test_blogpage_is_ok_and_uses_correct_template(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'blog/index.html')
