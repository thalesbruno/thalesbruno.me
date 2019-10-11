from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
        return redirect('thanks/')
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)


def thanks(request):
    return render(request, 'thanks.html', {})