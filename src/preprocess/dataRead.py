#encoding=utf-8

import numpy as np
import pandas as pd
import datetime
import urllib

from sodapy import Socrata

#DBmanagement is the self-defined ACTION CLASS
import DBmanagment
import json


def process():

    #create the databace
    dataDb = DBmanagment.DBAction()
    dataDb.db_name("NYCData")
    dataDb.dropDB()


    url = "https://data.cityofnewyork.us/resource/"

    #file names and its Endpoint in NYC open data
    db_names = {
                'FHV_active_data':'p8xb-39i5',
                'FHV_active_and_inactive_vehicles':'k5sk-y8y9',
                'FHV_base_aggregate_report':'edp9-qgv4',
                'new_driver_application':'xtra-f75s',
                'map_of_NYC_subway_entrances':'he7q-3hwy',
                'yellow_taxi_trip_data':'gkne-dk5s',
                'green_taxi_trip_data':'utt9-dvgj',
                'lost_property_information':'t5yn-hzvi',
                'safe_routes_to_schools':'mnpn-iqeb',
                'school_bus_breakdown_delays':'fbkk-fqs7',
                '311service':'fhrw-4uyv',
                'public_pay_telehone_locations':'vzju-a4ks',
                'free_wifi_hotspots':'jd4g-ks2z',
                'DHS_daily_report':'wece-v9d7'
                }
    client = Socrata("data.cityofnewyork.us", 'nx6tpIeRrj5pLGVaCTuxYfLPP', username="kxuak@connect.ust.hk",
                     password="urbanvis2016.XK")

    for key in db_names:

        #**************another way to query data************************
        # queryUrl = (url + db_names[key] + '.json?$limit=50000')
        # raw_data = pd.read_json(queryUrl)
        # print type(raw_data)
        # print np.size(raw_data)
        # datas = raw_data.to_json(orient='records')
        # print np.size(datas)
        # datas = json.loads(datas)


        #create table for each database
        #limit the rows to 1000000, using the Socrata SDK library. There are more query actions can be achieved
        datas = client.get(db_names[key], limit=100000)

        dataDb.createTable(key)
        dataDb.insertDatas(datas)
        dataDb.close()



if __name__ == '__main__':
    process()
