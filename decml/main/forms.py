from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last name", max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.CharField(label="Company", max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    website = forms.CharField(label="Your website", max_length=100, widget=forms.URLInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Your business email", max_length=100, required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    message = forms.CharField(label="Your message", widget=forms.Textarea(attrs={"class": "form-control"}))
