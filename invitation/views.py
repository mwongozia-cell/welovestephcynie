from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from datetime import datetime
import json

from .models import RSVP

@login_required
def home(request):
    name = request.user.first_name or request.user.username
    return render(request, 'invitation/home.html', {
        'event_date': '2025-11-20T00:00:00Z',
        'name': name
    })
def log_rsvp(rsvp_data):
    rsvp_data['timestamp'] = datetime.now().isoformat()
    with open('rsvp_log.json', 'a') as f:
        f.write(json.dumps(rsvp_data) + '\n')

def send_confirmation_email(name, email, rsvp_type, count=None, attendees=None):
    if not email:
        return

    subject = "Your RSVP Confirmation"
    if rsvp_type == 'attending':
        message = f"Hi {name}, thanks for RSVPing! We’ve received your response for {count} guest(s):\n" + \
                  "\n".join(attendees)
    elif rsvp_type == 'celebrating':
        message = f"Hi {name}, thanks for celebrating with us from afar! Your love means the world."
    elif rsvp_type == 'regrets':
        message = f"Hi {name}, thank you for your kind message. We’ll miss you at the celebration."

    send_mail(subject, message, None, [email])

@login_required
def rsvp_attending(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        count = int(request.POST.get('count', 1))
        attendees = request.POST.getlist('attendees') if count > 1 else [name]

        rsvp_data = {
            'type': 'attending',
            'name': name,
            'email': email,
            'count': count,
            'attendees': attendees,
        }

        log_rsvp(rsvp_data)

        RSVP.objects.create(
            name=name,
            rsvp_type='attending',
            count=count,
            attendees=', '.join(attendees)
        )

        send_confirmation_email(name, email, 'attending', count, attendees)

        return render(request, 'invitation/thank_you.html', {'rsvp_data': rsvp_data})
    return render(request, 'invitation/rsvp_attending.html')

@login_required
def rsvp_celebrating(request):
    return render(request, 'invitation/rsvp_celebrating.html')
@login_required
def contribute(request):
    return render(request, 'invitation/contribute.html')

@login_required
def rsvp_regrets(request):
    rsvp_data = {
        'type': 'regrets',
        'name': 'Guest',
        'email': None,
    }

    log_rsvp(rsvp_data)

    RSVP.objects.create(
        name='Guest',
        rsvp_type='regrets',
        count=0,
        attendees=''
    )

    return render(request, 'invitation/thank_you.html', {'rsvp_data': rsvp_data})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('invitation:home')
        else:
            return render(request, 'invitation/login.html', {'error': 'Invalid credentials'})
    return render(request, 'invitation/login.html')