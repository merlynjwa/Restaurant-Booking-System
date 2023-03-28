from django.db import models
from django.core import validators

# Create your models here.


class Customer(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    table_number = models.IntegerField(
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(10)],
        unique_for_date='date_and_time'
        )

    def __str__(self):
        return '%s - Table no. %s' % (self.date_and_time, self.table_number)
