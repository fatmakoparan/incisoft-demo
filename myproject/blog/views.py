from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def blog_list(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'myproject/blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'myproject/blog_detail.html', {'blog': blog})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            subject = f'Yeni İletişim Formu: {name}'
            message_body = f'Ad: {name}\nE-posta: {email}\nTelefon: {phone}\nMesaj: {message}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['fatmakoparaan@gmail.com']  # Kendi mail adresin

            try:
                send_mail(subject, message_body, from_email, recipient_list, fail_silently=False)
                return render(request, 'myproject/contact.html', {'form': form, 'success': True})
            except Exception as e:
                return render(request, 'myproject/contact.html', {'form': form, 'error': str(e)})
    else:
        form = ContactForm()
    return render(request, 'myproject/contact.html', {'form': form})