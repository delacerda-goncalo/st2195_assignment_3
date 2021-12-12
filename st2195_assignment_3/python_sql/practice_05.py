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

#question 5: get flights grouped by plane, exclude cancelled and diverted ones. Average
#their delay number

aac_list = c.execute('''
SELECT field11, AVG(CAST(field16 AS INT)) as dep_delay
FROM ontime 
WHERE field22 = 0 AND field24 = 0 AND field16 IS NOT NULL
GROUP BY field11
''').fetchall()

#st.sort(key=lambda x: x[1])

print(aac_list.sort(key=lambda x: -x[1]))