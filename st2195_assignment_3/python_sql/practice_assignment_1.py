#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:56:13 2021

@author: goncalodelacerda
"""
import os

try:
    os.remove('Airline2.db')
except OSError:
    pass

import sqlite3
conn = sqlite3.connect('Airline2.db')

import pandas as pd

ontime = pd.read_csv("/Users/goncalodelacerda/Desktop/programming for data science/Practice Assignment 3/ontime.csv")
plane_data = pd.read_csv("/Users/goncalodelacerda/Desktop/programming for data science/Practice Assignment 3/plane-data.csv")
airports = pd.read_csv("/Users/goncalodelacerda/Desktop/programming for data science/Practice Assignment 3/airports.csv")
carriers = pd.read_csv("/Users/goncalodelacerda/Desktop/programming for data science/Practice Assignment 3/carriers.csv")

ontime.to_sql('ontime', con = conn, index = False) 
plane_data.to_sql('plane-data', con = conn, index = False)
airports.to_sql('airports', con = conn, index = False)
carriers.to_sql('carriers', con = conn, index = False)

