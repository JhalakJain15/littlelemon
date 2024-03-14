from django.test import TestCase
from .models import MenuItem  # Assuming your models file is named models.py

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        expected_string = "IceCream : 80"  # Assuming this is the format you want to compare with
        self.assertEqual(str(item), expected_string)
