# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import requests
import math

class WeatherAPI:

    __slots__ = ('session', 'raw')

    def __init__(self, key: str):
        self.session = requests.Session()
        self.session.params['APPID'] = key
        self.raw = None

    def get_data(self, **kwargs) -> None:
        self.raw = self.session.get('http://api.openweathermap.org/data/2.5/weather',
                                    params={**kwargs}).json()

    @property
    def pressure(self) -> int:
        return self.raw.get('main', {}).get('pressure', 'error')

    @property
    def temperature(self) -> int:
        return self.raw.get('main', {}).get('temp', 'error')

    @property
    def wind(self) -> int:
        return self.raw.get('wind', 'error')




def dc(a, b):
    return math.cos(a) * b, math.tan(a) * b

def get_history(lat, lon):
    loc = str(lat) + ',' + str(lon)
    parms = {'key': '69f8dd57c5354d22b3f150100181205', 'format': 'json', 'q': loc, 'date': '2018-04-01',
             'enddate': '2018-04-30'}
    history = requests.get('https://api.worldweatheronline.com/premium/v1/past-weather.ashx', params=parms).json()
    weather = history['data']['weather']
    wind = []

    for k in weather:
        for i in k['hourly']:
            tmp = dc(*[int(i['windspeedKmph']), int(i['winddirDegree'])])
            wind.append(tmp)
