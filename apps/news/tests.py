from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from django.test import TestCase,SimpleTestCase,Client
from apps.news.views import ListNewsAPIView,news_categories
class TestNewsUrl(SimpleTestCase):
    def test_news_url(self):

        url = reverse("news_list")
        self.assertEquals(resolve(url).func.view_class, ListNewsAPIView)


    def test_news_category_url(self):
        url = reverse("news_category")
        self.assertEquals(resolve(url).func,news_categories)


class TestView(TestCase):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.client=Client()


    def test_list_news_view(self):
        url = reverse("news_list")
        responce=self.client.get(url)
        print(responce)
        assert responce.status_code ==200
        assert responce.json()==[]


    def test_single_news_view(self):
        
        url = reverse("detail_news", kwargs={'pk':1})
        responce=self.client.get(url)
        assert responce.status_code ==404





