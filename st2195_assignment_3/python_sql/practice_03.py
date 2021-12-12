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

#question 3: group companies together, and average their cancellation rate
aac_list = c.execute('''
SELECT field9, AVG(field22) as avg_cancel
FROM ontime 
GROUP BY field9 
''').fetchall()


lst = [[x[0], float(x[1])] for x in aac_list]
lst.sort(key=lambda x: x[1])

print(lst)