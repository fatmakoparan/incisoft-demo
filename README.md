# Incisoft Demo

## Project Overview (English)
**Incisoft Demo** is a web application developed using Python and Django. The project includes both **backend** and **frontend** components, and uses **PostgreSQL** as its database.  

- **Blog Application:** Allows users to create and view blog posts.  
- **Contact Application:** Visitors can leave their name, email, phone number, and message to get in touch.  

**Setup and Running**
```bash
git clone <project-repo-link>
cd incisoft_demo
cd incisoft_project
```
# Create and activate virtual environment
# Windows
```bash
python -m venv venv
venv\Scripts\activate
```
# Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
# Install dependencies
```bash
pip install -r requirements.txt
```
# Configure database (update settings.py)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '<database_name>',
#         'USER': '<username>',
#         'PASSWORD': '<password>',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
# Create superuser (optional)
```bash
python manage.py createsuperuser
```
# Run project
```bash
python manage.py runserver
```
# View in browser
```bash
http://127.0.0.1:8000/

```


# Incisoft Demo

## Proje Hakkında
**Incisoft Demo**, Python ve Django kullanılarak geliştirilmiş bir web uygulamasıdır. Projede hem **backend** hem de **frontend** bileşenleri bulunmaktadır. Veritabanı olarak **PostgreSQL** kullanılmıştır.  

- **Blog Uygulaması:** Kullanıcılar blog yazıları oluşturabilir ve görüntüleyebilir.  
- **Contact Uygulaması:** Ziyaretçiler isim, e-posta, telefon ve mesaj bilgilerini bırakarak iletişim kurabilir.  

## Kurulum ve Çalıştırma
```bash
# 1. Projeyi klonlayın ve proje klasörüne girin
git clone <proje-repo-linki>
cd incisoft_demo
cd incisoft_project  # Django ana proje klasörüne geçin
```
# 2. Sanal ortam oluşturun ve aktive edin
# Windows
```bash
python -m venv venv
venv\Scripts\activate
```
# Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
# 3. Bağımlılıkları yükleyin
```bash
pip install -r requirements.txt
```
# 4. Veritabanı ayarlarını yapın
# incisoft_project/settings.py dosyasında PostgreSQL bağlantısını güncelleyin:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': '<veritabani_adi>',
#         'USER': '<kullanici_adi>',
#         'PASSWORD': '<sifre>',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# 5. Veritabanı migrasyonlarını uygulayın
```bash
python manage.py makemigrations
python manage.py migrate
```
# 6. Süper kullanıcı oluşturun (opsiyonel)
```bash
python manage.py createsuperuser
```
# 7. Projeyi çalıştırın
```bash
python manage.py runserver
```
# Tarayıcıda görüntüleme:
```bash
# http://127.0.0.1:8000/
```

**Notlar**  
Bu proje tamamen demo amaçlıdır. Ticari bir ürün değildir. Canlıya alınması planlanmamaktadır.

**Lisans**  
Bu projede henüz lisans tanımlanmamıştır.
