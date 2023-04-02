from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s (%s)' % (self.email, self.username)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    table_number = models.IntegerField(
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(10)],
        unique_for_date='date_and_time'
        )

    def __str__(self):
        return '%s - Table no. %s - %s' % (self.date_and_time,
                                           self.table_number,
                                           self.customer)
