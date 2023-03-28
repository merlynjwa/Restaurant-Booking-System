from django.db import models
from django.core import validators

# Create your models here.


class Customer(models.Model):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return '%s (%s %s)' % (self.email,
                               self.first_name,
                               self.last_name)


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
