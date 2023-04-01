from django import forms
from .models import Order
from django.contrib.admin import widgets


class OrderForm(forms.ModelForm):
    date_and_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)

    class Meta:
        model = Order
        fields = ['table_number',
                  'date_and_time']
