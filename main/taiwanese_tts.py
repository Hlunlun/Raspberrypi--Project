# !/usr/bin/env python
# _*_coding:utf-8_*_

# 給任何使用這支程式的人：這支程式是新版台語台羅語音合成的API的client端。具體上會發送最下方變數data的台羅
# 給伺服器，並接收一個回傳的wav檔，output.wav
# 接受之台羅為教育部羅馬拼音，非教會羅馬拼音，請注意。
# 接受格式為UTF-8台羅，不是帶數字的。即請用類似"phái-sè"而非"phai2-se3"這種
# 不同port可以有不同格式，詳見下面的[注意]

# 客戶端 ，用來呼叫service_Server.py
import socket
import sys
import struct
# Don't touch
from aiy.voice.audio import play_wav
def askForService(token, data, model="M12_5"):
    # HOST, PORT 記得修改
    global HOST
    global PORT
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    received = ""
    try:
        sock.connect((HOST, PORT))
        msg = bytes(token+"@@@"+data+"@@@"+model, "utf-8")
        msg = struct.pack(">I", len(msg)) + msg
        sock.sendall(msg)

        with open('output.wav', 'wb') as f:
            while True:
                # print("True, wait for 15sec")
                # time.sleep(15)

                l = sock.recv(8192)
                # print('Received')
                if not l:
                    break
                f.write(l)
        # print("File received complete")
    finally:
        sock.close()
    return "OK"
# Don't touch


def process(token, data):
    # 可在此做預處理

    # 送出
    result = askForService(token, data)
    # 可在此做後處理
    return result


def main(data):
    global HOST
    global PORT
    # 注意：以下數字，10008為原版，10010套用實驗室變調版，10012則是接受中文輸入，即多套一個中文轉台羅
    # ***10008以及10010接受台羅，10012接受中文
    HOST, PORT = "140.116.245.146", 10012
    token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3OTEyOTMxMzMsImlhdCI6MTYzMzYxMzEzMywic3ViIjoiIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJpc3MiOiJKV1QiLCJ1c2VyX2lkIjoiMjkwIiwibmJmIjoxNjMzNjEzMTMzLCJ2ZXIiOjAuMSwic2VydmljZV9pZCI6IjI0IiwiaWQiOjM5Niwic2NvcGVzIjoiMCJ9.XtqCCNnmc6tiNIOvcCsY6_vX-IjQFreYQWeU3BqXAvhZYCnjRUZvkcQcRLo-FjUikviipwRRYZhBGXK2Pd2xK8gfNu7LKRGh9V3sPvHIHn4MxC-YzV0tjQItGyIDW2w708YJQffx3v4A7wxnj3sjkxDxHIS8LApRcgk7Cd3Rdig"
   
    
   # data = "I kú-kú tsiah lâi tsi̍t pái"
    # data = "lîm--sian--sinn ê tsa-bóo-kiánn、 tíng-kò-gue̍h tsò--lâng āu--ji̍t 、tio̍h beh kè--lâng"
    
    #print("local ans = ", data) 確認要唸的答案有進來
    for i in range(1):
        if process(token, data) == "OK":
            play_wav('output.wav')
