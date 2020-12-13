# lessgobiches

import requests, time, os
from selenium import webdriver
import re

browser = webdriver.Firefox()
browser.maximize_window()


# replace this url with the url of the album you want to download.
url = "https://downloads.khinsider.com/game-soundtracks/album/persona-5-royal"


flac_check = re.findall('FLAC', requests.get(url).text)
browser.get(url)

time.sleep(3)

source = browser.page_source    # only GOD knows why this exits. I am too afraid to delete it.
filename = browser.find_elements_by_tag_name("h2")[0].text      # folder name
browser.find_element_by_xpath("//div[@class='audioplayerVolume']").click()      # mute
os.mkdir(f"D:\\Music\\VG\\{filename}")
buttons = browser.find_elements_by_class_name("arrow-play")     # button to play song
xpath_result = browser.find_elements_by_xpath('//td[@class="clickable-row"]//a')    # track name
track_name = []
flac_or_not = 'n'
if flac_check:
    print('FLAC type is available for this album.\n(F)lac or (M)p3:\n')
    flac_or_not = input('->').lower()
    for i in range(0, len(xpath_result), 4):
        track_name.append(xpath_result[i].text)
else:
    print('FLAC filetype is not available for this album.\n Downloading mp3 format.')
    for i in range(0, len(xpath_result), 3):
        track_name.append(xpath_result[i].text)

# download mp3
if flac_or_not == 'm':
    for i in buttons:
        i.click()
        src = browser.find_element_by_id("audio1").get_attribute("src")
        song = requests.get(src)
        try:
            song.raise_for_status()
            if filename:
                file = open(f"D:\\Music\\VG\\{filename}\\{buttons.index(i) + 1}-{track_name[buttons.index(i)]}.mp3", "wb")
                for chunk in song.iter_content(100000):
                    file.write(chunk)
                print(f"{buttons.index(i) + 1} downloaded. MP3 Format.")
                file.close()
            else:
                print("file name blank")

        except Exception as e:
            print(f"error downloading {buttons.index(i) + 1} : {e}")

# download flac
elif flac_or_not == 'f':
    for i in buttons:
        i.click()
        src = browser.find_element_by_id("audio1").get_attribute("src")
        src = re.sub('mp3$', "flac", src)
        song = requests.get(src)
        try:
            song.raise_for_status()
            if filename:
                file = open(f"D:\\Music\\VG\\{filename}\\{buttons.index(i) + 1}-{track_name[buttons.index(i)]}.flac",
                            "wb")
                for chunk in song.iter_content(100000):
                    file.write(chunk)
                print(f"{buttons.index(i) + 1} downloaded. FLAC format.")
                file.close()
            else:
                print("file name blank")

        except Exception as e:
            print(f"error downloading {buttons.index(i) + 1} : {e}")

else:
    print("Please choose from one of the options.")
time.sleep(2)
browser.close()

