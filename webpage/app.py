# import dependencies
import psycopg2
import pprint
from flask import Flask, request, render_template, jsonify, current_app
import json
from sqlalchemy import create_engine 
import urllib.request
import os
from os import environ
from wtforms.widgets.core import TextInput
app = Flask(__name__)


from datetime import datetime
from flask import render_template, request, redirect
# from FlaskAppAML import app
#testing
# from FlaskAppAML.forms import SubmissionForm
from wtforms import Form, StringField, TextAreaField, validators
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
class SubmissionForm(Form):
    consumption = StringField('consumption', [validators.Length(min=1, max=10)])
    gdp = StringField('gdp', [validators.Length(min=1, max=10)])
    text = TextAreaField('Text', [validators.Length(min=1, max=500)])

BRAIN_ML_KEY=os.environ.get('API_KEY', "6Y7OIHwX81CHPIWweiBbG8S7O2til34fyrW3IyddygcrpAFsr8P5j2y90YtvJlPzYU/UB5f9JQN9j8gCAqrAJQ==")
BRAIN_URL = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/0018df5d0829491794032862bb44c32e/services/8a57db277ac34954933dffead2a43867/execute?api-version=2.0&details=true")
# Deployment environment variables defined on Azure (pull in with os.environ)

# Construct the HTTP request header
# HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}

HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ BRAIN_ML_KEY)}


@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template('index.html')
@app.route("/index")
def home():
    """List all available api routes."""
    return render_template('index.html')
@app.route("/machinelearning", methods=['GET', 'POST'])
def ml():
    """Renders the home page which is the CNS of the web app currently, nothing pretty."""

    form = SubmissionForm(request.form)
    # Form has been submitted
    if request.method == 'POST' and form.validate():

        # Plug in the data into a dictionary object 
        #  - data from the input form
        #  - text data must be converted to lowercase
        data =  {
              "Inputs": {
                "input1": {
                 "ColumnNames": ["GDP per capita", "Alcohol Consumption per Capita (liter)", "equal_or_lower_than_5.41?"],
                 "Values": [[form.gdp.data.lower(), form.consumption.data.lower(),0 ]]
               
               
                }
              },
              "GlobalParameters": {}
            }


        # Serialize the input data into json string
        body = str.encode(json.dumps(data))
        print(body) 
        # Formulate the request
        #req = urllib.request.Request(URL, body, HEADERS)
        req = urllib.request.Request(BRAIN_URL, body, HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            # response = requests.post(URL, headers=HEADERS, data=body)
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'result.html',
                title="This is the result from AzureML running our example Student Brain Weight Prediction:",
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'result.html',
                title='There was an error',
                result=result)
            #print(err)

    # Just serve up the input form
    return render_template(
        'form.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='Demonstrating a website using Azure ML Api')



@app.route("/landing")
def names():
    #################################################
    # Database Setup
    #################################################
    # create params_dic
    param_dic = {
    "host"      : 'project3.cexcs0a519gc.us-west-1.rds.amazonaws.com',
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
        countries_dict["beer_servings"] = beer_servings
        countries_dict["wine_servings"] = wine_servings
        countries_dict["spirit_servings"] = beer_servings
        all_countries.append(countries_dict)
    return jsonify(all_countries)

@app.route("/maps")
def maps():
    return render_template('maps.html')
@app.route("/bar")
def bar():
    return render_template('bar.html')
@app.route("/gauge")
def gauge():
    return render_template('gauge.html')
@app.route("/scatterplot")
def scatter():
    return render_template('scatterplot.html')

def do_something_pretty(jsondata):
    """We want to process the AML json result to be more human readable and understandable"""
    import itertools # for flattening a list of tuples below

    # We only want the first array from the array of arrays under "Value" 
    # - it's cluster assignment and distances from all centroid centers from k-means model
    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    #valuelen = len(value)
    print(value)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    output='‘For an alcohol consumption of : '+value[1]+ "<br/>Our Algorithm would calculate the weight to be: "+ value[4]
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output


if __name__ == '__main__':
    app.run(debug=True)# import dependencies
