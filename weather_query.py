import requests
import json

def weather_query(key, station, start, end, time_zone='America/Chicago', time_format='Y-m-d%20H:i'):
    """
    Variable names here are consistent with those in the Weather Stack Documentation
    
    key: The api key provided by Weather Stack
    station: The weather station id
    start: Starting date for query
    end: Ending date for query
    time_zone: The time zone to report the measurements in
    time_format: The datetime format of the results
    
    Returns a query to meteostat in json format.
    """
    
    head = 'https://api.meteostat.net/v1/history/hourly'
    url = f'{head}?station={station}&start={start}&end={end}&time_zone={time_zone}&time_format={time_format}&key={key}'
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise requests.ConnectionError("Expected status code 200, but got {}" \
                                       .format(response.status_code))
    else:
        return response.json()