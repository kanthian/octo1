import board, smbus, busio, adafruit_mpr121, pygame
from adafruit_extended_bus import ExtendedI2C as I2C

path = "/home/pi/audionumbers/"
#path = "/home/pi/testnumbers/"

print("Starting octopusbus.py with sounds path=" + path)

sounds = ["1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav", "10.wav", "11.wav", "12.wav",
        "13.wav", "14.wav", "15.wav", "16.wav", "17.wav", "18.wav", "19.wav", "20.wav", "21.wav", "22.wav", "23.wav", "24.wav",
        "25.wav", "26.wav", "27.wav", "28.wav", "29.wav", "30.wav", "31.wav", "32.wav", "33.wav", "34.wav", "35.wav", "36.wav", "37.wav",
        "38.wav", "39.wav", "40.wav", "41.wav", "42.wav", "43.wav", "44.wav", "45.wav", "46.wav", "47.wav", "48.wav", "49.wav", "50.wav",
        "51.wav", "52.wav", "53.wav", "54.wav", "55.wav", "56.wav", "57.wav", "58.wav", "59.wav", "60.wav", "61.wav", "62.wav", "63.wav",
        "64.wav", "65.wav", "66.wav", "67.wav", "68.wav", "69.wav", "70.wav", "71.wav", "72.wav", "73.wav", "74.wav", "75.wav", "76.wav",
        "77.wav", "78.wav", "79.wav", "80.wav", "81.wav", "82.wav", "83.wav", "84.wav", "85.wav", "86.wav", "87.wav", "88.wav", "89.wav",
        "90.wav", "91.wav", "92.wav", "93.wav", "94.wav", "95.wav", "96.wav", "97.wav", "98.wav", "99.wav", "100.wav",
            "101.wav", "102.wav", "103.wav", "104.wav", "105.wav", "106.wav", "107.wav", "108.wav", "109.wav", "110.wav", "111.wav", "112.wav",
                "113.wav", "114.wav", "115.wav", "116.wav", "117.wav", "118.wav", "119.wav", "120.wav", "121.wav", "122.wav", "123.wav", "124.wav",
                "125.wav", "126.wav", "127.wav", "128.wav", "129.wav", "130.wav", "131.wav", "132.wav", "133.wav", "134.wav", "135.wav", "136.wav", "137.wav",
                "138.wav", "139.wav", "140.wav", "141.wav", "142.wav", "143.wav", "144.wav", "145.wav", "146.wav", "147.wav", "148.wav", "149.wav", "150.wav",
                "151.wav", "152.wav", "153.wav", "154.wav", "155.wav", "156.wav", "157.wav", "158.wav", "159.wav", "160.wav", "161.wav", "162.wav", "163.wav",
                "164.wav", "165.wav", "166.wav", "167.wav", "168.wav", "169.wav", "170.wav", "171.wav", "172.wav", "173.wav", "174.wav", "175.wav", "176.wav",
                "177.wav", "178.wav", "179.wav", "180.wav", "181.wav", "182.wav", "183.wav", "184.wav", "185.wav", "186.wav", "187.wav", "188.wav", "189.wav",
                "190.wav", "191.wav", "192.wav", "193.wav", "194.wav", "195.wav", "196.wav", "197.wav", "198.wav", "199.wav", "200.wav",
                    "201.wav", "202.wav", "203.wav", "204.wav", "205.wav"]

def playSound(soundIndex):
    print(sounds[soundIndex])
    pygame.mixer.music.load(path + sounds[soundIndex])
    pygame.mixer.music.play()
    # empty_channel = pygame.mixer.find_channel()
    # empty_channel.play(s)
    while pygame.mixer.music.get_busy() == True:
        continue

#each i2c object corresponds to a i2c clock data pair on the pi configured in boot/config.txt
#CONFIG.TXT IS IS CONFIGURED TO GIVE THE PI EXTRA I2C PINS (DEFAULT PINS ARE 2 AND 3)
i2c_array = [
    I2C(1),
    I2C(3),
    I2C(6),
    I2C(5),
    I2C(4),
]

START_I2C_ADDRESS = 0x5A
i2c_device_counts = [2, 4, 4, 4, 4]
mpr121_array = []


board_count = 0
for i, i2c in enumerate(i2c_array):
    for device_num in range(i2c_device_counts[i]):
        board_letter = chr(ord('A') + board_count)
        try:
            mpr121 = adafruit_mpr121.MPR121(i2c, address=(START_I2C_ADDRESS + device_num))
            mpr121._write_register_byte(adafruit_mpr121.MPR121_CONFIG1, 0x10|0xB0) # 16uA charge current, 34 sample avg
            mpr121_array.append(mpr121)
            print ("board " + board_letter + " connected")
        except:
            mpr121_array.append(None)
            print ("board " + board_letter + " not connected")
        board_count += 1

pygame.mixer.pre_init(buffer=2048)
pygame.mixer.init()
speaker_volume = 1.0
pygame.mixer.music.set_volume(speaker_volume)

while True:
    #first_board = [x for x in mpr121_array if x is not None][0]
    #print("0.0: {} / {}".format(first_board.filtered_data(0), first_board.baseline_data(0)))

    for i in range (12):
        for board_number, mpr121 in enumerate(mpr121_array):
            board_letter = chr(ord('A') + board_number)
            if mpr121 is None:
                pass
            try:
                if mpr121[11-i].value:
                    print('you touched sensor (' + board_letter + ' pad # {}!'.format (i+1))
                    playSound(i + board_number * 12)
            except:
                pass
