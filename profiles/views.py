from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
# from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {
        # 'form': form,
        # 'orders': orders,
        # 'on_profile_page': True
    }

    return render(request, template, context)


