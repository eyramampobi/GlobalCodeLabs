import pyowm
from pprint import pprint
import requests

request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=1e2c5b9103431398f3e092ae93b6a865')
pprint(request.json())
print(request)
print("=======================================================================")
owm = pyowm.OWM('1e2c5b9103431398f3e092ae93b6a865')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Accra,GH')
w = observation.weather
pprint(w.wind().json())
print(w.humidity)
pprint(w.json())