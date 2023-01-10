import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
import requests
from urllib import parse
from pprint import pprint


def get_data():

    # Dataset: https://data.nationalgrideso.com/demand/daily-demand-update
    sql_query =  '''SELECT * FROM  "177f6fa4-ae49-4182-81ea-0c6b35f26ca6" ORDER BY "_id" ASC LIMIT 100'''
    params = {'sql': sql_query}

    try:
        resposne = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params = parse.urlencode(params))
        data = resposne.json()["result"]
        # print(data) # Printing data
    except requests.exceptions.RequestException as e:
        print(e.response.text)


    df = pd.DataFrame.from_records(data['records'])
    return df

if __name__ == "__main__":
    print(get_data())