# lessgobiches

import requests, time, os
from selenium import webdriver

browser = webdriver.Firefox()
url = "https://downloads.khinsider.com/game-soundtracks/album/ghost-of-tsushima-music-from-the-video-game"
browser.get(url)

time.sleep(10)

source = browser.page_source
filename = browser.find_elements_by_tag_name("h2")[0].text
os.mkdir(f"D:\\Music\\VG\\{filename}")
buttons = browser.find_elements_by_class_name("arrow-play")

for i in buttons:
    i.click()
    src = browser.find_element_by_id("audio1").get_attribute("src")
    song = requests.get(src)
    try:
        song.raise_for_status()
        if filename:
            file = open(f"D:\\Music\\VG\\{filename}\\{buttons.index(i) + 1}.mp3", "wb")
            for chunk in song.iter_content(100000):
                file.write(chunk)
            print(f"{buttons.index(i) + 1} downloaded.")
            file.close()
        else:
            print("file name blank")

    except Exception as e:
        print(f"error downloading {buttons.index(i) + 1}")
