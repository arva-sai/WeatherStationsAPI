# -*- coding: utf-8 -*-
import psycopg2
import logging


def insertData(data):
    con = psycopg2.connect(host="localhost",
                           database="api",
                           user="postgres",
                           password="453812",
                           port=5432)

    cur = con.cursor()

    for result in data:

        print(result)

        '''
        INSERT INTO apidata.noaadata(
        elevation, mindate, maxdate, latitude, name, datacoverage, id, elevationunit, longitude)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''

        if 'elevation' in result:
            elevation = result.get('elevation')
        else:
            elevation = -999

        if 'elevationUnit' in result:
            elevationUnit = result.get('elevationUnit')
        else:
            elevationUnit = "meters"

        # sql = """INSERT INTO public.apidata(elevation,mindate,maxdate,latitude,name,
        # datacoverage,id,"elevationUnit",longitude) values ({},'{}','{}',{},'{}',{},'{}','{}',{})""".format(
        #     elevation,
        #     result.get("mindate"),
        #     result.get("maxdate"),
        #     result.get("latitude"),
        #     result.get("name"),
        #     result.get("datacoverage"),
        #     result.get("id"),
        #     elevationUnit,
        #     result.get("longitude"))
        '''
        ﻿SELECT public.adddata(
	<_elevation integer>, 
	<_name text>, 
	<_maxdate date>, 
	<_datacoverage numeric>, 
	<_longitude numeric>, 
	<_latitude numeric>, 
	<_elevationunit text>, 
	<_id text>, 
	<_mindate date>
)
        '''

        sql = "SELECT public.adddata({},'{}','{}',{},{},{},'{}','{}','{}')".format(
            int(elevation),
            result.get("name").replace(",",""),
            result.get("maxdate"),
            float(result.get("datacoverage")),
            result.get("longitude"),
            result.get("latitude"),
            elevationUnit,
            result.get("id"),
            result.get("mindate"))

        print(sql)

        cur.execute(sql)

        # print(sql)

        # cur.execute(sql)

    con.commit()
    cur.close()
    con.close()
