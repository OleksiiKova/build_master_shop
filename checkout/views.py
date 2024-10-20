from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing in your cart at the moment')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PuAsa2KzsAtyLJOKqvX2IPHK0zV6LYc2zMHZACxaS43rBWG5sQlCzUaw5SMBh2VmAsnXCSPnC3EdDRDqB52XQaD00aPDol2vC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)