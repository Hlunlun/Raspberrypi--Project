# 自動生成以及判讀視力檢測結果

## 裝置
<img src="https://github.com/Hlunlun/Raspberrypi-Project/assets/92961617/4c723786-e455-4e37-9d9e-6aedfebb225c" alt="drawing" width="400"/>

## 步驟
1. Ultrasonic啟動:\
   ➙ 超音波偵測30-100 cm內距離啟動，語音說出: "你好，現在要進行視力檢查嗎?"\
   ➙ Chatbot接收使用者語音回覆:
      - 使用者回答「要」， 則會開始說明使用方法:\
        步進馬達的C字缺口會顯示不同方向的C，回答C字缺口的方向，總共會檢測5次，最後判斷你的視力回答準確率，顯示在OLED螢幕上
      - 使用者回答「不要」:	 "好的，那掰掰，打擾了!"
2. 產生視力測量C字 & 語音辨識:\
   ➙ 步進馬達開始旋轉後，會由Chatbot語音提示: "請回答C字缺口的方向"\
   ➙ Chatbot自動記錄使用者語音回覆的答案\
   <img src="https://github.com/Hlunlun/Raspberrypi-Project/assets/92961617/b8aa2e76-2f9a-4c5b-b948-7152a0b58cbf" alt="drawing" width="800"/>\
3. OLED顯示答案:\
   ➙ 使用者回答Ｃ字缺口方向後，會由OLED顯示正確或是錯誤\
   ➙ 進行5次後會計算出準確率\
   ➙ 結束語音說出:Thank you bye bye\
   <img src="https://github.com/Hlunlun/Raspberrypi-Project/assets/92961617/09352d8d-420b-4107-acb3-1291fcd81c44" alt="drawing" width="800"/>\

## Demo 
[link](https://drive.google.com/file/d/1k_Bw0O-vlbsRKo22TdIk8HiPuiUqi3yV/view)
