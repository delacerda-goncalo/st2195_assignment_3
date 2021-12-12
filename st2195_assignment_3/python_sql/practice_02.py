#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:56:22 2021

@author: goncalodelacerda
"""

import sqlite3
import pandas as pd
from collections import Counter


conn = sqlite3.connect('/Users/goncalodelacerda/Documents/GitHub/st2195_assignment_2/python_csv/Airline2.db')
c = conn.cursor()

#obtain column names in airports table
column_names = c.execute('''
PRAGMA table_info (airports);
''').fetchall()

#question 2: obtain list of rows with cities for each uncancelled flight
inbound_cities = c.execute('''
SELECT field18 
FROM ontime 
WHERE field22 = '0'
''').fetchall()

#question 2: using counter, we obtain and print the most common values in the inbound_cities list
counter_inbound = Counter(inbound_cities)
print(counter_inbound.most_common(3))

#question 3: obtain list of companies, flights and total flights
inbound_cities = c.execute('''
SELECT field9 AND field22
FROM ontime 
''').fetchall()
