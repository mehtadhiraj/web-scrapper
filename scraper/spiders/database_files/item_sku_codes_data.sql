-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2018 at 10:28 AM
-- Server version: 10.1.33-MariaDB
-- PHP Version: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scraperdb1`
--

-- --------------------------------------------------------

--
-- Table structure for table `item_sku_codes`
--

CREATE TABLE `item_sku_codes` (
  `item_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `sku_code` varchar(45) NOT NULL,
  `is_scrape_active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `item_sku_codes`
--

INSERT INTO `item_sku_codes` (`item_id`, `store_id`, `sku_code`, `is_scrape_active`) VALUES
(1, 1, 'B01K4F6SHO', 1),
(1, 2, '389683', 1),
(1, 3, '10000200', 1),
(2, 1, 'B01K4F45LU', 1),
(2, 2, '114408', 1),
(2, 3, '10000178', 1),
(3, 1, 'B01K4F4B9Q', 1),
(3, 2, '375919', 1),
(3, 3, '10000068', 1),
(4, 1, 'B01K4F55BE', 1),
(5, 1, 'B01N0L50QX', 1),
(6, 1, 'B01N4893Q0', 1),
(7, 1, 'B07DLGX4KK', 1),
(8, 1, 'B01MSTFSXA', 1),
(9, 1, 'B01K4F6N2E', 1),
(10, 1, 'B01K4F5KWS', 1),
(11, 1, 'B01K4F5KWS', 1),
(12, 1, 'B01MTUXLEQ', 1),
(13, 1, 'B07DLBXGF1', 1),
(14, 1, 'B01K4F6SHO', 1),
(15, 1, 'B01K4F4QG4', 1),
(16, 1, 'B01K4F4VXC', 1),
(17, 1, 'B01K4F4VXC', 1),
(18, 1, 'B01MQQDL4A', 1),
(19, 1, 'B01K4F72RY', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `item_sku_codes`
--
ALTER TABLE `item_sku_codes`
  ADD PRIMARY KEY (`item_id`,`store_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
