from app_logger import app_logger_instance
from app_exception.exception import AppException
import pyowm
import sys

class WeatherData:
    def __init__(self):
        self.owmapikey = 'c8537154778558a3c9e30c03f18a1672'
        self.owm = pyowm.OWM(self.owmapikey)
        self.weather_manager = self.owm.weather_manager()

    def processRequest(self, req):
        try:
            self.result = req.get("queryResult")
            self.parameters = self.result.get("parameters")
            self.city = self.parameters.get("geo-city")
            print(self.city)

            # Uncomment this for logging
            # app_logger_instance.info(f"Fetching weather data for: {self.city}")

            self.observation = self.weather_manager.weather_at_place(str(self.city))
            # Uncomment this for logging
            # app_logger_instance.info(f"Observation for {self.city}: {self.observation}")

            # Call the weather object and wind attributes correctly
            w = self.observation.weather
            self.latlon_res = self.observation.location

            self.lat = str(self.latlon_res.lat)
            self.lon = str(self.latlon_res.lon)

            # Accessing wind data correctly
            self.wind_res = w.wind()  # Call the method to get wind data
            self.wind_speed = str(self.wind_res.get('speed'))
            self.humidity = str(w.humidity)

            self.celsius_result = w.temperature('celsius')
            self.temp_min_celsius = str(self.celsius_result.get('temp_min'))
            self.temp_max_celsius = str(self.celsius_result.get('temp_max'))

            speech = f"Today's weather in {self.city}: Humidity: {self.humidity}, Wind Speed: {self.wind_speed}, Minimum Temperature: {self.temp_min_celsius}, Maximum Temperature: {self.temp_max_celsius}"
            return {
                "fulfillmentText": speech,
                "displayText": speech
            }
        except Exception as e:
            # Uncomment this for logging
            # app_logger_instance.error(f"Error occurred: {e}")
            raise AppException(e, sys) from e  

