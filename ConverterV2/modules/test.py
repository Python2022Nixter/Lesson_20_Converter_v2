import constants as CONST
import json

with open(CONST.PATH_TO_RATES_JSON) as f:
    json_data = json.load(f)
    date_to_write = json_data['date'] 
    rates_to_write =  json_data['rates'].items() # convert dictionary to tuple of key - value pairs
    rates_to_write = [ [item[0], item[1], F"DATE ('{date_to_write}')"] for item  in json_data['rates'].items()  ]
    print (rates_to_write[0])
    pass
