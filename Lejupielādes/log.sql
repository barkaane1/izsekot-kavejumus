-- Keep a log of any SQL queries you execute as you solve the mystery.
---1.uzdevms---
SELECT description FROM crime_scene_reports
WHERE street = "Humphrey Street"
AND month = 7
AND day = 28;
--- meklē 3 lieciniekus---
SELECT name, transcript FROM interviews
WHERE transcript like "%bakery%"
AND month = 7
AND day = 28;
---mekle to kas bija pie bankomata
SELECT account_number from atm_transactions
where month = 7 
and day = 28 
and atm_location = "Leggett Street";
--- lidojums no rita
SELECT origin_airport_id, destination_airport_id, min(hour) from flights
inner JOIN airports
where airports.id = flights.origin_airport_id
and month = 7 and day = 29;

---mekle cilveku 
SELECT people.name
FROM atm_transactions
INNER JOIN bank_accounts
  ON bank_accounts.account_number = atm_transactions.account_number
INNER JOIN people
  ON people.id = bank_accounts.person_id
WHERE atm_transactions.day = 28
AND atm_transactions.month = 7
AND atm_transactions.atm_location = "Leggett Street";
--- mekle kas izbrauca no bekerejas
--SELECT name from people
--INNER join bakery_security_logs
--where people.license_plate = bakery_security_logs.license_plate
-- and month = 7 
-- and day = 28
-- and activity = "exit"
-- inner join 









