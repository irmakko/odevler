import pygame
import sys
import threading
import time
#EKRAN BOYUTLARI
width, height = 800, 600
ekran = pygame.display.set_mode((width, height))
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Araba Projesi")

#RENKLER VE BÜYÜKLÜK
araba1_rengi = (255, 0, 0)  # Kırmızı
araba2_rengi = (0, 0, 255)  # Mavi
araba_width = 50
araba_height = 30

#ARABA SINIFI
class Araba:
    def __init__(self, x, y, hiz, renk):
        self.x = x
        self.y = y
        self.hiz = hiz
        self.renk = renk

    def hareket_et(self, yon):
        self.x += yon * self.hiz
#THREAD SINIFI
class ArabaThread(threading.Thread):
    def __init__(self, araba, yon):
        threading.Thread.__init__(self)
        self.araba = araba
        self.yon = yon

    def run(self):
        while True:
            self.araba.hareket_et(self.yon)
            time.sleep(10)
#ARABAYI OLUŞTUR
araba1 = Araba(x=width // 4 - araba_width // 2, y=height - araba_height - 230, hiz=10, renk=araba1_rengi)
araba2 = Araba(x=3 * width // 4 - araba_width // 2, y=170, hiz=10, renk=araba2_rengi)

#ANA PYGAME DÖNGÜSÜ
saat = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Araba thread'lerini oluştur
    thread1 = ArabaThread(araba1, 1)  # Sağa doğru
    thread2 = ArabaThread(araba2, -1)  # Sola doğru

    # Thread'leri başlat
    thread1.start()
    thread2.start()
       
    #ARABAYI HAREKET ETTİR
    #araba1.hareket_et(1)  #Sağ
    #araba2.hareket_et(-1)  #Sol

    #ARABAYI SONSUZ DÖDÜRME
    if araba1.x > width:
        araba1.x = -araba_width

    if araba2.x < -araba_width:
        araba2.x = width

    #ARKA PLAN
    ekran.fill((255, 255, 255))
#FOTOĞRAF KONUM BE BOYUTU
    photo_x, photo_y = 0, 10
    photo_width, photo_height = 800, 500

    #FOTOĞRAFI YÜKLEME
    photo_path = "yolresim06.png" 
    photo_img = pygame.image.load(photo_path)
    photo_img = pygame.transform.scale(photo_img, (photo_width, photo_height))


    #FOTOĞRAFI EKRANA ÇİZME
    screen.blit(photo_img, (photo_x, photo_y))

    #ARABALARI ÇİZME
    pygame.draw.rect(ekran, araba1.renk, (araba1.x, araba1.y, araba_width, araba_height))
    pygame.draw.rect(ekran, araba2.renk, (araba2.x, araba2.y, araba_width, araba_height))

    #EKRANI GÜNCELLEME
    pygame.display.flip()
    # FPS SINIRLAMA
    saat.tick(30)