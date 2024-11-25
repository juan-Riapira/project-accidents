

-- Cargar Locations.csv primero
LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\location.csv' 
INTO TABLE Location
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_location,geometry,municipio)

LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\Class_of_accident.csv' 
INTO TABLE Class_of_accident
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_class_of_accident,class_of_accident,possible_class)

LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\tabla_condiciones.csv' 
INTO TABLE conditions
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_conditions ,surface_condition,land ,weather_condition )

LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\date_accident.csv' 
INTO TABLE Date_Accident
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_date,day,month,year,weekday)

LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\tabla_accidentes.csv' 
INTO TABLE Accident
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_accidente,accident_time,id_date  ,id_location ,id_condition ,id_class_accident )


LOAD DATA
INFILE 'C:\Users\juan3\OneDrive\Documentos\UPTC\DB2\accident_project\src\utils\collateral_damage.csv' 
INTO TABLE Collateral_damage
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
(id_collateral_damage,deaths,wounded,id_accident)
