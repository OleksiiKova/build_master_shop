from django.contrib import messages
from django.shortcuts import render, redirect

import pprint

from .forms import ContactForm
from blog.models import BlogPost


def index(request):
    """
    A view to return the index page.

    Retrieves the 3 most recent blog posts from the database and renders the
    index page.
    Passes the latest blog posts to the template to be displayed.
    """
    latest_posts = BlogPost.objects.order_by('-published_date')[:3]
    return render(request, 'home/index.html', {'latest_posts': latest_posts})


def privacy_policy(request):
    """
    A view to return the privacy policy page.

    Renders the privacy policy page to the user. This page typically includes
    information about how user data is collected and used.
    """
    return render(request, 'home/privacy_policy.html')


def terms_of_service(request):
    """
    A view to return the terms of service page.

    Renders the terms of service page to the user. This page typically includes
    the legal terms that govern the use of the website or service.
    """
    return render(request, 'home/terms_of_service.html')


def contact_us(request):
    """
    A view to handle contact form submissions.

    If the form is submitted via POST and is valid, it saves the form data,
    sends a success message to the user, and redirects them to the homepage.
    If there are errors with the form, an error message is shown to the user.
    If the request is a GET request, a blank form is displayed.

    Arguments:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The rendered contact form template with either success
        or error messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for your message! We '
                             'endeavour to respond within 2 working days!')
            return redirect('home')
        else:
            messages.error(
                request, f'Please correct the errors below.')
    else:
        form = ContactForm()

    template = 'home/contact_us.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    print("Context:", pprint.pformat(context))

    return render(request, template, context)
