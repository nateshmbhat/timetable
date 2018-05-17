-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2018 at 05:19 PM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 7.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `timetable_major`
--

-- --------------------------------------------------------

--
-- Table structure for table `batch`
--

CREATE TABLE `batch` (
  `batchID` varchar(5) NOT NULL,
  `day` int(11) NOT NULL,
  `hour` int(11) NOT NULL,
  `roomId` int(11) NOT NULL,
  `subjectId` varchar(100) NOT NULL,
  `facultyId1` int(11) DEFAULT NULL,
  `facultyId2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `facultyId` int(11) NOT NULL,
  `facultyName` varchar(100) DEFAULT NULL,
  `facultyType` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`facultyId`, `facultyName`, `facultyType`) VALUES
(1, 'Dr. R Sumathi', 0),
(2, 'Dr. N R Sunitha', 0),
(3, 'Dr. R Sathish', 0),
(4, 'Dr. Y S Nijagunarya', 0),
(5, 'Dr. A S Poornima', 0),
(6, 'Dr. A S Manjunath', 1),
(7, 'Dr. K N Sreenath', 2),
(8, 'Dr. M B Nirmala', 2),
(9, 'K G Manjunath', 3),
(10, 'A H Shanthakumara', 3),
(11, 'A V Krishna Mohan', 3),
(12, 'G Bhaskar', 3),
(13, 'K Srinivasa', 3),
(14, 'M Raghavendra', 3),
(15, 'M Kavitha', 3),
(16, 'K R PrasannaKumar', 3),
(17, 'S Thejaswini', 3),
(18, 'V Ravi', 3),
(19, 'S Nayana', 3),
(20, 'Nousheen Taj', 3),
(21, 'R M Savithramma', 3),
(22, 'S P Gururaj', 3),
(23, 'E Guruprasad', 3),
(24, 'H D Kallinatha', 3),
(25, 'H K Vedamurthy', 3),
(26, 'B P Ashwini', 3),
(27, 'C P Prabodh', 3),
(28, 'K S Chandraprabha', 3),
(29, 'K Bhargavi', 3),
(30, 'G S Thejas', 3),
(31, 'Shruti K', 3),
(32, 'Prema S', 3),
(33, 'Shwetha A N', 3),
(34, 'Santhosh S Patil', 3),
(35, 'Ashwini N S', 3),
(36, 'Srujan S N', 3),
(37, 'Anirudhha Prabhu B P', 3),
(38, 'Rashmi T V', 3),
(39, 'Goura A Koti', 3),
(40, 'Prithvi M G', 3),
(41, 'S Suresh Kumar', 3),
(42, 'NA', 3),
(43, 'Chethana M S', 3),
(44, 'Siddagangamma', 3),
(45, 'Ranganath', 3),
(46, 'G J Manjula', 0),
(47, 'P S K Reddy', 0),
(48, 'CIPE', 3),
(49, 'Prasanna B R', 0),
(50, 'Kavitha G N', 2),
(51, 'PATIL HP', 0);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `roomId` int(11) NOT NULL,
  `roomType` int(11) DEFAULT NULL,
  `roomNo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`roomId`, `roomType`, `roomNo`) VALUES
(1, 0, 'CSL001'),
(2, 0, 'CSL002'),
(3, 0, 'CSL003'),
(4, 0, 'CSL101'),
(5, 0, 'CSL102'),
(6, 0, 'CSL103'),
(7, 0, 'CSL104'),
(8, 0, 'CSL105'),
(9, 1, 'Aryabhatta Computer Center'),
(10, 1, 'Rohini Computer Center'),
(11, 1, 'Linux Laboratory'),
(12, 1, 'Bhaskara Computer Center'),
(13, 1, 'M. Tech. CSE Laboratory'),
(14, 1, 'M. Tech. CNE Laboratory'),
(15, 1, 'Project Laboratory'),
(16, 1, 'Research Center'),
(17, 1, 'LD Lab'),
(18, 0, 'NA'),
(19, 0, 'FREE'),
(20, 0, 'ISE304'),
(21, 0, 'M. Tech. CSE Theory'),
(22, 0, 'M. Tech. CNE Theory');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subjectId` varchar(100) NOT NULL,
  `subjectName` varchar(100) DEFAULT NULL,
  `subjectType` int(11) DEFAULT NULL,
  `credits` float(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subjectId`, `subjectName`, `subjectType`, `credits`) VALUES
