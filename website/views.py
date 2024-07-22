from django.shortcuts import render, redirect
import ssl
from smtplib import SMTP
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
# def web(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())
# def web(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         subject = request.POST['subject']
#         message = request.POST['message']
#         send_mail(
#         name,
#         email,
#         phone,
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         ['ak7379jaiswal@gmail.com'],
#         fail_silently=False
#         )
#     return render(request, "index.html", context={'page':'Home'})
def web(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            print(message_body)
            # Create a custom SSL context
            ssl_context = ssl.create_default_context(cafile=settings.EMAIL_SSL_CERTFILE)

            try:
                with SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as smtp:
                    smtp.starttls(context=ssl_context)
                    smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                    smtp.sendmail(
                        settings.EMAIL_HOST_USER,
                        ['anil.focuscode@gmail.com'],
                        f"Subject: {subject}\n\n{message_body}"
                    )
                return redirect('success')
            except Exception as e:
                return render(request, 'index.html', context={'page': 'Home', 'error': str(e)})
            return redirect('success')
    else:
        form = ContactForm()
        

    return render(request, 'index.html', context={'page': 'Home','form':form})
def success(request):
    return render(request, "success_view.html")

def about(request):
    return render(request, "about.html", context={'page':'About Us'})

def contact(request):
    return render(request, "contact.html", context={'page':'Contact Us'})

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Success Page in Website</h1>")

