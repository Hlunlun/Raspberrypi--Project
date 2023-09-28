
import text_oled
import chinese_tts
import record
import chinese_stt

#Libraries
import RPi.GPIO as GPIO
import time

#import text_oled
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    start_time = time.time()
    stop_time = time.time()
 
    # save start_time
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
 
    # time difference between start and arrival
    time_elapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2
 
    return distance

def explain():
    with Board() as board:        
        print('Press button to skip explaination')
        board.button.wait_for_press()
        done = threading.Event()
        board.button.when_pressed = done.set
		
        if done.set:
            return
        else :
            chinese_tts('OLED螢幕上顯示不同缺口的C，回答C字缺口的方向，總共會檢測5次，最後判斷你的視力是否超過0.9，定顯示在OLED螢幕上')

def check_vision():
    # TODO : mortor
    chinese_tts('')
    answer = chinese_stt.answer()
    


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            if(dist>=30 and dist<=100):
                print ("Measured Distance = %.1f cm" % dist)
                chinese_tts.play('你好，請問你要進行視力檢查嗎?')                
                record.main()
                if(chinese_stt().chinese_recognize('recording.wav')):
                    reponse = chinese_stt().chinese_recognize('recording.wav')
                    if ('不用'in reponse or '不要'in response or 'No'in reponse):
                        chinese_tts().play('好的，那掰掰，打擾了!')
                        # TODO : sleep
                    else:           
                        chinese_tts.play('好的，現在向你說明如何檢測，如果想跳過可直接按下按鈕')
                        explain()
                        check_vision()
                    
                        
                           
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
