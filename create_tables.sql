CREATE CREATE TABLE IF NOT EXISTS FrontDeskOperator
(
    ID INT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL
);

CREATE CREATE TABLE IF NOT EXISTS DataEntryOperator
(
    ID INT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL
);

CREATE CREATE TABLE IF NOT EXISTS DatabaseAdmin
(
    ID INT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Patient
(
    ID INT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Room
(
    ID INT NOT NULL PRIMARY KEY,
    Type TEXT NOT NULL, /* 2 types: Admission and Operation */
    Available BOOLEAN NOT NULL,
);

CREATE TABLE IF NOT EXISTS Doctor
(
    ID INT NOT NULL PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Address TEXT NOT NULL,
    RoomID INT NOT NULL,
    FOREIGN KEY (RoomID) REFERENCES Room(ID)
);

-- CREATE TABLE IF NOT EXISTS TimeSlot
-- (
--     ID INT NOT NULL PRIMARY KEY,
--     Start TIMESTAMP NOT NULL,
--     End TIMESTAMP NOT NULL
-- )

CREATE TABLE IF NOT EXISTS Appointment
(
    ID INT NOT NULL PRIMARY KEY,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    DoctorRoom TEXT NOT NULL,
    StartTime TIMESTAMP NOT NULL,
    EndTime TIMESTAMP NOT NULL,
    Priority INT NOT NULL
    FOREIGN KEY (PatientID) REFERENCES Patient(ID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(ID)
);

CREATE TABLE IF NOT EXISTS Admitted
(
    ID INT NOT NULL PRIMARY KEY,
    PatientID INT NOT NULL,
    RoomID INT NOT NULL,
    StartTime TIMESTAMP NOT NULL,
    EndTime TIMESTAMP, /* Nullable */
    FOREIGN KEY (PatientID) REFERENCES Patient(ID),
    FOREIGN KEY (RoomID) REFERENCES Room(ID)
);

CREATE TABLE IF NOT EXISTS Test
(
    ID INT NOT NULL PRIMARY KEY,
    PatientID INT NOT NULL,
    TestName TEXT NOT NULL,
    TestRoom TEXT NOT NULL,
    StartTime TIMESTAMP NOT NULL,
    EndTime TIMESTAMP NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patient(ID)
);

CREATE TABLE IF NOT EXISTS Operation
(
    ID INT NOT NULL PRIMARY KEY,
    OperationName TEXT NOT NULL,
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    RoomID INT NOT NULL,
    Procedure TEXT NOT NULL,
    StartTime TIMESTAMP NOT NULL,
    EndTime TIMESTAMP NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patient(ID),
    FOREIGN KEY (DoctorID) REFERENCES Doctor(ID),
    FOREIGN KEY (RoomID) REFERENCES Room(ID)
);

CREATE TABLE IF NOT EXISTS AppointmentReport
(
    ID INT NOT NULL PRIMARY KEY, /* Can consider removing reportID */
    AppointmentID INT NOT NULL,
    ReportDate TIMESTAMP NOT NULL,
    Diagnosis TEXT NOT NULL,
    Prescription TEXT, /* Nullable */
    Test TEXT, /* Nullable */
    Procedure TEXT, /* Nullable */
    FOREIGN KEY (AppointmentID) REFERENCES Appointment(ID)
);

CREATE TABLE IF NOT EXISTS TestReport
(
    ID INT NOT NULL PRIMARY KEY, /* Can consider removing reportID */
    TestID INT NOT NULL,
    ReportDate TIMESTAMP NOT NULL,
    Diagnosis TEXT NOT NULL,
    FOREIGN KEY (TestID) REFERENCES Test(ID)
);

CREATE TABLE IF NOT EXISTS OperationReport
(
    ID INT NOT NULL PRIMARY KEY, /* Can consider removing reportID */
    OperationID INT NOT NULL,
    ReportDate TIMESTAMP NOT NULL,
    Diagnosis TEXT NOT NULL,
    FOREIGN KEY (OperationID) REFERENCES Operation(ID)
);
