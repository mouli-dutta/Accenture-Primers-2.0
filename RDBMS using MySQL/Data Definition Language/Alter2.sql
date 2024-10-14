ALTER TABLE Booking_Master
ADD CONSTRAINT fk
FOREIGN KEY (Enquiry_Id) REFERENCES Enquiry_Master(Enquiry_Id);