('3CCI01', 'Computer Organization ', 0, 4.0),
('3CCI02', 'Data Structures', 0, 4.5),
('3CCI03', 'Logic Design', 0, 4.0),
('3CCI04', 'Discrete Mathematical structures', 0, 4.5),
('3CSL01', 'Data Structures  Lab ', 1, 1.5),
('3CSL02', 'Logic Design Lab', 1, 1.5),
('3CSL03', 'Arduino Programming Lab ', 1, 1.0),
('3MAT3C', 'Mathematical Concepts for Information Technology', 0, 3.5),
('4CCI01', 'Object Oriented Programming with C++ ', 0, 4.0),
('4CCI02', 'Analysis & Design of Algorithms ', 0, 4.0),
('4CCI03', 'Finite Automata & Formal Languages', 0, 4.0),
('4CCI04', ' Graph Theory and Combinatorics ', 0, 4.0),
('4CS01', 'Microcontroller ', 0, 4.0),
('4CSL01', 'Object Oriented Programming Lab.', 1, 1.5),
('4CSL02', 'Microcontroller Lab.', 1, 1.5),
('4MAT2', 'Statistics and Probability Theory ', 0, 3.5),
('5CCI01 ', 'Database management Systems', 0, 4.0),
('5CCI02', 'Data Communications', 0, 4.0),
('5CCI03', 'Operating Systems', 0, 4.0),
('5CCI04', 'UNIX and Shell Programming ', 0, 4.0),
('5CSL01', 'Analysis & Design of\nAlgorithms Lab', 1, 1.5),
('5CSL02', 'Java Programming Lab ', 1, 1.5),
('5CSMP', 'Mini Project ', 2, 0.0),
('6CCI01 ', 'Computer Networks', 0, 4.0),
('6CCI02', 'Software Engineering', 0, 4.0),
('6CS01', 'System Software and Compiler Design', 0, 4.0),
('6CS03', 'Computer Graphics and visualization', 0, 3.0),
('6CSL01', 'Database Management System Lab', 1, 1.5),
('6CSL03', 'Compiler Design and Operating System Lab', 1, 1.5),
('6CSL04', 'Computer Graphics and visualization Lab', 1, 1.0),
('6CSMP', 'Mini Project', 2, 1.0),
('7CCI01', 'Cryptography & Network Security ', 0, 4.0),
('7CS02', 'Object Oriented Modeling and Design', 0, 4.0),
('7CSL01', 'Network Programming Lab', 1, 1.5),
('7CSL02', 'Cryptography & Network Security Lab', 1, 1.5),
('ASE', 'Advanced  Software Engineering', 0, 3.0),
('AWN', 'Adhoc Wireless Networks', 0, 3.0),
('CSIT ', 'Industrial Training', 5, 0.0),
('CSMP7 ', 'Major Project ', 4, 3.0),
('CSMP8', 'Major Project ', 5, 9.9),
('CSPE01', 'Artificial Intelligence', 0, 3.0),
('CSPE02', 'Advanced DBMS', 0, 3.0),
('CSPE03', 'Data Compression', 0, 3.0),
('CSPE05', 'C# and .Net Technologies', 0, 3.0),
('CSPE06', 'Multimedia Computing', 0, 3.0),
('CSPE07', 'Data warehouse and Data Mining', 0, 3.0),
('CSPE08', 'Cloud Computing', 0, 3.0),
('CSPE09', 'Distributed Operating System', 0, 3.0),
('CSPE10', 'System Simulation & Modeling', 0, 3.0),
('CSPE11', 'Fuzzy Logic', 0, 3.0),
('CSPE12', 'Wireless Sensor Networks', 0, 3.0),
('CSPE13', 'Advanced Computer Architecture', 0, 3.0),
('CSPE14', 'Web 2.0 & rich internet application', 0, 3.0),
('CSPE15', 'Software Architecture', 0, 3.0),
('CSPE16', 'Computer Systems & Performance Analysis', 0, 3.0),
('CSPE17', 'Storage Area Networks', 0, 3.0),
('CSPE19', 'Communication Protocol Engineering', 0, 3.0),
('CSPE20', 'Ad hoc Wireless Networks', 0, 3.0),
('CSPE21', 'Multi-Core Architecture and Programming', 0, 3.0),
('CSPE22', 'Advanced Algorithms', 0, 3.0),
('CSPE23', 'Web Design Technique', 0, 3.0),
('CSPE24', 'Parallel Algorithms', 0, 3.0),
('CSPE25', 'Fundamentals of Digital Image Processing', 0, 3.0),
('CSPE26', 'Service Oriented Architecture', 0, 3.0),
('CSPE27', 'Mobile Computing', 0, 3.0),
('CSPE28', 'High Performance Computing', 0, 3.0),
('CSPE29', 'Network Management', 0, 3.0),
('CSPE30', 'Cyber Security', 0, 3.0),
('CSPE31', 'Software Testing', 0, 3.0),
('CSPE32', 'Advanced UNIX Programming ', 0, 3.0),
('CSPE33', 'Foundations of Data Science', 0, 3.0),
('CSTS', 'Technical Seminar ', 6, 1.0),
('DCS', 'Distributed Computing Systems', 0, 3.0),
('FR', 'FREE', 0, 0.0),
('HS22', 'Environmental Science ', 8, 3.0),
('HSS22', 'Humanity and Social Sciences', 8, 3.0),
('LFR', 'Lab-Free', 1, 0.0),
('MC03', ' Const. of India & Prof. Ethics ', 0, 0.0),
('MC05', 'Aptitude Related Analytical Skills', 3, 0.0),
('MC06', 'Soft Skills', 3, 0.0),
('NA', 'Not Allocated', 0, 0.0),
('OE01', 'Open Elective 1', 0, 3.0),
('OE02', 'Open Elective 2', 0, 3.0),
('OE03', 'Open Elective 3', 0, 3.0),
('ON', 'Optical Networks', 0, 3.0),
('PE01', 'Professional Elective - 1', 0, 3.0),
('PE02', 'Professional Elective - 2', 0, 3.0),
('PE03', 'Professional Elective - 3', 0, 3.0),
('PE04', 'Professional Elective - 4', 0, 3.0),
('PE05', 'Professional Elective - 5', 0, 3.0),
('PE06', 'Professional Elective - 6', 0, 3.0),
('SC', 'Soft Computing', 0, 3.0);

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `batchID` varchar(30) NOT NULL,
  `subjectID` varchar(30) NOT NULL,
  `facultyID1` int(11) NOT NULL,
  `facultyID2` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`batchID`, `subjectID`, `facultyID1`, `facultyID2`) VALUES
