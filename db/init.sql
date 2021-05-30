CREATE user dms_user;
CREATE database dms_db;
USE dms_db;
GRANT ALL on dms_db to dms_user;
CREATE table events (
    ContactID int,
    TriggerTime time,
    ContactType varchar(255),
    Message blob
    );
CREATE table contacts (
    ContactName varchar(255),
    ContactID int,
    PhoneNumber varchar(10),
    Passkey varchar(16)
)