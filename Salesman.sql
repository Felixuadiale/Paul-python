CREATE TABLE IF NOT EXISTS SALESMAN(
Salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
Commission TEXT
);

INSERT INTO SALESMAN VALUES
('5001','James Hoog','New York','0.15'),
('5002','Nail Knite','Paris','0.13'),
('5005','Pit Alex','London','0.11'),
('5006','Mc Lyon','paris','0.14'),
('5007','Paul Adam','Rome','0.13'),
('5003','Lauson Hen','Sac Jose','0.12');

SELECT * FROM SALESMAN ORDER BY name;
SELECT  Salesman_id,Commission from SALESMAN WHERE name like '%Hoog';
SELECT * FROM SALESMAN WHERE Commission < 0.13;
SELECT SUM(Commission)FROM SALESMAN;