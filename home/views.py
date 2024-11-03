from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from blog.models import BlogPost
import pprint



def index(request):
    """
    A view to return the index page
    """
    latest_posts = BlogPost.objects.order_by('-published_date')[:3]
    return render(request, 'home/index.html', {'latest_posts': latest_posts})


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def terms_of_service(request):
    return render(request, 'home/terms_of_service.html')


def contact_us(request):
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
