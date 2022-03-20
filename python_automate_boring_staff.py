# programs
# chapter 2 guess the number
import random

true = random.randint(1, 20)
for i in range(5):
    guess1 = int(input('take a guess '))
    if guess1 == true:
        print('right')
        break
    elif guess1 > true:
        print('high')
    else:
        print('low')
if guess1 == true:
    print('well done')
else:
    print('stupid')

# chapter 3: a short program: zigzag
import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent + '********')
        time.sleep(0.5)
        if indentIncreasing:
            indent += 1
        else:
            indent -= 1
        if indent == 20:
            indentIncreasing = False
        if indent == 0:
            indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

# chapter 12: Downloading all XKCD Comics
"""
Here’s what your program does:

Loads the XKCD home page
Saves the comic image on that page
Follows the Previous Comic link
Repeats until it reaches the first comic
This means your code will need to do the following:

Download pages with the requests module.
Find the URL of the comic image for a page using Beautiful Soup.
Download and save the comic image to the hard drive with iter_content().
Find the URL of the Previous Comic link, and repeat.
Open a new file editor tab and save it as downloadXkcd.py.
"""
## Step 1: Design the Program
#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
    # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),
                     'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')