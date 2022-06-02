# DSC510 T301
# Week 12 Weather Program
# Programming Assignment Final Project
# Moshe Burnstein
# 4/27/2022
# Access Current Weather by City or Zipcode
# Use City, Zipcode to Get Coordinates to Pass Through OpenWeatherMap API


import requests


# Change #1
# Learned how to pass variables through functions
# Allows me to omit dreaded global variables
# Date of change: May 30, 2022
# Author Moshe Burnstein


# Prompt user to choose degrees representation and assign to variable
def prompt_degrees_type():
    while True:
        print("How would you like to view degrees?")
        choose_temp = input('Please enter "C" for Celsius, "F" for Fahrenheit, and "K" for Kelvin: ')
        if choose_temp.upper() == "C":
            degrees_temp = "metric"
        elif choose_temp.upper() == "F":
            degrees_temp = "imperial"
        elif choose_temp.upper() == "K":
            degrees_temp = "standard"
        else:
            print("You have not entered a valid entry.")
            continue
        return degrees_temp


# Access coordinates for city
def find_by_city():
    locale = input("Please enter the city name: ")
    state_abbreviation = input("Please enter your state by abbreviation: ")
    url = 'https://api.openweathermap.org/geo/1.0/direct?q={},{},US&limit=2&appid=fab5265f59e2fe91da54d4dfef6df75a'.format(
        locale, state_abbreviation)
    try:
        response = requests.get(url)
    except requests.ConnectionError as e:
        print(e)

    except requests.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        weather_facts = response.json()
    try:
        latitude = (weather_facts[0]['lat'])
    except Exception as e:
        print(e)
    else:
        longitude = (weather_facts[0]['lon'])
    return latitude, longitude, locale



# Access coordinates for zipcode
def find_by_zipcode():
    locale = input("Please enter your 5 digit zipcode:")
    url = 'http://api.openweathermap.org/geo/1.0/zip?zip={},US&appid=5c59712d5d2f4678bde5bb17947f8421'.format(locale)
    try:
        response = requests.get(url)
    except requests.ConnectionError as e:
        print(e)
    except requests.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        data = response.json()
    try:
        latitude = data['lat']
    except Exception as e:
        print(e)

    longitude = data['lon']

    return latitude, longitude, locale


# Pass through parameters to make lookup in API
def get_weather_info(latitude, longitude, locale, degrees_temp):
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=5c59712d5d2f4678bde5bb17947f8421&units={}'.format(
        latitude, longitude, degrees_temp)
    try:
        response = requests.get(url)
    except requests.ConnectionError as e:
        print(e)
    except requests.HTTPError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        current_weather = response.json()

    print("        Current weather conditions for", locale.capitalize(), ":")
    print("        ----------------------------------------")
    print("The temperature is ", current_weather['main']['temp'], "degrees.")
    print("The high is ", current_weather['main']['temp_max'], "degrees.")
    print("The low is ", current_weather['main']['temp_min'], "degrees.")
    print("It feels like ", current_weather['main']['feels_like'], "degrees.")
    print("The humidity is ", current_weather['main']['humidity'], "percent.")
    print("The barometric pressure is ", current_weather['main']['pressure'], "hPa")
    print("The current wind speed is ", current_weather['wind']['speed'], "m/s.")
    print("The visibility is ", current_weather['visibility'], "meters.")
    # Must index for list after first dictionary
    print("Current weather conditions: ", current_weather['weather'][0]['description'])


def main():
    print("Welcome to my weather program. It would be my pleasure to provide you with weather facts.")

    while True:
        try:
            choose_locale = int(
                input('Please enter "1" to search by U.S. city, "2" to search by zipcode, and "3" to finish:'))
        except ValueError as e:
            print("You did not enter a valid number,", e)
            continue
        if choose_locale == 1:
            print("You have chosen to search by city.")

            latitude, longitude, locale = find_by_city()
            # Change #2
            # May 31,2022
            # Originally prompted for degrees metric once for program
            # Assumed user would want only one standard
            # Professor wants option for each rerun...maybe user wishes to compare
            # Author Moshe Burnstein
            degrees_temp = prompt_degrees_type()
            get_weather_info(latitude, longitude, locale, degrees_temp)
        if choose_locale == 2:
            print("You have chosen to search by zipcode.")

            latitude, longitude, locale = find_by_zipcode()
            degrees_temp = prompt_degrees_type()
            get_weather_info(latitude, longitude, locale, degrees_temp)

        if choose_locale == 3:
            print("Thank you for using my program.")
            break


if __name__ == "__main__":
    main()
