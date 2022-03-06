from django.db import models

# Create your models here.


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    travelPoints = models.IntegerField()

    def __str__(self):
        return "Passenger "+self.firstName+" "+self.lastName+" with points "+self.travelPoints+". "
