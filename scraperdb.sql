-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 25, 2018 at 03:27 PM
-- Server version: 5.5.60
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scraperdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `location_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `area` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `pincode` varchar(25) NOT NULL DEFAULT 'NOT NULL'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `productdetails`
--

CREATE TABLE `productdetails` (
  `product_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `skus_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `store_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `location_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `product_name` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `product_price` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `product_stock` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `product_rating` varchar(25) NOT NULL DEFAULT 'NOT NULL'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `skus`
--

CREATE TABLE `skus` (
  `sku_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `store_id` varchar(25) NOT NULL DEFAULT 'NOT NULL'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `store_id` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `store_name` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `base_url` varchar(25) NOT NULL DEFAULT 'NOT NULL'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `location`
--
ALTER TABLE `location`
  ADD PRIMARY KEY (`location_id`),
  ADD UNIQUE KEY `area` (`area`),
  ADD UNIQUE KEY `pincode` (`pincode`);

--
-- Indexes for table `productdetails`
--
ALTER TABLE `productdetails`
  ADD PRIMARY KEY (`product_id`),
  ADD KEY `store_id` (`store_id`),
  ADD KEY `skus_id` (`skus_id`),
  ADD KEY `location_id` (`location_id`);

--
-- Indexes for table `skus`
--
ALTER TABLE `skus`
  ADD PRIMARY KEY (`sku_id`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`store_id`),
  ADD UNIQUE KEY `store_name` (`store_name`),
  ADD UNIQUE KEY `base_url` (`base_url`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `productdetails`
--
ALTER TABLE `productdetails`
  ADD CONSTRAINT `productdetails_ibfk_3` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`),
  ADD CONSTRAINT `productdetails_ibfk_1` FOREIGN KEY (`store_id`) REFERENCES `store` (`store_id`),
  ADD CONSTRAINT `productdetails_ibfk_2` FOREIGN KEY (`skus_id`) REFERENCES `skus` (`sku_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
