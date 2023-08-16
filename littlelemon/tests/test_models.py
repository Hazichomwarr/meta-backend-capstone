from django.test import TestCase
from restaurant.models import Menu, Booking


# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="icecream", price="80", inventory=6)

        self.assertEqual(item, "icecream : 80")
