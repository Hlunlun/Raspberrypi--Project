# 自動生成以及判讀視力檢測結果

## 組員
[Hlunlun](https://github.com/Hlunlun), [kuanyu0712](https://github.com/kuanyu0712)

## 動機
1. 視力測量過去均為人工檢測，造成醫護人力資源損耗。
2. 視力測量為一種有規律的行為，適合自動化。
3. 希望透過樹莓派自動生成及判讀視力檢測的結果

## Introduction 視力檢測功能: **隨機生成Ｃ字缺口、自動判斷檢測結果**
由樹莓派控制直流步進馬達，藉由旋轉隨機生成Ｃ字缺口，再透過語音辨識判斷使用者是否觀測正確，最後顯示結果在OLED。
1. Ultrasonic：啟動裝置
2. 直流步進馬達 : 隨機產生Ｃ字缺口
3. hatbot：語音判斷使用者是否回答正確。
4. OLED：顯示結果。

## 裝置
<img src="https://github.com/Hlunlun/Raspberrypi-Project/assets/92961617/4c723786-e455-4e37-9d9e-6aedfebb225c" alt="drawing" width="400"/>

## 實作步驟與對話設計
1. 啟動: 超音波偵測30-100 cm內距離啟動, 語音說出使用說明
2. 視力測量C字: 直流步進馬達控制缺口方向, 產生四個不同方向缺口
3. 語音辨識: 受測者說出缺口方向, 轉換成文字後, 判斷是否與正確答案相同
4. 顯示答案: 顯示正確答案顯示在OLED, 與測量的準確率

## 操作
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
