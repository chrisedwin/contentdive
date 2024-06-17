from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Subscriber, Title

def subscribe(request):
    notification = None
    success = False

    if request.method == 'POST' and 'subscribe' in request.POST:
        email = request.POST.get('email')
        try:
            validate_email(email)  # Validate email format
            Subscriber.objects.create(email=email)
            notification = 'Subscribed successfully!'
            success = True
        except ValidationError:
            notification = 'Invalid email format. Please provide a valid email address.'

    return render(request, 'resources/subscribe.html', {'notification': notification, 'success': success})


def title(request):
    notification = None
    success = False

    if request.method == 'POST' and 'title' in request.POST:
        title = request.POST.get('title')
        try:
            Title.objects.create(title=title)
            notification = 'Request successfully!'
            success = True
        except ValidationError:
            notification = 'Invalid request. Please provide a valid address.'

    return render(request, 'resources/title.html', {'notification': notification, 'success': success})


def policy(request):
    return render(request, 'resources/policy.html')

def terms(request):
    return render(request, 'resources/terms.html')