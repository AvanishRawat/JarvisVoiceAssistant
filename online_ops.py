import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address

def search_on_wiki(query):
    results = wikipedia.summary(query,sentences = 2)
    return results

def play_on_YT(video):
    kit.playonyt(video)

def search_on_Google(query):
    kit.search(query)

email = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(receiver_address,subject,message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = email
        email.set_content(message)
        s = smtplib.SMTP('smtp.gmail.come',587)
        s.starttls
        s.login(email,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

OPENWEATHER_APP_ID = config('OPENWEATHER_APP_ID')
def get_weather_reports(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res['weather'][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res['main']["feels_like"]
    return weather,f"{temperature}℃",f"{feels_like}℃"

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res['joke']

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
