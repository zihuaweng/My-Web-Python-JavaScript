from django.test import TestCase, Client
from .models import Page
from django.urls import reverse
from django.contrib.auth import get_user_model


class PageModelTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.page = Page.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        page = Page(title='A sample title')
        self.assertEqual(str(page), page.title)

    def test_page_content(self):
        self.assertEqual(f'{self.page.title}', 'A good title')
        self.assertEqual(f'{self.page.author}', 'testuser')
        self.assertEqual(f'{self.page.body}', 'Nice body content')

    def test_page_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_page_detail_view(self):
        response = self.client.get('/page/1/')
        no_response = self.client.get('/page/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'page_detail.html')


class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Page.objects.create(title='this is another test')

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
