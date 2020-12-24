# khdownloader
Contains only one file "main.py" that uses the modules os, reqeusts and selenium.

Main idea is:
* The audio player when gets activated contains the source file in mp3 format.
* I use selenium to simulate web browser as the source code from bs4 is bs.
* Using selenium I get all the elements on the page that are of the the class: "arrow-play". These are the buttons that I want to click in order to play the desired song on the audio player.
* By looping over n number of times where n is the number of elements in of class: "arrow-play". I click on each of the element in the list and get the source file url from the audio player.
* Using requests module I download the files to the disk.

Changes made on 13/12/2020
* Added support for FLAC file type for lossless audio.
* Changed the naming system. Songs now include the track name along with the number.
* Muted the audio player on the website.

Changes made on 25/12/2020
* Added support for chrome browser
* Fixed the error where a program exits out if no FLAC is available
* Files now overwrite when using the same URL twice.
* Browsers are now hidden.
