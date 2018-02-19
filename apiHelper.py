# -*- coding: utf-8 -*-
import requests

from apiHelp import dbHelper


def get_total_records():
    headers = {
        'token': "xfsnLLQnvwvJYcNNnMIpNTRzIZTCWWtk"
    }
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
    querystring = {"offset": 0, "limit": "1000", "sortfield": "name", "sortorder": "asc"}

    res = requests.get(url=url, params=querystring, headers=headers)

    totalRecords = res.json()["metadata"]["resultset"].get("count")

    return totalRecords


def weatherStation(total_no_records):
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
    headers = {
        'token': "xfsnLLQnvwvJYcNNnMIpNTRzIZTCWWtk"
    }
    k = (total_no_records / 1000) + 1
    for i in range(int(k)):
        o = (i*1000)+1
        querystring = {"offset": o, "limit": "1000", "sortfield": "name", "sortorder": "asc"}

        res = requests.get(url=url, params=querystring, headers=headers)
        #data = res.json()["metadata"]["resultset"].get("count")

        if res.status_code == 200:
            data = res.json()
            results = data.get("results")


            dbHelper.insertData(results)


if __name__ == '__main__':
    weatherStation(get_total_records())
