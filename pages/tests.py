from django.test import TestCase
from .models import Page
from django.urls import reverse

class PageModelTest(TestCase):
    def setUp(self) -> None:
        Page.objects.create(text='just a test')

    def test_text_content(self):
        page = Page.objects.get(id=1)
        expected_object_name = f'{page.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Page.objects.create(text='this is another test')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


