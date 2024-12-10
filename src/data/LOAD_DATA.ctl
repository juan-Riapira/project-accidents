-- Cargar Locations.csv primero
LOAD DATA
INFILE 'C:\Users\bibia\Documents\ProjectsVScode\5-Semestre\Bases de Datos\project-accidents\src\data\date_accident.csv' 
INTO TABLE Date_Accident
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_date,day,month,year,weekday,time)