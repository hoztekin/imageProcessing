import streamlit as st 
import cv2
import numpy as np
from PIL import Image
import io

# Sayfa Yapılandırması

st.set_page_config(
    page_title = "Görüntü Gri Formata Dönüştürücü",
    page_icon = "",
    layout = "wide",
    initial_sidebar_state="expanded"
)

def load_image(image_file):
    "Yüklenen görüntüyü okur ve döndürür."
    img=Image.open(image_file)
    return img

def convert_to_grayscale(img):
    "Görüntüyü gri formata dönüştürür"
    img_array = np.array(img)
    if len(img_array.shape) == 3 and img_array.shape[2] == 3 :
        gray_img = img.convert('L')
        return gray_img
    
    else :
        return img

def apply_filter(img, filter_type, intensity=1.0):
    img_array = np.array(img)
    if filter_type == "Bulanıklaştırma":
        kernel_size = int(intensity * 3)
        if kernel_size % 2 == 0:
            kernel_size += 1
        if len(img_array.shape) == 3 :
            filtered_img = cv2.GaussianBlur(img_array,(kernel_size, kernel_size), 0)
        else:
            filtered_img = cv2.GaussianBlur(img_array,(kernel_size, kernel_size), 0)

    elif filter_type == "Keskinleştirme":
        kernel = np.array([[-1, -1, -1],
                            [-1, 9, -1],
                           [-1, -1, -1]]) * intensity
        if len(img_array.shape) == 3 :
            filtered_img = cv2.filter2D(img_array, -1, kernel)
        else:
            filtered_img = cv2.filter2D(img_array, -1, kernel)

    elif filter_type == "Kenar Algılama":
        if len(img_array.shape) == 3 :
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else :
            gray = img_array
        threshold1 = 50*intensity
        threshold2 = 150*intensity
        edges = cv2.Canny(gray, threshold1, threshold2)
        filtered_img = edges

    elif filter_type == "Negatif":
        filtered_img = 255 - img_array
    
    else :
        filtered_img = img_array

    filtered_img = np.clip(filtered_img, 0, 255).astype(np.uint8)

    if len(filtered_img.shape) == 2 :
        return Image.fromarray(filtered_img, mode = 'L')
    else :
        return Image.fromarray(filtered_img)
    
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
    
def sidebar_content():
    st.sidebar.title("Hakkında")
    st.sidebar.info(
        "Bu uygulama, üniversite öğrencileri hazırlanan"
        "bir gelişim kampı projesi olarak tasarlanmıştır."
        "Görüntü işleme ve streamlit kullanımı konusunda"
        "temel bir örnek sunmaktadır."
    )
    st.sidebar.title("Nasıl Kullanılır")
    st.sidebar.markdown(
        """
        1. Sol taraftaki 'Bir görüntü yükleyin' butona tıklayın.
        2. Bilgisayarınızdan bir görüntü seçin (JPG, JPEG veya PNG).
        3. 'Gri gormata dönüştür' butonuna tıklayın.
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
        """
    )
    
def main():
        
        add_custom_css()
        sidebar_content()
        
        st.markdown('<h1 class="main-header"> Görüntü Gri Formata Dönüştürücü </h1>', unsafe_allow_html=True)
        st.markdown('<p class="info-text"> Bu uygulama yüklediğiniz görüntüyü gri formata dönüştürür ve çeşitli filtreler uygulamamıza olanak sağlar.</p>', unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)
        
        #Görüntü yükleme
        
        with col1:
            uploaded_file = st.file_uploader("Bir görüntü yükleyin", type=["jpg","png","jpeg"])
            
            if uploaded_file is not None:
                image = load_image(uploaded_file)
                with col1:
                    st.markdown('<h2 class="sub-header">Orjinal Görüntü</h2>', unsafe_allow_html=True)
                    st.image(image,caption="Yüklenen Görüntü",use_column_width=True)
                    
                    st.markdown('<h3 class="sub-header">Görüntü Bilgileri</h3>', unsafe_allow_html=True)
                    img_array= np.array(image)
                    st.write(f"Boyut: {img_array.shape[1]}x{img_array.shape[0]}")
                    if len(img_array.shape) == 3:
                        st.write(f"Kanal sayısı:{img_array.shape[2]}")
                        st.write(f"Renk formatı: RGB")
                    else:
                        st.write(f"Kanal sayısı: 1")
                        st.write(f"Renk formatı: Gri Tonlama")
                        
                #İşlem Seçenekleri
                st.markdown('<h3 class= "sub-header">İşlem Seçenekleri</h3>', unsafe_allow_html=True)
                process_option = st.radio(
                    "İşlem türünü seçin:",
                    ["Sadece Gri Formata Dönüştür", "Gri Dönüştür ve Filtre Uygula", "Sadece Filtre Uygula"]
                )        
                
                if "Filtre" in process_option:
                    filter_type = st.selectbox(
                        "Filtre türünü seçin:",
                        ["Bulanıklaştırma", "Keskinleştirme", "Kenar Algılama", "Negatif"]                        
                    )
                    intensity = st.slider(
                        "Filtre Yoğunluğu",
                        min_value=0.1,
                        max_value=2.0,
                        value=1.0,
                        step=0.1
                    )
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
                                processed_image = apply_filter(gray_image,filter_type,intensity)
                                result_caption = f"Gri formatlı ve {filter_type} filtresi uygulanmış görüntü"
                            else:
                                st.info(f"{filter_type} filtresi uygulanıyor...")
                                processed_image = apply_filter(image,filter_type,intensity)
                                result_caption = f"{filter_type} filtresi uygulanmış görüntü"
                                
                            with col2:
                                st.markdown('<h2 class="sub-header">İşlenmiş görüntü</h2>', unsafe_allow_html=True)
                                st.image(processed_image,caption=result_caption,use_column_width=True)
                                
                                buf= io.BytesIO()
                                processed_image.save(buf,format="PNG")
                                byte_img= buf.getvalue()
                                st.download_button(
                                    label=" Görüntü indir",
                                    data= byte_img,
                                    file_name= "processed_image.png",
                                    mime= "image/png"
                                )
                        except Exception as e:
                            st.error(f"Bir hata oluştu :{e}")
                            st.error(f"Lütfen farklı bir görüntü ve dosya seçiniz")
            else:
                st.info("Lütfen bir görüntü yükleyin. Desteklenen formatlar: JPG, JPEG ve PNG")

if __name__== "__main":
    main()