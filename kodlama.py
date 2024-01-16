import cv2
import numpy as np

#en anlamlı bit

def en_anlami_bit_gizle(img, data):

    data_bin = ''.join(format(ord(char), '08b') for char in data)
    data_index = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if data_index < len(data_bin):
                    img[i, j, k] = img[i, j, k] & 0b11111110 | int(data_bin[data_index])
                    data_index += 1
    
    return

def en_Anlamli_bit_cikar(img):

    extracted_data = ''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                extracted_data += str(img[i,j,k] & 1)
    
    extracted_text= ''.join(chr(int(extracted_data[i:i+8], 2)) for i in range(0, len(extracted_data), 8))
    return extracted_text

#en anlamsız bit

def en_anlamsiz_bit_gizle(img, data):

    data_bin = ''.join(format(ord(char), '08b') for char in data)
    data_index = 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range (img.shape[2]):
                if data_index < len(data_bin):
                    img[i, j, k] = img[i, j, k] & 0b01111111 | (int(data_bin[data_index]) << 7)
                    data_index += 1

    return img

def en_anlamsiz_bit_cikar(img):

    extracted_data = ''
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                extracted_data += str(img[i, j, k] >> 7)

    extracted_text = ''.join(chr(int(extracted_data[i:i+8], 2)) for i in range(0, len(extracted_data), 8))
    return extracted_text

def psnr(img1, img2):
    mse = np.mean((img1 - img2)**2)
    psnr_val = 10 * np.log10((255**2)/mse)
    return psnr_val

orjinal_mesaj="GİZLİ MESAJ İÇERİR"
img_path="ornek.jpg"

orijinal_img=cv2.imread(img_path)

img_lsb= en_anlami_bit_gizle(orijinal_img.copy(), orjinal_mesaj)

extracted_message_lsb = en_Anlamli_bit_cikar(img_lsb.copy())

img_msb = en_anlamsiz_bit_gizle(orijinal_img.copy(), orjinal_mesaj)

extracted_message_msb = en_anlamsiz_bit_cikar(img_msb.copy())

psnr_lsb = psnr(orijinal_img, img_lsb)
psnr_msb = psnr(orijinal_img, img_msb)

print("Orijinal Mesaj:", orjinal_mesaj)
print("\nEn Anlamlı Bit Yöntemi:")
print("Gizlenen Mesaj:", extracted_message_lsb)
print("PSNR Değeri:", psnr_lsb)
print("\nEn Anlamsız Bit Yöntemi:")
print("Gizlenen Mesaj:", extracted_message_msb)
print("PSNR Değeri:", psnr_msb)