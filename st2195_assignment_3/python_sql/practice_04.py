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

#question 3: get each uncancelled flight, obtain only carrier column
aac_list = c.execute('''
SELECT field9
FROM ontime 
WHERE field22 = 0
''').fetchall()

counts = Counter(aac_list)
print(counts)