('4A', '4CCI01', 29, 42),
('4A', '4CCI02', 5, 42),
('4A', '4CCI03', 21, 42),
('4A', '4CCI04', 47, 42),
('4A', '4CS01', 39, 42),
('4A', '4MAT2', 46, 42),
('4A', '4MAT2', 48, 42),
('4A', 'FR', 42, 42),
('4A', 'MC03', 48, 42),
('4A1', '4CSL01', 24, 29),
('4A1', '4CSL02', 18, 39),
('4A1', 'LFR', 42, 42),
('4A2', '4CSL01', 24, 29),
('4A2', '4CSL02', 25, 39),
('4A2', 'LFR', 42, 42),
('4A3', '4CSL01', 24, 29),
('4A3', '4CSL02', 39, 18),
('4A3', 'LFR', 42, 42),
('4B', '4CCI01', 27, 42),
('4B', '4CCI02', 21, 42),
('4B', '4CCI03', 26, 42),
('4B', '4CCI04', 50, 42),
('4B', '4CS01', 15, 42),
('4B', '4MAT2', 49, 42),
('4B', 'FR', 42, 42),
('4B', 'MC03', 48, 42),
('4B1', '4CSL01', 31, 27),
('4B1', '4CSL02', 15, 18),
('4B1', 'LFR', 42, 42),
('4B2', '4CSL01', 31, 27),
('4B2', '4CSL02', 25, 15),
('4B2', 'LFR', 42, 42),
('4B3', '4CSL01', 38, 8),
('4B3', '4CSL02', 25, 18),
('4B3', 'LFR', 42, 42),
('4C', '4CCI01', 33, 42),
('4C', '4CCI02', 31, 42),
('4C', '4CCI03', 36, 42),
('4C', '4CCI04', 41, 42),
('4C', '4CS01', 9, 42),
('4C', '4MAT2', 51, 42),
('4C', 'FR', 42, 42),
('4C', 'MC03', 48, 42),
('4C1', '4CSL01', 32, 12),
('4C1', '4CSL02', 31, 18),
('4C1', 'LFR', 42, 42),
('4C2', '4CSL01', 34, 31),
('4C2', '4CSL02', 18, 9),
('4C2', 'LFR', 42, 42),
('4C3', '4CSL01', 22, 34),
('4C3', '4CSL02', 19, 9),
('4C3', 'LFR', 42, 42),
('6A', '6CCI01 ', 24, 42),
('6A', '6CCI02', 35, 42),
('6A', '6CS01', 26, 42),
('6A', '6CS03', 33, 42),
('6A', 'CSPE01', 4, 42),
('6A', 'CSPE08', 20, 42),
('6A', 'CSPE22', 25, 42),
('6A', 'CSPE28', 29, 42),
('6A', 'FR', 42, 42),
('6A1', '6CSL01', 27, 34),
('6A1', '6CSL03', 26, 19),
('6A1', '6CSL04', 20, 34),
('6A1', 'LFR', 42, 42),
('6A2', '6CSL01', 27, 13),
('6A2', '6CSL03', 26, 37),
('6A2', '6CSL04', 38, 40),
('6A2', 'LFR', 42, 42),
('6A3', '6CSL01', 12, 16),
('6A3', '6CSL03', 26, 28),
('6A3', '6CSL04', 33, 20),
('6A3', 'LFR', 42, 42),
('6B', '6CCI01 ', 22, 42),
('6B', '6CCI02', 37, 42),
('6B', '6CS01', 11, 42),
('6B', '6CS03', 20, 42),
('6B', 'CSPE01', 3, 42),
('6B', 'CSPE08', 25, 42),
('6B', 'CSPE22', 38, 42),
('6B', 'CSPE28', 29, 42),
('6B', 'FR', 42, 42),
('6B1', '6CSL01', 12, 16),
('6B1', '6CSL03', 32, 33),
('6B1', '6CSL04', 20, 28),
('6B1', 'LFR', 42, 42),
('6B2', '6CSL01', 10, 12),
('6B2', '6CSL03', 1, 11),
('6B2', '6CSL04', 20, 38),
('6B2', 'LFR', 42, 42),
('6B3', '6CSL01', 10, 12),
('6B3', '6CSL03', 11, 14),
('6B3', '6CSL04', 20, 21),
('6B3', 'LFR', 42, 42),
('6C', '6CCI01 ', 8, 42),
('6C', '6CCI02', 16, 42),
('6C', '6CS01', 7, 42),
('6C', '6CS03', 2, 42),
('6C', 'CSPE01', 5, 42),
('6C', 'CSPE08', 34, 42),
('6C', 'CSPE22', 18, 42),
('6C', 'CSPE28', 29, 42),
('6C', 'FR', 42, 42),
('6C1', '6CSL01', 37, 31),
('6C1', '6CSL03', 21, 14),
('6C1', '6CSL04', 33, 14),
('6C1', 'LFR', 42, 42),
('6C2', '6CSL01', 10, 16),
('6C2', '6CSL03', 21, 19),
('6C2', '6CSL04', 34, 2),
('6C2', 'LFR', 42, 42),
('6C3', '6CSL01', 10, 31),
('6C3', '6CSL03', 37, 35),
('6C3', '6CSL04', 20, 33),
('6C3', 'LFR', 42, 42),
('8', 'CSPE08', 24, 42),
('8', 'CSPE08', 37, 42),
('8', 'CSPE12', 12, 42),
('8', 'CSPE12', 14, 42),
('8', 'CSPE17', 28, 42),
('8', 'CSPE30', 22, 42),
('8', 'FR', 42, 42),
('M-CNE', 'AWN', 5, 42),
('M-CNE', 'CSPE08', 8, 42),
('M-CNE', 'CSPE29', 11, 42),
('M-CNE', 'DCS', 7, 42),
('M-CNE', 'FR', 42, 42),
('M-CNE', 'ON', 6, 42),
('M-CSE', 'ASE', 16, 42),
('M-CSE', 'CSPE08', 1, 42),
('M-CSE', 'CSPE13', 10, 42),
('M-CSE', 'CSPE28', 2, 42),
('M-CSE', 'FR', 42, 42),
('M-CSE', 'SC', 4, 42);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `batch`
--
ALTER TABLE `batch`
  ADD PRIMARY KEY (`batchID`,`day`,`hour`,`roomId`),
  ADD KEY `facultyId1_fk` (`facultyId1`),
  ADD KEY `facultyId2_fk` (`facultyId2`),
  ADD KEY `roomId_fk` (`roomId`),
  ADD KEY `subjectId_fk` (`subjectId`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`facultyId`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`roomId`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subjectId`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`batchID`,`subjectID`,`facultyID1`,`facultyID2`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `batch`
--
ALTER TABLE `batch`
  ADD CONSTRAINT `facultyId1_fk` FOREIGN KEY (`facultyId1`) REFERENCES `faculty` (`facultyId`),
  ADD CONSTRAINT `facultyId2_fk` FOREIGN KEY (`facultyId2`) REFERENCES `faculty` (`facultyId`),
  ADD CONSTRAINT `roomId_fk` FOREIGN KEY (`roomId`) REFERENCES `room` (`roomId`),
  ADD CONSTRAINT `subjectId_fk` FOREIGN KEY (`subjectId`) REFERENCES `subject` (`subjectId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
