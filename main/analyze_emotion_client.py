import requests
import chinese_tts

def askForService(query:str, token:str) -> dict:
    '''
    Do sentiment analysis
    '''
    response = requests.post("http://140.116.245.157:9526", data={"inputtext":query, "token":token})
    if response.status_code == 200:
        return {"status":True, "result": response.text.strip()}
    else:
        return {"status":False, "result": None}
    



if __name__ == "__main__":
    query = ""
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJ2ZXIiOjAuMSwiaWF0IjoxNjY0ODUyMDQ0LCJ1c2VyX2lkIjoiNDIxIiwiaWQiOjU1NCwic2NvcGVzIjoiMCIsInN1YiI6IiIsImlzcyI6IkpXVCIsInNlcnZpY2VfaWQiOiIzMCIsImF1ZCI6IndtbWtzLmNzaWUuZWR1LnR3IiwibmJmIjoxNjY0ODUyMDQ0LCJleHAiOjE4MjI1MzIwNDR9.JbdxxAWpJh35Pre6clVBNwBoDokykoE4XMZbj8716tOb9trHvByQrkWIYaWM3E4PlyPRcdeOPJRj5Iia9uEfqeP94_Zj-gk3pAPL-Yv1HL1nx8dQxrUHB4MZMNoZ60E3d7rF58fg8LrLb1DFP2S0RUTTRmuYbjgGGxghexybpGw"
    r = askForService(query, token)
    chinese_tts('你的心情現在是' + r)
    print(r)
