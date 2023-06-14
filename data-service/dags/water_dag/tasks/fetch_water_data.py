import json
import urllib3

from airflow.decorators import task

sites = [
    "10129500", # Middle Weber
    "10155200", # Middle Provo
]

@task(task_id="fetch_water_data")
def fetch_water_data():
    request_url = f"http://waterservices.usgs.gov/nwis/iv/"
    http = urllib3.PoolManager()
    response = http.request('GET', request_url, fields={
        "format": "json", # json return type
        "period": "P1D", # past 1 day
        "parameterCd": "00060,00010", # fetch cfs and water temp (Celsius)
        # TODO: Batch these requests into 100s of sites
        "sites": ",".join(sites), # the sites to fetch data for
    })

    if response.status != 200:
        print("failed to fetch data")
        print(response.json())
    
    raw_data = response.data.decode()
    json_data = json.loads(raw_data)
    print(json_data)

    # TODO: Extract values from JSON

    # Iterate over each site
    for obj in json_data["value"]["timeSeries"]:
        values = []
        print("Site name:", obj["sourceInfo"]["siteName"])
        print("Site code:", obj["sourceInfo"]["siteCode"][0]["value"])
        
        # Collect the value and timestamp of each observation
        max_value = (-1, "default")
        min_value = (-1, "default")
        for observation in obj["values"][0]["value"]:
            observation_int = int(observation["value"])
            values.append((observation_int, observation["dateTime"]))
            print(f"\t {observation_int} cfs at {observation['dateTime']}")

            if min_value[0] == -1 or min_value[0] > observation_int:
                min_value = (observation_int, observation["dateTime"])

            if max_value[0] == -1 or max_value[0] < observation_int:
                max_value = (observation_int, observation["dateTime"])

        print("Maximum flow:", max_value)
        print("Minimum flow:", min_value)
        print()

        
    # TODO: Insert new snowtel data into Postgres