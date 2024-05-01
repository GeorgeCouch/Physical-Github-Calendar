import board
import neopixel
import requests

response = requests.get('https://gh-calendar.rschristian.dev/user/GeorgeCouch')
json = response.json()
contributions = json["contributions"]

pixels = neopixel.NeoPixel(board.D18, 106, brightness=1)

pixel_arr = []
for i in range(len(contributions)):
    for j in range(len(contributions[i])):
        intensity = int(contributions[i][j]["intensity"])
        if (intensity == 0):
            pixel_arr.append((0, 0, 0))
        elif (intensity == 1):
            pixel_arr.append((0, 64, 0))
        elif (intensity == 2):
            pixel_arr.append((0, 0, 128))
        elif (intensity == 3):
            pixel_arr.append((192, 0, 0))
        else:
            pixel_arr.append((255, 255, 255))

for i in range(106):
    pixels[i] = pixel_arr[i]

print(len(pixel_arr))
print(len(contributions))