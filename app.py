import streamlit as st
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import io
import matplotlib.pyplot as plt

# Sayfa Yapılandırması

st.set_page_config(
    page_title="Görüntü Gri Formata Dönüştürücü",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_image(image_file):
    "Yüklenen görüntüyü okur ve döndürür."
    img = Image.open(image_file)
    return img


def convert_to_grayscale(img):
    "Görüntüyü gri formata dönüştürür"
    return img.convert('L')


def apply_filter(img, filter_type, intensity=1.0):
    if filter_type == "Bulanıklaştırma":
        blur_radius = int(intensity * 3)
        filtered_img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    elif filter_type == "Keskinleştirme":
        filtered_img = img.filter(ImageFilter.SHARPEN)
        if intensity > 1.0:
            for _ in range(int(intensity)):
                filtered_img = filtered_img.filter(ImageFilter.SHARPEN)

    elif filter_type == "Kenar Algılama":
        filtered_img = img.filter(ImageFilter.FIND_EDGES)

    elif filter_type == "Negatif":
        if img.mode == 'L':
            img_array = np.array(img)
            filtered_img = Image.fromarray(255 - img_array)
        else:
            filtered_img = ImageOps.invert(img.convert('RGB'))

    elif filter_type == "Sepia":
        img_array = np.array(img.convert('RGB'))
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                 [0.349, 0.686, 0.168],
                                 [0.393, 0.769, 0.189]])

        sepia_img = np.dot(img_array, sepia_filter.T)
        sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

        # Yoğunluk ayarı
        blended = np.uint8(img_array * (1 - intensity) + sepia_img * intensity)
        filtered_img = Image.fromarray(blended)
    else:
        filtered_img = img

    return filtered_img


def add_custom_css():
    st.markdown("""
                <style>

                .main-header{
                    font-size: 2.5rem;
                    color: #4527A0;
                    text-align: center;
                    margin-bottom: 1rem;
                }

                .sub-header{
                    font-size: 1.5 rem;
                    color: #5E35B1;
                    margin-top: 1rem;
                    margin-bottom: 0.5rem;
                }

                .info-text{
                    font-size: 1rem;
                    color: #333;
                    margin-bottom: 1rem;
                }

                .stButton>button{
                    background-color: #5E35B1;
                    color: white;
                    font-weight: bold;
                    border-radius: 5px;
                    padding: 0.5rem 1rem;
                    border: none;
                }
                .stButton>button:hover{
                    background-color: #4527A0;
                }

                </style>
                """, unsafe_allow_html=True)


def rotate_flip_image(img, operation):
    """Görüntüyü döndürür veya aynalar"""

    if operation == "90° Sağa Döndür":
        rotated = img.rotate(-90, expand=True)
    elif operation == "90° Sola Döndür":
        rotated = img.rotate(90, expand=True)
    elif operation == "180° Döndür":
        rotated = img.rotate(180, expand=True)
    elif operation == "Yatay Aynala":
        rotated = ImageOps.mirror(img)
    elif operation == "Dikey Aynala":
        rotated = ImageOps.flip(img)
    else:
        rotated = img

    return rotated


def sidebar_content():
    st.sidebar.title("Hakkında")
    st.sidebar.info(
        "Bu uygulama, üniversite öğrencileri tarafından hazırlanan"
        "bir gelişim kampı projesi olarak tasarlanmıştır."
        "Görüntü işleme ve streamlit kullanımı konusunda"
        "temel bir örnek sunmaktadır."
    )
    st.sidebar.title("Nasıl Kullanılır")
    st.sidebar.markdown(
        """
        1. Sol taraftaki 'Bir görüntü yükleyin' butona tıklayın.
        2. Bilgisayarınızdan bir görüntü seçin (JPG, JPEG veya PNG).
        3. 'Gri formata dönüştür' butonuna tıklayın.
        4. İsterseniz ek filtreler uygulayabilirsiniz.
        5. Dönüştürülen görüntüyü indirmek için 'Görüntüyü indir' butonuna tıklayın.
        """
    )

    st.sidebar.title("Görüntü İşleme Hakkında")
    st.sidebar.markdown(
        """
        ** Gri formata Dönüştürme Nedir?**
        Renkli bir görüntüyü gri formata dönüştürmek,
        her pikselin renk bilgisini (RGB) tek gri
        ton değerine dönüştürme işlemdir.

        ** Filtreler Hakkında **
        - **Bulanıklaştırma**: Görüntüdeki gürültüyü azaltır ve detayları yumuşatır.
        - **Keskinleştirme** : Görüntüdeki kenarları ve detayları vurgular.
        - **Kenar Algılama** : Görüntüdeki nesnelerin kenarlarını tespit eder.
        - **Negatif** : Görüntünün renklerini tersine çevirir.
        - **Sepia** : Görüntüye nostaljik, eski fotoğraf görünümü kazandırır.
        """
    )


