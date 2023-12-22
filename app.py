import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weatherData.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'conyWeather'
database = SQLAlchemy(app)


class City(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)


def validate_City(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=8ad2342bc9de1e81734e896a48a13c93'
    response = requests.get(url).json()
    return response


@app.route('/')
def index_get():
    cities = City.query.all()
    weather_data_cities = []
    weather_data_cities_first_half = []
    weather_data_cities_second_half = []

    for city in cities:
        response = validate_City(city.name)
        print(response)
        weather_data = {
            'City': city.name,
            'Temperature': response['main']['temp'],
            'Description': response['weather'][0]['description'],
            'Icon': response['weather'][0]['icon'],
            'Temperature_Max': response['main']['temp_max'],
            'Temperature_Min': response['main']['temp_min'],
            'Humidity': response['main']['humidity'],
            'Pressure': response['main']['pressure'],
            'Wind': response['wind']['speed']
        }
        weather_data_cities.append(weather_data)
        weather_data_cities_first_half = weather_data_cities[len(weather_data_cities) // 2:]
        weather_data_cities_second_half = weather_data_cities[:len(weather_data_cities) // 2]

    return render_template('weather.html', weather_data_cities_first_half=weather_data_cities_first_half,
                           weather_data_cities_second_half=weather_data_cities_second_half)


@app.route('/', methods=['POST'])
def index_post():
    new_city = request.form.get('city')
    warning = []
    # print(new_city)
    if new_city:
        existed_city = City.query.filter_by(name=new_city).first()
        if not existed_city:
            validation = validate_City(new_city)
            if validation['cod'] == 200:
                new_city_obj = City(name=new_city)

                database.session.add(new_city_obj)
                database.session.commit()
            else:
                warning = new_city + ' does NOT exist in the world!'
                print(warning)
        else:
            warning = new_city + ' already EXISTS in your data!'
            print(warning)
    if warning:
        flash(warning, 'warning')
    else:
        flash(new_city + ' added successfully!')

    return redirect(url_for('index_get'))


@app.route('/delete/<name>')
def delete_city(name):
    city = City.query.filter_by(name=name).first()
    database.session.delete(city)
    database.session.commit()

    flash(f'{city.name} is deleted successfully!', 'info')
    return redirect(url_for('index_get'))

if __name__== "__main__":
    app.run()
