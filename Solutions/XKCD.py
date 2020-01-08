import requests
import re
import io
from PIL import Image
import matplotlib.pyplot as plt


def get_xkcd(i):
    r = requests.get(f"https://xkcd.com/{i}")  # load html page
    regex = r'<div id="comic">[ \n]+<img src="(.*jpg)"'  # regex to scrape the image url
    img_url = re.findall(regex, r.text)[0]  # get first regex match
    r = requests.get(f"https:{img_url}")  # load image
    img = Image.open(io.BytesIO(r.content))  # create PIL.Image from byte string
    return img


if __name__ == '__main__':
    for i in range(1, 10):
        img = get_xkcd(i)  # get image
        plt.imshow(img)  # show image
        plt.show()
