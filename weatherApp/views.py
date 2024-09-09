from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                        +city
                                        +'&units=metric&appid=9811b81e0179143cf9ad41848e52ed01')
        list_of_data = json.load(source)
        data = {
            'temp':(list_of_data['main']['temp']),
            'pressure' : str(list_of_data['main']['pressure']),
            'humidity' : str(list_of_data['main']['humidity']),
            'description' : str(list_of_data['weather'][0]['main']),
            'icon' : list_of_data['weather'][0]['icon'],
            'city':city,
            'country_code':str(list_of_data['sys']['country']),
        }
        print(data)
    else:
        data={}
    return render(request,'main/index.html',data)