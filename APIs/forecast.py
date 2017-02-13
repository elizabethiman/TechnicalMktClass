import forecastio

api_key = "cfd6da32e48ad96286aa551f08b17c1f"

lat = 38.89768
lng = -77.03653
forecast = forecastio.load_forecast(api_key, lat, lng)

byHour = forecast.hourly()
current = forecast.currently()

print (current.temperature, byHour.summary)
