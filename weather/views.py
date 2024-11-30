import requests
from django.shortcuts import render

API_KEY = "d674d8bb8158f83efd3bff45d5b3852d" 

def home(request):
    city = request.GET.get('city', 'Kathmandu')  # Default city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if(response.status_code == 200):
        context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
        'error':None
    }
    else:
        context={
        'city':city,
        'error': weather_data.get('message','city not found')
    }
    return render(request, 'weather/home.html', context)
