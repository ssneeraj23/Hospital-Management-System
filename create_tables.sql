CREATE DATABASE dbms_2;
use dbms_2;
CREATE TABLE IF NOT EXISTS Physician (
    EmployeeID INT not NULL,
    Name text not NULL,
    Position text not NULL,
    SSN INT not NULL,
    primary key (EmployeeID)
);
CREATE TABLE IF NOT EXISTS Department(
    DepartmentID INT not NULL,
    Name text not NULL,
    Head INT not NULL,
    primary key (DepartmentID),
    FOREIGN KEY (Head) references Physician(EmployeeID) 
);
CREATE TABLE IF NOT EXISTS Affiliated_with(
    Physician INT not NULL,
    Department INT not NULL,
    PrimaryAffiliation BOOLEAN not NULL,
    primary key (Physician,Department),
    FOREIGN key (Physician) references Physician(EmployeeID),
    FOREIGN key (Department) references Department(DepartmentID)
);
CREATE TABLE IF NOT EXISTS Procedures(
    Code INT not NULL,
    Name text not NULL,
    Cost INT not NULL,
    primary key(Code)
);
CREATE TABLE IF NOT EXISTS Trained_In(
    Physician INT not NULL,
    Treatment INT not NULL,
    CertificationDate datetime not NULL,
    CertificationExpires datetime not NULL,
    primary key (Physician,Treatment),
    FOREIGN key (Physician) references Physician(EmployeeID),
    FOREIGN key (Treatment) references Procedures(Code)
    
);
CREATE TABLE IF NOT EXISTS Nurse(
    EmployeeID INT not NULL,
    Name text not NULL,
    Position text not NULL,
    Registered BOOLEAN not NULL,
    SSN INT not NULL,
    primary key (EmployeeID)
);
CREATE TABLE IF NOT EXISTS Patient(
    SSN INT not NULL,
    Name text not NULL,
    Address text not NULL,
    Phone text not NULL,
    InsuranceID INT not NULL,
    PCP INT not NULL,
    primary key (SSN),
    FOREIGN key (PCP) references Physician(EmployeeID)
);
CREATE TABLE Block(
    Floor INT not NULL,
    Code INT not NULL,
    primary key (Floor,Code)
);
CREATE TABLE Medication(
    Code INT not NULL,
    Name text not NULL,
    Brand text not NULL,
    Description text not NULL,
    primary key(Code)
);
CREATE TABLE IF NOT EXISTS Appointment(
    AppointmentID INT not NULL,
    Patient INT not NULL,
    PrepNurse INT,
    Physician INT not NULL,
    Start datetime not NULL,
    End datetime not NULL,
    ExaminationRoom text not NULL,
    primary key(AppointmentID),
    FOREIGN key (Physician) references Physician(EmployeeID),
    FOREIGN KEY (Patient) references Patient(SSN),
    FOREIGN key(PrepNurse) references Nurse(EmployeeID)
);
CREATE TABLE IF NOT EXISTS Prescribes(
    Physician INT not NULL,
    Patient INT not NULL,
    Medication INT not NULL,
    Date datetime not NULL,
    Appointment INT ,
    Dose text not NULL,
    primary key (Physician,Patient,Medication,Date),
    FOREIGN key (Physician) references Physician(EmployeeID),
    FOREIGN key (Patient) references Patient(SSN),
    FOREIGN KEY (Appointment) references Appointment(AppointmentID),
    FOREIGN KEY (Medication) references Medication(Code)
);
CREATE TABLE IF NOT EXISTS Room(
    Number INT not NULL,
    Type text not NULL,
    BlockFloor INT not NULL,
    BlockCode INT not NULL,
    Unavailable BOOLEAN not NULL,
    primary key(Number),
    FOREIGN key (BlockFloor,BlockCode) references Block(Floor,Code)
);
CREATE TABLE IF NOT EXISTS Stay (
    StayID INT not NULL,
    Patient INT not NULL,
    Room INT not NULL,
    Start datetime not NULL,
    End datetime not NULL,
    primary key (StayID),
    FOREIGN key (Room) references Room(Number),
    FOREIGN KEY (Patient) references Patient(SSN)
);
CREATE TABLE IF NOT EXISTS Undergoes(
    Patient INT not NULL,
    Procedures INT not NULL,
    Stay INT not NULL,
    Date datetime not NULL,
    Physician INT not NULL,
    AssistingNurse INT,
    primary key(Patient,Procedures,Stay,Date),
    FOREIGN key (Procedures) references Procedures(Code),
    FOREIGN key(AssistingNurse) references Nurse(EmployeeID),
    FOREIGN key (Physician) references Physician(EmployeeID),
    FOREIGN key (Patient) references Patient(SSN),
    FOREIGN key (Stay) references Stay(StayID)
);

CREATE TABLE IF NOT EXISTS On_Call(
    Nurse INT not NULL,
    BlockFloor INT not NULL,
    BlockCode INT not NULL,
    Start datetime not NULL,
    End datetime not NULL,
    primary key (Nurse,BlockFloor,BlockCode),
    FOREIGN key (BlockFloor,BlockCode) references Block(Floor,Code),
    FOREIGN key(Nurse) references Nurse(EmployeeID)
);


