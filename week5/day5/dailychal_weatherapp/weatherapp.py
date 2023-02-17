# e17646015c22bc307b3eea27f9366f27


from pyowm.owm import OWM

# api call from api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=08876b8ab00fa4d62c8b990f75994601


def get_weather(city):
    owm = OWM("08876b8ab00fa4d62c8b990f75994601")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return w


print(f'{get_weather("London")}')
