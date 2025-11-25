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

# 2. Sanal ortam oluşturun ve aktive edin
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

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
python manage.py makemigrations
python manage.py migrate

# 6. Süper kullanıcı oluşturun (opsiyonel)
python manage.py createsuperuser

# 7. Projeyi çalıştırın
python manage.py runserver

# Tarayıcıda görüntüleme:
# http://127.0.0.1:8000/


**Notlar**  
Bu proje tamamen demo amaçlıdır. Ticari bir ürün değildir. Canlıya alınması planlanmamaktadır.

**Lisans**  
Bu projede henüz lisans tanımlanmamıştır.
