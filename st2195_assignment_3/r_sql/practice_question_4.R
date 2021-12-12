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
question_4_data <- dbGetQuery(conn, 
  "SELECT field9
  FROM ontime 
  WHERE field22 = '1'")

sort(table(question_4_data))
