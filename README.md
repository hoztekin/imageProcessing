# Görüntü İşleme ve Filtre Uygulaması

Bu uygulama, görüntü işleme teknikleri kullanarak çeşitli filtreler ve transformasyonlar uygulayan, Python ve Streamlit ile geliştirilmiş interaktif bir web uygulamasıdır.

## Canlı Demo

Uygulamayı çevrimiçi olarak test etmek için buraya tıklayın:
**[Görüntü Gri Formata Dönüştürücü](https://imageprocessing-hll.streamlit.app)**

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

2. Sanal ortam oluşturun (opsiyonel ama tavsiye edilir):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. Gerekli kütüphaneleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Uygulamayı çalıştırın:
```bash
streamlit run app.py
```

5. Browser'da şu adresi açın:
```
http://localhost:8501
```

## Kullanım

1. **Görüntü Yükleme**: Sol taraftaki "Bir görüntü yükleyin" butonuna tıklayarak JPG, JPEG veya PNG formatında bir görüntü seçin.

2. **İşlem Seçimi**: Aşağıdaki işlem türlerinden birini seçin:
   - Sadece Gri Formata Dönüştür
   - Gri Dönüştür ve Filtre Uygula
   - Sadece Filtre Uygula
   - Döndür/Aynala

3. **Parametre Ayarlama**: Filtre seçtiyseniz, filtre türünü ve yoğunluğunu ayarlayın.

4. **İşlemi Başlatma**: "İşlemi başlat" butonuna tıklayın.

5. **Sonuçları İnceleme**: Sağ tarafta işlenmiş görüntüyü ve histogram grafiğini görüntüleyin.

6. **İndirme**: "Görüntü indir" butonu ile işlenmiş görüntüyü bilgisayarınıza kaydedin.

## Kullanılan Teknolojiler

- **Streamlit**: Web arayüzü ve interaktif bileşenler
- **Pillow (PIL)**: Görüntü işleme ve manipülasyon
- **NumPy**: Matris işlemleri ve matematiksel hesaplamalar
- **Matplotlib**: Histogram grafikleri ve veri görselleştirme

## Dosya Yapısı

```
imageProcessing/
├── app.py                 # Ana uygulama dosyası
├── requirements.txt       # Proje bağımlılıkları
├── README.md             # Bu dosya
└── .gitignore            # Git için ignore listesi
```

## Eğitim ve Kaynaklar

Bu proje, Yılmaz Alacan'ın görüntü işleme eğitimleri üzerine kurgulanmış ve geliştirilmiştir. Temel görüntü işleme kavramları ve tekniklerinin pratik uygulaması olarak tasarlanmıştır.

## Deployment

Bu uygulama **Streamlit Cloud** üzerinde hosting edilmektedir. Kendi deployment'unuz için:

1. GitHub repository'sini oluşturun
2. `requirements.txt` dosyasını ekleyin
3. [Streamlit Cloud](https://streamlit.io/cloud) üzerinde kayıt olun
4. Repository'nizi bağlayın ve deploy edin

## Lisans

Bu proje eğitim amaçlı kullanılabilir.

## İletişim

Sorularınız veya geri bildiriminiz için GitHub issues bölümünü kullanabilirsiniz.