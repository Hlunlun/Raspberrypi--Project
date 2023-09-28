from gtts import gTTS
import socket
import urllib
import os


def ch_tts(text, file_):
    tts = gTTS(text, lang = 'zh-tw')
    tts.save(file_ + '.wav')
    os.system(file_ + '.wav')

def play(text):
     while True:
            tts = gTTS(text=text, lang='zh-tw')
            tts.save("test.mp3")
            os.system("mpg123 test.mp3")
            break

if __name__ == "__main__":
    
    while True:
        try:
            urllib.request.urlopen("http://www.google.com")
        except urllib.error.URLError:
            print("Fail to connect Internet...")
            os.system("")
            time.sleep(1)
        else:
            print("Connected")
            # change here
            tts = gTTS(text='你好，我是google大姐', lang='zh-tw')
            tts.save("test.mp3")
            os.system("mpg123 test.mp3")
            break
