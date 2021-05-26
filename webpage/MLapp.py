"""
Routes and views for the flask application.
"""
import json
import urllib.request
import os
from os import environ

from flask import Flask
from wtforms.widgets.core import TextInput
app = Flask(__name__)


from datetime import datetime
from flask import render_template, request, redirect
# from FlaskAppAML import app
#testing
# from FlaskAppAML.forms import SubmissionForm
from wtforms import Form, StringField, TextAreaField, validators


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

# Our main app page/route
@app.route('/', methods=['GET', 'POST'])
# def root():
#     return render_template('contact.html')
@app.route('/ML', methods=['GET', 'POST'])
def home():
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


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

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
    output='For an alcohol consumption of : '+value[1]+ "<br/>And a Gdp of: "+ value[0] + "<br/>Our Algorithm would calculate your country to be Happy: "+ value[2] + "with a weight of " + value[4]
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output


if __name__ == '__main__':
    app.run()