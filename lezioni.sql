-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Ago 05, 2020 alle 17:39
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
  `giorno` set('Lunedi','Martedi','Mercoledi','Giovedi','Venerdi','Sabato','Domenica') NOT NULL,
  `orario_inizio` time NOT NULL,
  `orario_fine` time NOT NULL,
  `aula` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `lezioni`
--

INSERT INTO `lezioni` (`corso`, `giorno`, `orario_inizio`, `orario_fine`, `aula`) VALUES
('Algoritmi e Strutture Dati', 'Lunedi', '09:00:00', '13:00:00', 'A2'),
('Algoritmi e Strutture Dati', 'Lunedi', '20:00:00', '21:00:00', 'B6'),
('Algoritmi e Strutture Dati', 'Giovedi', '09:00:00', '13:00:00', 'C1'),
('Analaisi Matematica', 'Venerdi', '10:00:00', '12:00:00', 'A2'),
('Analisi Matematica', 'Martedi', '09:00:00', '11:00:00', 'A4'),
('Matematica Discreta', 'Martedi', '11:00:00', '13:00:00', 'B1'),
('Matematica Discreta', 'Giovedi', '13:00:00', '14:00:00', 'A3'),
('Programmazione 1', 'Lunedi', '13:00:00', '15:00:00', 'A1'),
('Programmazione 1', 'Mercoledi', '09:00:00', '12:00:00', 'A1'),
('Programmazione 1', 'Venerdi', '09:00:00', '10:00:00', 'A1'),
('Programmazione 2', 'Lunedi', '15:00:00', '17:00:00', 'A3'),
('Programmazione 2', 'Mercoledi', '12:00:00', '14:00:00', 'B3');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `lezioni`
--
ALTER TABLE `lezioni`
  ADD PRIMARY KEY (`corso`,`giorno`,`orario_inizio`,`orario_fine`,`aula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
