import record
import chinese_tts
import chinese_stt
import taiwanese_tts 


ans = 1
while(ans != 0):
    print('請輸入(1)台語回復(2)中文回復(0)結束樹梅派程式')
    taiwanese_tts.main("請選擇你 要 台語 回覆 或是 國語 回覆")
    chinese_tts.play("請輸入(1)台語回覆(2)中文回覆(0)結束樹梅派程式")
    ans = eval(input())
    if ans == 1:
        record.main()
        answer_sentense =chinese_stt.answer()
        taiwanese_tts.main(answer_sentense) #確認要唸出來的台語句子
    elif ans == 2:
        record.main()
        answer_sentense =chinese_stt.answer()
        chinese_tts.play(answer_sentense) #確認要唸出來的台:語句子
    elif ans == 0:
        chinese_tts.play("你選擇結束樹梅派程式,那掰掰囉")
        break        
    else:
        chinese_tts.play('你的選擇不在範圍內,請重新選擇')
    chinese_tts.play('回答結束，你可以繼續問問題')
