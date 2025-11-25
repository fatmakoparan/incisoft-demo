from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Adınız", max_length=50, min_length=2, required=True)
    email = forms.EmailField(label="E-posta", required=True)
    phone = forms.CharField(label="Telefon", max_length=15, min_length=10, required=True)
    message = forms.CharField(label="Mesaj", max_length=1000, min_length=10, required=True, widget=forms.Textarea)