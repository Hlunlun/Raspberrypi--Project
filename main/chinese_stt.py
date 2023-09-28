import speech_recognition as sr
import question
import analyze_emotion_client

def chinese_recognize(wav_file):
    
    r = sr.Recognizer()
    with sr.WavFile(wav_file) as source:
        audio = r.record(source)

    try:
        result = r.recognize_google(audio, language='zh-tw')
        return result
    except LookupError:
        print("Could not understand audio:" , wav_file)
        return None

def answer():
    q = chinese_recognize('recording.wav')
        
    # TODO : answer 
    anwer = '上'
    # check response
    if answer in q:
        # OLED output answer
        text_oled.display_text('CORRECT!')
    else:
        # OLED output answer
        text_oled.display_text('WRONG!')


if __name__ == "__main__":

    print(chinese_recognize("recording.wav"))

    


