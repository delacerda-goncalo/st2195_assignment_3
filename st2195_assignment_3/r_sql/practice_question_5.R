## Connect to airline.db SQLite Database
library("DBI")
conn <- dbConnect(RSQLite::SQLite(), "/Users/goncalodelacerda/Documents/GitHub/st2195_assignment_2/python_csv/Airline2.db")
dbListTables(conn)

## Create reference to the tables in the database
library ("dplyr")
airports_db <- tbl(conn, "airports")
carriers <- tbl(conn, "carriers")
ontime <- tbl(conn, "ontime")
plane <- tbl(conn, "plane-data")

## obtain list of cities with the most inbound flights (excluding cancelled) 
question_5_data <- dbGetQuery(conn, 
  "SELECT field11, AVG(CAST(field16 AS INT)) as dep_delay
  FROM ontime 
  WHERE field22 = 0 AND field24 = 0 AND field16 > 0
  GROUP BY field11")

sort(table(question_5_data))
