from flask import Flask, render_template, request, jsonify  # Correct imports
import requests

app = Flask(__name__)

# API Key and Base URL for OpenWeatherMap
api_key = '03643eac79b12d9d9d4d893f1df73405'
baseURL = 'http://api.openweathermap.org/data/2.5/weather'

# API route to fetch weather data - check notes
@app.route('/api/weather', methods=['GET'])
def getWeather():
    # the function runs whenever someone accesses that route in browser
    city = request.args.get('city')  
    # The city we search gets appended(?) to the url and we set that value to 'city'
    
    if not city:
        # if you haven't entered a city. I wasn't familiar with this syntax
        return jsonify({'error': 'City is required'}), 400

    # Important stuff
    # Taking city and appid(connected by and like a poorly structured sentence), we construct this url and send it to openweather
    weatherurl = f"{baseURL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(weatherurl) # send this to the server..?
    
    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

@app.route('/')
def index():
    # Probably the only useful thing I learnt in that tutorial
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
