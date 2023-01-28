
import numpy as np
from PIL import ImageGrab
import cv2

kamera=cv2.VideoCapture(0)

while (True):
    ret, goruntu = kamera.read()
    cv2.imshow("aaaa",goruntu)
    ornek=cv2.imread("cilt.jpg")
    OrnekResimDonustur = cv2.cvtColor(ornek, cv2.COLOR_BGR2GRAY)  # Tespit Edeceğimiz Resimi Gri Formata Donustur
    EkranGoruntusu = np.array(ImageGrab.grab(bbox=(0, 40, 600, 640)))  # Anlik Ekran Goruntusunu Al
    EkranGoruntusuDonustur = cv2.cvtColor(EkranGoruntusu,
                                          cv2.COLOR_BGR2GRAY)  # Ekran Goruntusunu Gri Formata Donusturuyoruz
    Sonuc = cv2.matchTemplate(EkranGoruntusuDonustur, OrnekResimDonustur,
                              cv2.TM_CCOEFF_NORMED)  # Ekran Grountusunun Icerisinde Resmi Ariyoruz
    sin_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Sonuc)  # Bulunan Objenin Koordinatlarini Bul
    Ust_Sol = max_loc  # Bulunan Objenin Ust ve Sol Uzakligi
    Alt_Sag = (Ust_Sol[0] + 50, Ust_Sol[1] + 50)
    cv2.rectangle(EkranGoruntusu, Ust_Sol, Alt_Sag, (0, 255, 0), 5)
    cv2.imshow('cilt', EkranGoruntusu)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
