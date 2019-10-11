from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Enter your email address'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Enter subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-3',
        'placeholder': 'Enter message'}))