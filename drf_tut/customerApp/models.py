from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    phone = models.CharField(max_length=9)


class Order(models.Model):
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
