import requests
import random
import psycopg2
import psycopg2.extras
from secrets import host, user, password

# Connect to this api https://restcountries.com/v2/name/ and get the data for the list of countries and store into varialbe list_countries

list_countries = requests.get("https://restcountries.com/v2/all").json()

get_country_name = list_countries[0]["name"]

# loop 10 times, get a random country from the list_countries and store it into a list called random_country_list_10

random_country_list_10 = []

while len(random_country_list_10) < 10:
    random_country = random.choice(list_countries)
    random_country_list_10.append(random_country)

print(random_country_list_10)

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

# function to connect to postgres sql database called day6

database = "day6"
connect = psycopg2.connect(host=host, database=database, user=user, password=password)

if connect.closed == 0:
    print("Connection is open")
else:
    print("Connection is closed")

# for each country in the list random_country_list_10, select the name, capitable, flag, subregion and population keys and push the values in the table country_details in database day6, match name to country_name, capital to country_capital, flag to country_flag, subregion to country_subregion and population to country_population

for country in random_country_list_10:
    name = country["name"]
    capital = country["capital"]
    flag = country["flag"]
    subregion = country["subregion"]
    population = country["population"]

    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO country_details (country_name, country_capital, country_flag, country_subregion, country_population) VALUES (%s, %s, %s, %s, %s)",
        (name, capital, flag, subregion, population),
    )
    connect.commit()

cursor.close()
