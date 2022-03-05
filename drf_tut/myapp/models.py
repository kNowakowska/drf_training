from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.id+" "+self.name+" "+self.salary


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    score = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.id+" "+self.name+" "+self.score