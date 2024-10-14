CREATE TABLE Venue_Master
(
  Venue_Id varchar(10) PRIMARY KEY,
  Event_id varchar(10),
  Venue_name varchar(30),
  Location varchar(50),
  Venue_Cost int,
  Food varchar(10),
  Capacity int,
  Wifi varchar(10),
  Description varchar(50),
  FOREIGN KEY (Event_id) REFERENCES Event_Master(Event_Id)
);
