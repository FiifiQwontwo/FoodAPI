from django.db import models
from accounts.models import Account


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=120, blank=True, null=True)
    address = models.CharField(blank=True, max_length=120)


def upload_to(instance, filename):
    return f'pictures/{instance.name_of_meal}/{filename}'


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name_of_meal = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=upload_to)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        self.picture.name = upload_to(self, self.picture.name)
        super().save(*args, **kwargs)


FOOD_STATUS = (
    ('Pending', 'Pending'),
    ('Progress', 'Progress'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)


class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    status = models.CharField(max_length=20, choices=FOOD_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
