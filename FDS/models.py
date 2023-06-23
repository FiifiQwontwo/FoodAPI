from django.db import models
from accounts.models import Account


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=120, blank=True, null=True)
    address = models.CharField(blank=True, max_length=120)

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return f'pictures/{instance.name_of_meal}/{filename}'


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name_of_meal = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=upload_to, blank=True, null=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name_of_meal

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
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='Food_Orders')
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.customer.phone)

    def sub_total(self):
        return self.food.price * self.quantity


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="customer_orders")
    status = models.CharField(max_length=25, choices=FOOD_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
