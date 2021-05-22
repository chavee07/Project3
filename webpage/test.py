import psycopg2
import pprint
import json
from sqlalchemy import create_engine


# create params_dic
param_dic = {
    "host"      : "project3.cexcs0a519gc.us-west-1.rds.amazonaws.com",
    "database"  : "project3",
    "user"      : "postgres",
    "password"  : "postgres"
}
    
# set up connection
connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (
    param_dic['user'],
    param_dic['password'],
    param_dic['host'],
    param_dic['database']
)

engine = create_engine(connect)
conn = engine.connect()
results = conn.execute('Select * from df')

# Create a dictionary from the row data and append to a list of all_passengers
all_countries = []
 
for country, con_code, score, gdp, social, health, freedom, generosity, corruption, alcohol, beer_servings, wine_servings, spirit_servings in results:
        countries_dict = {}
        countries_dict["Country"] = country
        countries_dict["Country Code"] = con_code
        countries_dict["Score"] = score
        countries_dict["GDP per capita"] = gdp
        countries_dict["Social support"] = social
        countries_dict["Health life expectancy"] = health
        countries_dict["Freedom to make life choices"] = freedom
        countries_dict["Generosity"] = generosity
        countries_dict["Perceptions of corruption"] = corruption
        countries_dict["Alcohol Consumption per Capita (liter)"] = alcohol
        countries_dict["Beer"] = beer_servings
        countries_dict["Wine"] = wine_servings
        countries_dict["Spirits"] = beer_servings
        all_countries.append(countries_dict)



print(all_countries)
