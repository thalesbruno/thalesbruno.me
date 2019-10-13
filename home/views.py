from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, BadHeaderError
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                email = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=['thalesbrunom@gmail.com']
                )
                email.send()
            except Exception as e:
                print(e)
                return redirect('home')
        return redirect('thanks')
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


def thanks(request):
    return render(request, 'thanks.html', {})