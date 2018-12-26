import pandas as pd

try:
    import urllib2 as ulib
except ImportError:
    import urllib as ulib

try:
    from StringIO import BytesIO as io
except ImportError:
    from io import BytesIO as io

try:
    from urllib import urlencode as urlencode
except ImportError:
    from urllib.parse import urlencode as urlencode
    
try:
    from urllib import urlopen as urlopen
except ImportError:
    from urllib.request import urlopen as urlopen
    
try:
    from urllib2 import HTTPError as HTTPError
except ImportError:
    from urllib.error import HTTPError as HTTPError

def queryCartoDB(query, source, formatting = 'CSV'):
    '''queries carto datasets from a given carto account'''
    
    
    data = urlencode({'format': formatting, 'q': query}).encode("utf-8")
    try:
        response = urlopen(source, data)
        return response.read()
    except HTTPError as e:
        raise (ValueError('\n'.join(ast.literal_eval(e.readline())['error'])))
        
def get_data(query, sql_source):
    '''submits a query to queryCartoDB and returns a pandas dataframe'''
    
    try:
        return pd.read_csv(io(queryCartoDB(query, source=sql_source)), sep = ',')
    except ValueError as v:
        print (str(v))
