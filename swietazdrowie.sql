-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2025 at 07:07 PM
-- Wersja serwera: 10.4.32-MariaDB
-- Wersja PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gedia swieta`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `swietazdrowie`
--

CREATE TABLE `swietazdrowie` (
  `Data` varchar(5) NOT NULL,
  `Nazwa` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `swietazdrowie`
--

INSERT INTO `swietazdrowie` (`Data`, `Nazwa`) VALUES
('01-26', 'Ogólnopolski Dzień Transplantacji'),
('01-25', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-26', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-27', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-28', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-29', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-30', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('01-31', 'Tydzień Walki z Rakiem Szyjki Macicy'),
('02-04', 'Międzynarodowy Dzień Walki z Rakiem'),
('02-11', 'Światowy Dzień Chorego'),
('02-14', 'Dzień Wiedzy o Wrodzonych Wadach Serca'),
('02-23', 'Ogólnopolski Dzień Walki z Depresją'),
('02-28', 'Światowy Dzień Chorób Rzadkich'),
('03-01', 'Dzień Otyłości'),
('03-01', 'Międzynarodowy Dzień Wózka Inwalidzkiego'),
('03-03', 'Światowy Dzień Słuchu'),
('03-05', 'Dzień Dentysty'),
('03-06', 'Europejski Dzień Logopedy'),
('03-09', 'Światowy Dzień Nerek'),
('03-18', 'Europejski Dzień Mózgu'),
('03-20', 'Światowy Dzień Zdrowia Jamy Ustnej'),
('03-21', 'Światowy Dzień Zespołu Downa'),
('03-24', 'Światowy Dzień Gruźlicy'),
('04-07', 'Światowy Dzień Zdrowia'),
('04-07', 'Światowy Dzień Chorego Psychicznie'),
('04-10', 'Dzień Służby Zdrowia'),
('04-11', 'Światowy Dzień Osób z Chorobą Parkinsona'),
('04-15', 'Dzień Trzeźwości'),
('04-17', 'Tydzień dla Serca'),
('04-18', 'Tydzień dla Serca'),
('04-19', 'Tydzień dla Serca'),
('04-20', 'Tydzień dla Serca'),
('04-21', 'Tydzień dla Serca'),
('04-22', 'Tydzień dla Serca'),
('04-23', 'Tydzień dla Serca'),
('04-24', 'Tydzień dla Serca'),
('04-22', 'Światowy Dzień Ziemi'),
('05-03', 'Międzynarodowy Dzień Astmy i Alergii'),
('05-05', 'Europejski Dzień Protestu Przeciwko Dyskryminacji Osób Niepełnosprawnych'),
('05-06', 'Światowy Dzień Astmy'),
('05-06', 'Tydzień PCK'),
('05-07', 'Tydzień PCK'),
('05-08', 'Tydzień PCK'),
('05-09', 'Tydzień PCK'),
('05-10', 'Tydzień PCK'),
('05-11', 'Tydzień PCK'),
('05-12', 'Tydzień PCK'),
('05-12', 'Międzynarodowy Dzień Pielęgniarek i Położnych'),
('05-12', 'Międzynarodowy Dzień Osób Niepełnosprawnych Umysłowo'),
('05-15', 'Międzynarodowy Dzień Rodziny'),
('05-18', 'Światowy Dzień Rodziny'),
('05-19', 'Międzynarodowy Dzień Pamięci Zmarłych na AIDS'),
('05-26', 'Tydzień Promocji Karmienia Piersią'),
('05-27', 'Tydzień Promocji Karmienia Piersią'),
('05-28', 'Tydzień Promocji Karmienia Piersią'),
('05-29', 'Tydzień Promocji Karmienia Piersią'),
('05-30', 'Tydzień Promocji Karmienia Piersią'),
('05-31', 'Tydzień Promocji Karmienia Piersią'),
('06-01', 'Tydzień Promocji Karmienia Piersią'),
('05-31', 'Światowy Dzień bez Tytoniu'),
('06-01', 'Dzień Dziecka'),
('06-04', 'Międzynarodowy Dzień Przeciwdziałania Agresji Wobec Dzieci'),
('06-04', 'Dni Walki z Rakiem'),
('06-05', 'Dni Walki z Rakiem'),
('06-06', 'Dni Walki z Rakiem'),
('06-07', 'Dni Walki z Rakiem'),
('06-08', 'Dni Walki z Rakiem'),
('06-09', 'Dni Walki z Rakiem'),
('06-10', 'Dni Walki z Rakiem'),
('06-11', 'Dni Walki z Rakiem'),
('06-12', 'Dni Walki z Rakiem'),
('06-13', 'Dni Walki z Rakiem'),
('06-14', 'Światowy Dzień Krwiodawstwa'),
('06-24', 'Światowy Dzień Osteoporozy'),
('06-26', 'Międzynarodowy Dzień Zapobiegania Narkomanii'),
('06-27', 'Światowy Dzień Walki z Cukrzycą'),
('07-11', 'Światowy Dzień Ludności'),
('08-01', 'Światowy Tydzień Karmienia Piersią'),
('08-02', 'Światowy Tydzień Karmienia Piersią'),
('08-03', 'Światowy Tydzień Karmienia Piersią'),
('08-04', 'Światowy Tydzień Karmienia Piersią'),
('08-05', 'Światowy Tydzień Karmienia Piersią'),
('08-06', 'Światowy Tydzień Karmienia Piersią'),
('08-07', 'Światowy Tydzień Karmienia Piersią'),
('08-27', 'Narodowy Dzień Życia'),
('09-09', 'Światowy Dzień FAS'),
('09-21', 'Światowy Dzień Walki z Chorobą Alzheimera'),
('09-24', 'Światowy Dzień Serca'),
('09-26', 'Dzień Serca'),
('09-28', 'Międzynarodowy Dzień Ludzi Niesłyszących'),
('10-01', 'Międzynarodowy Dzień Walki z WZW C'),
('10-01', 'Międzynarodowy Dzień Osób Starszych'),
('10-01', 'Międzynarodowy Dzień Pracownika Służby Zdrowia'),
('10-01', 'Światowy Dzień Świadomości o Zapaleniach Wątroby'),
('10-01', 'Międzynarodowy Dzień Lekarza'),
('10-31', 'Miesiąc Profilaktyki Raka Piersi'),
('12-01', 'Światowy Dzień Walki z AIDS'),
('12-03', 'Światowy Dzień Osób Niepełnosprawnych'),
('12-05', 'Międzynarodowy Dzień Wolontariusza'),
('12-10', 'Międzynarodowy Dzień Praw Człowieka');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
