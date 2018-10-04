-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2018 at 10:48 AM
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
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `item_code` varchar(45) NOT NULL,
  `item_description` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `items`:
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
-- RELATIONSHIPS FOR TABLE `item_sku_codes`:
--

-- --------------------------------------------------------

--
-- Table structure for table `report_recipients`
--

CREATE TABLE `report_recipients` (
  `id` int(11) NOT NULL,
  `recipient_email` varchar(75) NOT NULL,
  `recipient_name` varchar(75) DEFAULT NULL,
  `is_active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `report_recipients`:
--

-- --------------------------------------------------------

--
-- Table structure for table `scrape_reports`
--

CREATE TABLE `scrape_reports` (
  `id` int(11) NOT NULL,
  `scrape_session_id` int(11) NOT NULL,
  `sku_code` varchar(45) NOT NULL,
  `store_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `item_name` varchar(150) NOT NULL,
  `stock_available` varchar(50) NOT NULL,
  `item_price` decimal(8,2) DEFAULT NULL,
  `store_rating` varchar(45) DEFAULT NULL,
  `scrape_datetime` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `scrape_reports`:
--

-- --------------------------------------------------------

--
-- Table structure for table `scrape_sessions`
--

CREATE TABLE `scrape_sessions` (
  `id` int(11) NOT NULL,
  `session_start_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `session_end_datetime` datetime DEFAULT NULL,
  `scrape_result` varchar(150) DEFAULT NULL
  `email_status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `scrape_sessions`:
--

-- --------------------------------------------------------

--
-- Table structure for table `stores`
--

CREATE TABLE `stores` (
  `id` int(11) NOT NULL,
  `store_name` varchar(45) NOT NULL,
  `base_url` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `stores`:
--

-- --------------------------------------------------------

--
-- Table structure for table `store_locations`
--

CREATE TABLE `store_locations` (
  `id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `city_area` varchar(75) NOT NULL,
  `pin_code` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `store_locations`:
--

-- --------------------------------------------------------

--
-- Table structure for table `system_users`
--

CREATE TABLE `system_users` (
  `id` int(11) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(75) NOT NULL,
  `is_active` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- RELATIONSHIPS FOR TABLE `system_users`:
--

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `item_code_UNIQUE` (`item_code`);

--
-- Indexes for table `item_sku_codes`
--
ALTER TABLE `item_sku_codes`
  ADD PRIMARY KEY (`item_id`,`store_id`);

--
-- Indexes for table `report_recipients`
--
ALTER TABLE `report_recipients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scrape_reports`
--
ALTER TABLE `scrape_reports`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scrape_sessions`
--
ALTER TABLE `scrape_sessions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stores`
--
ALTER TABLE `stores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `store_name_UNIQUE` (`store_name`);

--
-- Indexes for table `store_locations`
--
ALTER TABLE `store_locations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `city_area_UNIQUE` (`city_area`),
  ADD UNIQUE KEY `pin_code_UNIQUE` (`pin_code`);

--
-- Indexes for table `system_users`
--
ALTER TABLE `system_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `report_recipients`
--
ALTER TABLE `report_recipients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scrape_reports`
--
ALTER TABLE `scrape_reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scrape_sessions`
--
ALTER TABLE `scrape_sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `stores`
--
ALTER TABLE `stores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `store_locations`
--
ALTER TABLE `store_locations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `system_users`
--
ALTER TABLE `system_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
