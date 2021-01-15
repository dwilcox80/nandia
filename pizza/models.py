from django.db import models


class CrustType(models.Model):
    crust_type = models.CharField(max_length=50)

    def __str__(self):
        return self.crust_type

class PizzaSize(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class SauceType(models.Model):
    sauce_type = models.CharField(max_length=15)

    def __str__(self):
        return self.sauce_type

class SauceAmount(models.Model):
    sauce_amount = models.CharField(max_length=15)

    def __str__(self):
        return self.sauce_amount

class Topping(models.Model):
    topping = models.CharField(max_length=50, default='Cheese')

    def __str__(self):
        return self.topping

class Pizza(models.Model):
    crust_selection = models.ForeignKey(CrustType, on_delete=models.CASCADE)
    sauce_amount = models.ForeignKey(SauceAmount, on_delete=models.CASCADE)
    sauce_type = models.ForeignKey(SauceType, on_delete=models.CASCADE)
    size_selection = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
    topping_selection = models.ManyToManyField(Topping)
