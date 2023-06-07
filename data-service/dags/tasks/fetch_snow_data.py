import csv
import urllib3

from airflow.decorators import task

@task(task_id="fetch_snow_data")
def fetch_snow_data():
    request_url = f"https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customMultiTimeSeriesGroupByStationReport/daily/start_of_period/814:UT:SNTL%7Cid=%22%22%7Cname/-6,0/WTEQ::value?fitToScreen=false"
    http = urllib3.PoolManager() # May need to set headers
    response = http.request('GET', request_url)

    if response.status == 200:
        csv_lines = response.data.decode().splitlines()
        csv_lines = filter(lambda x: not x.startswith('#'), csv_lines)
        csv_data = csv.reader(csv_lines)
        for row in csv_data:
            print(row)
    else:
        print("failed to fetch CSV")
        print(response.json())

    # TODO: Insert new snowtel data into Postgres