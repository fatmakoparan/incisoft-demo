from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from blog.forms import ContactForm  # 'blog' uygulamasından import et
# Home page view
def index(request):
    return render(request, 'myproject/index.html')

def portfolio(request):
    return render(request, 'myproject/portfolio.html')

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
            recipient_list = ['fatmakoparaan@gmail.com']

            try:
                send_mail(
                    subject,
                    message_body,
                    from_email,
                    recipient_list,
                    fail_silently=False,
                )
                return render(request, 'myproject/contact.html', {'form': form, 'success': True})
            except Exception as e:
                return render(request, 'myproject/contact.html', {'form': form, 'error': str(e)})
        else:
            return render(request, 'myproject/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'myproject/contact.html', {'form': form})

def service(request):
    return render(request, 'myproject/service.html')

#def blog(request):
#    return render(request, 'myproject/blog.html')

def about(request):
    return render(request, 'myproject/about.html')

def vision(request):
    return render(request, 'myproject/vision.html')

#def blog1(request):
#    return render(request, 'myproject/blog1.html')

#def blog2(request):
#    return render(request, 'myproject/blog2.html')

#def blog3(request):
#    return render(request, 'myproject/blog3.html')
