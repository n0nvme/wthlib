import requests


class wthlib:

    def __init__(self, key: str):
        self.session = requests.Session()
        self.session.params['APPID'] = key

        self.answer = None
        self.pressure = None
        self.temp = None
        self.wind = None


    def get_data(self, **kwargs):
        self.answer = self.session.get('https://api.openweathermap.org/data/2.5/weather', params={**kwargs}).json()
        self.pressure = self.answer['main']['pressure']
        self.temp = self.answer['main']['temp']
        self.wind = self.answer['wind']

    def get_pressure(self):
        return self.pressure

    def get_temp(self):
        return self.temp

    def get_wind(self):
        return self.wind
