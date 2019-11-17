from django.db import models

# Create your models here.
class Food(models.Model):
    product_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=500, default="")
    food_amount = models.FloatField(default=0.0)
    date = models.DateField()


    def __str__(self):
        return self.food_name
