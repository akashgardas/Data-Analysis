=========================================================
--------------------------DAY 5--------------------------
=========================================================
# PostgreSQL

1. Introduction to Databases & SQL

    What is a database, DBMS, RDBMS
    Difference between SQL & NoSQL
    SQL categories: DDL, DML, DCL, TCL

2. Data Definition Language (DDL)

    CREATE DATABASE, CREATE TABLE
    Data types (INT, VARCHAR, DATE, DECIMAL, etc.)
    Constraints:
    PRIMARY KEY
    FOREIGN KEY
    NOT NULL
    UNIQUE
    CHECK
    DEFAULT
    ALTER TABLE (add/modify/drop column)
    DROP TABLE, TRUNCATE

3. Data Manipulation Language (DML)

    INSERT INTO (single row, multiple rows)
    UPDATE (with WHERE)
    DELETE vs TRUNCATE

4. Basic Queries

    SELECT basics
    WHERE conditions (comparison, logical operators, BETWEEN, IN, LIKE)
    Sorting: ORDER BY (ASC/DESC)
    Limiting results: LIMIT, TOP (depends on DB)
    Removing duplicates: DISTINCT

5. Aggregate Functions

    COUNT, SUM, AVG, MIN, MAX
    GROUP BY
    HAVING (difference between WHERE and HAVING)

6. Joins

    Types of Joins:
    INNER JOIN
    LEFT JOIN / RIGHT JOIN
    FULL JOIN
    CROSS JOIN
    Self Join
    Using multiple joins

7. Subqueries

    Simple subquery in WHERE
    Subquery in FROM


---------------------------------------------------------
Supabase: Uses PostgreSQL

---------------------------------------------------------
## Practice
### Scenario: Design the database for a hospital.
    Tasks:

1. Create a table Patients with columns: patient_id, name, email, phone, city.
    patient_id should be primary key.
    email must be unique.
    phone cannot be NULL.

2. Create a table Doctors with columns: doctor_id, name, specialization, phone, fees.
    doctor_id primary key.
    fees > 0 (CHECK).

3. Create a table Appointments with columns: appointment_id, patient_id, doctor_id, appointment_date.
    appointment_id → primary key.
    patient_id references Patients(patient_id).
    doctor_id references Doctors(doctor_id).

4. Alter table Patients to add column age.

### Scenario: Manage hospital data.
    Tasks:
1. Insert 5 patients, 5 doctors.

2. Update the fees of one doctor.

3. Delete one patient (be careful of FK constraints).

4. Increase fees of all cardiologists by 200.

### Basic Queries (SELECT / WHERE / ORDER BY / DISTINCT / LIMIT)
### Scenario: Fetch hospital info.
    Tasks:
1. List all patients from Hyderabad.

2. Show all doctors who charge more than 1000.

3. List unique cities of patients.

4. Show top 3 most expensive doctors (highest fees).

5. Show all patients ordered alphabetically by name.

### Aggregate Functions + GROUP BY + HAVING
### Scenario: Analyze hospital activities.
    Tasks:
1. Find total number of patients.

2. Find total revenue from all appointments (sum of doctor fees).

3. Find average doctor consultation fee.

4. Show total appointments handled by each doctor.

5. Show doctors who handled more than 3 appointments (HAVING).

### Joins (INNER, LEFT, RIGHT, FULL)
### Scenario: Combine data across tables.
    Tasks:
1. Show all appointments with patient name and doctor name.

2. List all patients who consulted "Dr. Ramesh".

3. Find patients who never booked any appointment (LEFT JOIN).

4. Show doctor names along with total patients consulted.

5. Show all doctors and their patients (FULL JOIN, if supported).

### Subqueries
### Scenario: Advanced lookups.
    Tasks:
1. Find doctors who charge above the average consultation fee.

2. Find patients who consulted "Cardiologist".

3. Get the doctor with the maximum fee (using subquery).

4. List patients who booked appointments with the top 3 doctors (by appointment count).

5. Show all doctors who never got any appointment.

---------------------------------------------------------
# Python with database
Requirements:
1) Python program
2) Supabase Client
3) Supabase

Product table in supabase
```
    create table public.products (
    product_id serial not null,
    name text not null,
    sku text not null,
    price numeric(10, 2) not null,
    stock integer not null default 0,
    created_at timestamp with time zone null default now(),
    constraint products_pkey primary key (product_id),
    constraint products_sku_key unique (sku),
    constraint products_price_check check ((price > (0)::numeric))
    ) TABLESPACE pg_default;
```