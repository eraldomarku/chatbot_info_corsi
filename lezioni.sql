-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Lug 30, 2020 alle 14:20
-- Versione del server: 10.4.11-MariaDB
-- Versione PHP: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `triennale_lezioni`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `lezioni`
--

CREATE TABLE `lezioni` (
  `corso` varchar(100) NOT NULL,
  `data` date NOT NULL,
  `orario_inizio` time NOT NULL,
  `orario_fine` time NOT NULL,
  `aula` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `lezioni`
--

INSERT INTO `lezioni` (`corso`, `data`, `orario_inizio`, `orario_fine`, `aula`) VALUES
('Algoritmi', '2020-07-29', '19:00:00', '18:00:00', 'A2'),
('Algoritmi', '2020-07-31', '11:00:00', '13:00:00', 'C2'),
('Programmazione I', '2020-07-31', '09:00:00', '10:00:00', 'A'),
('Programmazione I', '2020-07-31', '10:00:00', '11:00:00', 'B'),
('Programmazione II', '2020-07-29', '20:00:00', '21:00:00', 'C1');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `lezioni`
--
ALTER TABLE `lezioni`
  ADD PRIMARY KEY (`corso`,`data`,`orario_inizio`,`orario_fine`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
