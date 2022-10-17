import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Achievements(request):
    return render(request, 'Achievements.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('form_name')
        phone = request.POST.get('form_phone')
        email = request.POST.get('form_email')
        subject = request.POST.get('form_subject')
        message = request.POST.get('form_message')
        
        data = {
            'name': name,
            'phone': phone,
            'email': email,
            'subject': subject,
            'message': message
        }
        
        message = '''
        New Message: {}
        
        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['ssshahriar17@gmail.com']) 
        
               
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def kiloflight(request):
    return render(request, 'kiloflight.html')

def outreach(request):
    return render(request, 'outreach.html')

def project(request):
    return render(request, 'project.html')

def team(request):
    return render(request, 'team.html')