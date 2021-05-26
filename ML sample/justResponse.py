import urllib.request
import os
# If you are using Python 3+, import urllib instead of urllib2

import json 


data =  {
  "Inputs": {
    "input1": {
      "ColumnNames": [
        "GDP per capita",
        "Alcohol Consumption per Capita (liter)",
        "equal_or_lower_than_5.41?"
      ],
      "Values": [
          [
          "0",
          "0",
          "0"
        ],
    
      ]
    }
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))
#example URL: https://ussouthcentral.services.azureml.net/workspaces/91af20abfc58455182eaaa615d581c59/services/da7cdb9359a443f0abdef36d30ce8f1c/execute?api-version=2.0&details=true
url = 'https://ussouthcentral.services.azureml.net/workspaces/0018df5d0829491794032862bb44c32e/services/1ed439bbd5fb4fef9e7ba4292200b61b/execute?api-version=2.0&details=true'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}



req =urllib.request.Request(url, body, headers) 
print(req)
try:
    response =urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 