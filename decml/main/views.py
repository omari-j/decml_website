from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Emails



def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            first = contact_form.cleaned_data["first_name"]
            last = contact_form.cleaned_data["last_name"]
            email = contact_form.cleaned_data["email"]
            website = contact_form.cleaned_data["website"]
            company = contact_form.cleaned_data["company"]
            message = contact_form.cleaned_data["message"]
            send_mail(
                subject="decml Contact Form Completion",
                message=f"Sender: {first} {last}"
                f"Email: {email}"
                f"Website: {website}"
                f"Company: {company}"
                f"{message}",
                from_email="omarisemail@gmail.com",
                recipient_list=["omarisemail@gmail.com"],
                fail_silently=False
            )
            email = Emails(
                first_name=first,
                last_name=last,
                email=email,
                company=company,
                website=website,
                message=message
            )
            email.save()
            return redirect("main:home")
    else:
        contact_form = ContactForm()
    return render(request, 'main/contact.html', {
        'form': contact_form
    })


def portfolio(request):
    return render(request, 'main/portfolio.html')


def home(request):
    return render(request, 'main/home.html')


def thank_you(request):
    return render(request, 'main/thank_you.html')
