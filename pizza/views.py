from django.shortcuts import render
from .forms import MultiplePizzaForm, PizzaForm
from django.forms import formset_factory
from .models import Pizza


# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()

    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        topping_note = ''
        if filled_form.is_valid():
            form = PizzaForm()  # reset the form
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            base_note = f'Thanks for ordering! Your {filled_form.cleaned_data["size_selection"]}' \
                        f' {filled_form.cleaned_data["crust_selection"]} pizza with'
            for topping in filled_form.cleaned_data['topping_selection']:
                topping_note += str(topping) + ', '
            note = f'{base_note} {topping_note[0:len(topping_note) - 2]}.'
        else:
            created_pizza_pk = None
            form = filled_form
            note = 'Your pizza order was not created. Please try again.'

        context = {
            'form': form,
            'multiple_form': multiple_form,
            'created_pizza_pk': created_pizza_pk,
            'note': note
        }
        return render(request, 'pizza/order.html', context=context)
    else:
        form = PizzaForm()
        context = {
            'form': form,
            'multiple_form': multiple_form
        }
    return render(request, 'pizza/order.html', context=context)


def multi_pizzas(request):
    number_of_pizzas = 2
    filled_multiple_form = MultiplePizzaForm(request.GET)
    if filled_multiple_form.is_valid():
        number_of_pizzas = filled_multiple_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            note = 'Your pizzas have been ordered!'
        else:
            note = 'Order was not created. Please try again'
        context = {
            'note': note,
            'formset': formset
        }
        return render(request, 'pizza/multi_pizzas.html', context=context)
    else:
        context = {
            'formset': formset
        }
        return render(request, 'pizza/multi_pizzas.html', context=context)


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
            return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza,
                                                             'note': note})
    return render(request, 'pizza/edit_order.html', {'form': form, 'pizza': pizza})
