import board
import neopixel
import requests

response = requests.get('https://gh-calendar.rschristian.dev/user/GeorgeCouch')
json = response.json()
contributions = json["contributions"]

contributions_intensities_sorted = []
for i in range(7):
    for j in range(len(contributions)):
        try:
            contributions_intensities_sorted.append(int(contributions[j][i]["intensity"]))
        except:
            contributions_intensities_sorted.append(0)

pixels = neopixel.NeoPixel(board.D18, len(contributions_intensities_sorted), brightness=1)

pixel_arr = []
for i in range(len(contributions_intensities_sorted)):
    if (contributions_intensities_sorted[i] == 0):
        pixel_arr.append((0, 0, 0))
    elif (contributions_intensities_sorted[i] == 1):
        pixel_arr.append((0, 64, 0))
    elif (contributions_intensities_sorted[i] == 2):
        pixel_arr.append((0, 0, 128))
    elif (contributions_intensities_sorted[i] == 3):
        pixel_arr.append((192, 0, 0))
    else:
        pixel_arr.append((255, 255, 255))

for i in range(len(contributions_intensities_sorted)):
    pixels[i] = pixel_arr[i]