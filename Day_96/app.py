from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if city:
        # Construct the API URL
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        
        # Fetch weather data from OpenWeatherMap API
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] == "404":
            return render_template('index.html', message="City Not Found!")
        
        # Parse the data to get the relevant information
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        # Return the weather information to the webpage
        return render_template('index.html', city=city, temp=temp, pressure=pressure, 
                               humidity=humidity, description=description)
    return render_template('index.html', message="Please enter a city!")

if __name__ == "__main__":
    app.run(debug=True)
