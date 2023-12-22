# Weather Forecast APP

### Intro
This is a weather forecast web app. 

User can freely add as many as cities he wants to see 
Detailed information of each city will be displayed.

#### * Information includes:
    - City Name
    - A weather logo
    - Current Temperature
    - Description
    - Max Temperature
    - Min Temperature
    - Humidity
    - Pressure
    - WindSpeed

#### * Remind info: (error handling)
(1) If user add a city successfully, a green info block appears: <CityName> added successfully!
(2) If user add a duplicated city, a red info block appears: <CityName> already exists in your data!
(3) If user add a city doesn't exist, a red info block appears: <CityName> doesn't exist in the world!
(4) If user choose to delete a city, a blue info block appears: <CityName> is deleted successfully!

### Mechanism
Flask
Sqlite Database
OpenAPI: [OpenWeatherAPI](https://stackoverflow.com/questions/7653483/github-relative-link-in-markdown-file)

### Set up
```console
foo@bar:~$ pip install flask
```
```console
foo@bar:~$ pipenv install python-dotenv
```

### Demo
[![Watch the video](assets/main.png)](https://youtu.be/blSzzns6-2c)
