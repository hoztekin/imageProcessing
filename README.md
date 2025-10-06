# Görüntü İşleme ve Filtre Uygulaması

Bu uygulama, görüntü işleme teknikleri kullanarak çeşitli filtreler ve transformasyonlar uygulayan, Python ve Streamlit ile geliştirilmiş interaktif bir web uygulamasıdır.

## Özellikler

### Temel İşlemler
- **Gri Tonlama Dönüşümü**: Renkli görüntüleri gri tonlamalı formata dönüştürme
- **Görüntü Bilgileri**: Boyut, kanal sayısı ve renk formatı analizi
- **Histogram Analizi**: RGB ve gri tonlama histogram grafikleri

### Filtreler
- **Bulanıklaştırma**: Gaussian blur ile görüntü yumuşatma
- **Keskinleştirme**: Kenar ve detay vurgulama
- **Kenar Algılama**: Canny algoritması ile kenar tespiti
- **Negatif**: Renk tersine çevirme
- **Sepia**: Nostaljik, eski fotoğraf efekti

### Transformasyonlar
- **Döndürme**: 90° sağa, 90° sola ve 180° döndürme
- **Aynalama**: Yatay ve dikey aynalama işlemleri

### Diğer Özellikler
- Filtre yoğunluk kontrolü
- İşlenmiş görüntüleri PNG formatında indirme
- Orijinal ve işlenmiş görüntü karşılaştırması
- Responsive ve kullanıcı dostu arayüz

## Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip paket yöneticisi

### Adımlar

1. Repository'yi klonlayın:
```bash
git clone https://github.com/hoztekin/imageProcessing.git
cd imageProcessing
```

2. Gerekli kütüphaneleri yükleyin:
   pip install streamlit opencv-python numpy pillow matplotlib

3. Uygulamayı çalıştırın:
   streamlit run app.py


Kullanım

Görüntü Yükleme: Sol taraftaki "Bir görüntü yükleyin" butonuna tıklayarak JPG, JPEG veya PNG formatında bir görüntü seçin.
İşlem Seçimi: Aşağıdaki işlem türlerinden birini seçin:

Sadece Gri Formata Dönüştür
Gri Dönüştür ve Filtre Uygula
Sadece Filtre Uygula
Döndür/Aynala


Parametre Ayarlama: Filtre seçtiyseniz, filtre türünü ve yoğunluğunu ayarlayın.
İşlemi Başlatma: "İşlemi başlat" butonuna tıklayın.
Sonuçları İnceleme: Sağ tarafta işlenmiş görüntüyü, histogram grafiğini görüntüleyin.
İndirme: "Görüntü indir" butonu ile işlenmiş görüntüyü bilgisayarınıza kaydedin.

Kullanılan Teknolojiler

Streamlit: Web arayüzü ve interaktif bileşenler
OpenCV: Görüntü işleme operasyonları
NumPy: Matris işlemleri ve matematiksel hesaplamalar
Pillow (PIL): Görüntü okuma ve kaydetme
Matplotlib: Histogram grafikleri ve veri görselleştirme


Eğitim ve Kaynaklar

Bu proje, Yılmaz Alacan'ın görüntü işleme eğitimleri üzerine kurgulanmış ve geliştirilmiştir. Temel görüntü işleme kavramları ve tekniklerinin pratik uygulaması olarak tasarlanmıştır.











   