def plot_histogram(img):
    """Görüntünün histogram grafiğini oluşturur"""
    img_array = np.array(img)

    fig, ax = plt.subplots(figsize=(10, 4))

    if len(img_array.shape) == 3:
        # RGB görüntü için
        colors = ('red', 'green', 'blue')
        labels = ('Kırmızı', 'Yeşil', 'Mavi')
        for i, (color, label) in enumerate(zip(colors, labels)):
            histogram = np.histogram(img_array[:, :, i], bins=256, range=(0, 256))
            ax.plot(histogram[0], color=color, label=label, alpha=0.7, linewidth=2)
        ax.set_xlabel('Piksel Değeri')
        ax.set_ylabel('Frekans')
        ax.set_title('RGB Histogram')
        ax.legend()
        ax.grid(True, alpha=0.3)
    else:
        # Gri görüntü için
        histogram = np.histogram(img_array, bins=256, range=(0, 256))
        ax.plot(histogram[0], color='gray', linewidth=2)
        ax.fill_between(range(256), histogram[0], alpha=0.3, color='gray')
        ax.set_xlabel('Piksel Değeri')
        ax.set_ylabel('Frekans')
        ax.set_title('Gri Tonlama Histogram')
        ax.grid(True, alpha=0.3)

    ax.set_xlim([0, 256])
    plt.tight_layout()
    return fig


def main():
    add_custom_css()
    sidebar_content()

    st.markdown('<h1 class="main-header"> Görüntü Gri Formata Dönüştürücü </h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="info-text"> Bu uygulama yüklediğiniz görüntüyü gri formata dönüştürür ve çeşitli filtreler uygulamamıza olanak sağlar.</p>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Görüntü yükleme

    with col1:
        uploaded_file = st.file_uploader("Bir görüntü yükleyin", type=["jpg", "png", "jpeg"])

        if uploaded_file is not None:
            image = load_image(uploaded_file)
            with col1:
                st.markdown('<h2 class="sub-header">Orjinal Görüntü</h2>', unsafe_allow_html=True)
                st.image(image, caption="Yüklenen Görüntü", use_column_width=True)

                st.markdown('<h3 class="sub-header">Görüntü Bilgileri</h3>', unsafe_allow_html=True)
                st.write(f"Boyut: {image.width}x{image.height}")
                st.write(f"Format: {image.mode}")
                if image.mode == 'RGB':
                    st.write(f"Renk formatı: RGB")
                elif image.mode == 'L':
                    st.write(f"Renk formatı: Gri Tonlama")
                else:
                    st.write(f"Renk formatı: {image.mode}")

                st.markdown('<h3 class="sub-header">Histogram</h3>', unsafe_allow_html=True)
                histogram_fig = plot_histogram(image)
                st.pyplot(histogram_fig)
                plt.close()

                # İşlem Seçenekleri
            st.markdown('<h3 class= "sub-header">İşlem Seçenekleri</h3>', unsafe_allow_html=True)
            process_option = st.radio(
                "İşlem türünü seçin:",
                ["Sadece Gri Formata Dönüştür", "Gri Dönüştür ve Filtre Uygula", "Sadece Filtre Uygula",
                 "Döndür/Aynala"]
            )

            if "Filtre" in process_option:
                filter_type = st.selectbox(
                    "Filtre türünü seçin:",
                    ["Bulanıklaştırma", "Keskinleştirme", "Kenar Algılama", "Negatif", "Sepia"]
                )
                intensity = st.slider(
                    "Filtre Yoğunluğu",
                    min_value=0.1,
                    max_value=2.0,
                    value=1.0,
                    step=0.1
                )

            if process_option == "Döndür/Aynala":
                rotation_option = st.selectbox("İşlem seçin:",
                                               ["90° Sağa Döndür", "90° Sola Döndür", "180° Döndür", "Yatay Aynala",
                                                "Dikey Aynala"])

            process_button = st.button("İşlemi başlat")

            if process_button:
                try:
                    if process_option == "Sadece Gri Formata Dönüştür":
                        st.info("Görüntü gri formata dönüştürülüyor...")
                        processed_image = convert_to_grayscale(image)
                        result_caption = "Gri formatlı görüntü"
                    elif process_option == "Gri Dönüştür ve Filtre Uygula":
                        st.info("Görüntü gri formata dönüştürülüyor ve filtre uygulanıyor...")
                        gray_image = convert_to_grayscale(image)
                        processed_image = apply_filter(gray_image, filter_type, intensity)
                        result_caption = f"Gri formatlı ve {filter_type} filtresi uygulanmış görüntü"
                    elif process_option == "Döndür/Aynala":
                        st.info(f"Görüntü işleniyor: {rotation_option}...")
                        processed_image = rotate_flip_image(image, rotation_option)
                        result_caption = f"{rotation_option} uygulanmış görüntü"
                    else:
                        st.info(f"{filter_type} filtresi uygulanıyor...")
                        processed_image = apply_filter(image, filter_type, intensity)
                        result_caption = f"{filter_type} filtresi uygulanmış görüntü"

                    with col2:
                        st.markdown('<h2 class="sub-header">İşlenmiş görüntü</h2>', unsafe_allow_html=True)
                        st.image(processed_image, caption=result_caption, use_column_width=True)

                        st.markdown('<h3 class="sub-header">İşlenmiş Görüntü Histogram</h3>', unsafe_allow_html=True)
                        processed_histogram_fig = plot_histogram(processed_image)
                        st.pyplot(processed_histogram_fig)
                        plt.close()

                        buf = io.BytesIO()
                        processed_image.save(buf, format="PNG")
                        byte_img = buf.getvalue()
                        st.download_button(
                            label=" Görüntü indir",
                            data=byte_img,
                            file_name="processed_image.png",
                            mime="image/png"
                        )
                except Exception as e:
                    st.error(f"Bir hata oluştu :{e}")
                    st.error(f"Lütfen farklı bir görüntü ve dosya seçiniz")
        else:
            st.info("Lütfen bir görüntü yükleyin. Desteklenen formatlar: JPG, JPEG ve PNG")


if __name__ == "__main__":
    main()