from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu


class MenuViewTest(TestCase):

    def setUp(self):
        super().setUp()
        self.item_salad = Menu.objects.create(title="Salad", price=5.20, inventory=40)
        self.item_beef_pasta = Menu.objects.create(title="Beef Pasta", price=6, inventory=5)
        self.item_grilled_fish = Menu.objects.create(title="Grilled Fish", price=7.50, inventory=21)

    def test_get_all(self):
        response = self.client.get(
            path=reverse('menu_item_list'),
            content_type='application/json')
        json_data = response.json()

        items_str = '\n'.join([f"{item['title']} : {str(item['price'])}" for item in json_data])
        expected = "Salad : 5.20\n" \
                   "Beef Pasta : 6.00\n" \
                   "Grilled Fish : 7.50"

        self.assertEqual(response.status_code, 200)
        self.assertEqual(items_str, expected)
