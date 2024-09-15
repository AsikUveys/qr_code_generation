import os
from PIL import Image
import qrcode
import time

def generate_qr_code(url):
    # Klasörün var olup olmadığını kontrol edin, yoksa oluşturun
    folder = 'qr_image'
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # QR kodu oluşturun
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    image = qr.make_image(fill='black', back_color='white')
    timestamp = int(time.time())
    
    # QR kodunu kaydedin
    image.save(f'{folder}/qr_{timestamp}.png')  # Zaman damgası kullanılarak dosya adı oluşturulur
    print(f'QR kodu {folder}/qr_{timestamp}.png olarak kaydedildi.')

# Örnek kullanım
url = '.......'
generate_qr_code(url)


