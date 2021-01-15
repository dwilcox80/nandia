from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = [
            'crust_selection',
            'sauce_type',
            'sauce_amount',
            'size_selection',
            'topping_selection'
        ]
        labels = {
            'crust_selection':'Crust',
            'sauce_amount':'Sauce Amount',
            'sauce_type':'Sauce Type',
            'size_selection':'Size',
            'topping_selection':'Toppings'
        }
        widgets = {
            'topping_selection': forms.CheckboxSelectMultiple()
        }

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(
        min_value=2,
        max_value=10,
    )