import board, busio, adafruit_mpr121, pygame

path = "/home/pi/sounds/"
i2c = busio.I2C(board.SCL, board.SDA)
# i2c = board.I2C()
# touch_pad = adafruit_mpr121.MPR121(i2c)
mpr121_A = adafruit_mpr121.MPR121(i2c, address=0x5A)
mpr121_B = adafruit_mpr121.MPR121(i2c, address=0x5B)
mpr121_C = adafruit_mpr121.MPR121(i2c, address=0x5C)
mpr121_D = adafruit_mpr121.MPR121(i2c, address=0x5D)

sounds = ["Tentacle1.wav",
          "Tentacle2.wav"]

pygame.mixer.pre_init(buffer=2048)
pygame.mixer.init()
speaker_volume = 0.5
pygame.mixer.music.set_volume(speaker_volume)


while True:
        for i in range (12):
            if mpr121_A[i].value:
                s = pygame.mixer.Sound(path+sounds[i])
                print('you touched sensor 1 pad # {}!'.format (i))
                pygame.mixer.music.load(path + sounds[i])
                pygame.mixer.music.play()
                # empty_channel = pygame.mixer.find_channel()
                # empty_channel.play(s)
                while pygame.mixer.music.get_busy() == True:
                    continue
            if mpr121_B[i].value:
                s = pygame.mixer.Sound(path+sounds[i])
                print('you touched a sensor 2 pad # {}!'.format (i))
                pygame.mixer.music.load(path + sounds[i])
                pygame.mixer.music.play()
                # empty_channel = pygame.mixer.find_channel()
                # empty_channel.play(s)
                while pygame.mixer.music.get_busy() == True:
                    continue
            if mpr121_C[i].value:
                s = pygame.mixer.Sound(path+sounds[i])
                print('you touched sensor 3 pad # {}!'.format (i))
                pygame.mixer.music.load(path + sounds[i])
                pygame.mixer.music.play()
                # empty_channel = pygame.mixer.find_channel()
                # empty_channel.play(s)
                while pygame.mixer.music.get_busy() == True:
                    continue
            if mpr121_D[i].value:
                s = pygame.mixer.Sound(path+sounds[i])
                print('you touched a sensor 4 pad # {}!'.format (i))
                pygame.mixer.music.load(path + sounds[i])
                pygame.mixer.music.play()
                # empty_channel = pygame.mixer.find_channel()
                # empty_channel.play(s)
                while pygame.mixer.music.get_busy() == True:
                    continue
