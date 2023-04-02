from django.test import TestCase
from .forms import OrderForm

# Create your tests here.


class TestOrderForm(TestCase):

    def test_table_number_is_required(self):
        form = OrderForm({'table_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('table_number', form.errors.keys())
        self.assertEqual(form.errors['table_number'][0],
                         'This field is required.')
