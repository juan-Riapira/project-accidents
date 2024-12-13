-- Cargar Locations.csv primero
LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\data\date_accident.csv' 
INTO TABLE Date_Accident
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_date,day,month,year,weekday,time_of_accident)