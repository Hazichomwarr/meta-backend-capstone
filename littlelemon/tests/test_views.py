from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        item1 = Menu.objects.create(title="icecream", price="80", inventory=6)
        item2 = Menu.objects.create(title="chicken", price="50", inventory=3)

    def test_getall(self):
        items = Menu.objects.all()
        self.assertContains(items)
