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

    def test_date_and_time_is_required(self):
        form = OrderForm({'date_and_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('date_and_time', form.errors.keys())
        self.assertEqual(form.errors['date_and_time'][0],
                         'This field is required.')

    def test_explicit_fields_in_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ['table_number', 'date_and_time'])


class TestViews(TestCase):

