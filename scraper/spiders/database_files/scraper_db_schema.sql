-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 01, 2018 at 06:10 AM
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
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `item_code`, `item_description`) VALUES
(1, '96433310006', 'BESAN     1KG  FINE'),
(2, '96433230002', 'CHANA DAL 1 KG'),
(3, '96433230003', 'CHANA DAL 500 GMS'),
(4, '96443140010', 'CHICKEN MASALA 60 X 100 GMS CARTONS'),
(5, '96443140006', 'CHICKEN  MASALA 120 X 45 G CARTONS'),
(6, '96443180005', 'CHILLI POWDER 36 X 500 GM POUCH'),
(7, '96443190008', 'CHINESE CHUNTEY 24 X 100G'),
(8, '96443200005', 'CORIANDER POWDER 36 X 500 GM POUCH'),
(9, '96443200003', 'CORIANDER POWDER 90X200GM POUCH'),
(10, '96443150001', 'DAL TADKA MASALA 120 X 100 GMS CARTONS'),
(11, '96443150008', 'DAL TADKA MASALA 60 X 100 GMS CARTONS'),
(12, '96443150007', 'DAL TADKA  MASALA 120 X 45 G CARTONS'),
(13, '96443180023', 'DATE TAMARIND CHUNTEY 24 X 100G'),
(14, '96433310018', 'FINE BESAN 1KG (7 MONTHS)'),
(15, '96433310019', 'FINE BESAN 500G (7 MONTHS)'),
(16, '96443110001', 'GARAM MASALA 120 X 100 GMS CARTONS'),
(17, '96443110010', 'GARAM MASALA 60 X 100 GMS CARTONS'),
(18, '96443110007', 'GARAM  MASALA 120 X 45 G CARTONS'),
(19, '96433170002', 'KABOOLI CHANA 1 KG'),
(20, '96433170003', 'KABOOLI CHANA 500 GMS'),
(21, '96433260003', 'KALA CHANA 1KG'),
(22, '96433190011', 'KALI MASOOR 1 KG'),
(23, '96443170008', 'KITCHEN KING MASALA  60 X 100 GMS CARTON'),
(24, '96443170004', 'KITCHEN KING  MASALA 120 X 45 G CARTONS'),
(25, '96433210002', 'MASOOR DAL 1 KG'),
(26, '96433210003', 'MASOOR DAL 500 GMS'),
(27, '96433200002', 'MASOOR DAL WHOLE 1 KG'),
(28, '96433200003', 'MASOOR DAL WHOLE 500 GMS'),
(29, '96433200005', 'MASOOR WHOLE 1KG (12 MONTHS)'),
(30, '96443120010', 'MEAT MASALA 60 X 100 GMS CARTONS'),
(31, '96443120006', 'MEAT  MASALA 120 X 45 G CARTONS'),
(32, '96433240003', 'MOONG 500 GMS'),
(33, '96433250003', 'MOONG CHILKA 500 GMS'),
(34, '96433250008', 'MOONG CHILKA 500G (12 MONTHS)'),
(35, '96433220002', 'MOONG DAL 1 KG'),
(36, '96433220012', 'MOONG DAL 1KG (12 MONTHS)'),
(37, '96433220003', 'MOONG DAL 500 GMS'),
(38, '96433230006', 'ORGANIC CHANA DAL 1KG'),
(39, '96433230007', 'ORGANIC CHANA DAL 500G'),
(40, '96433190013', 'ORGANIC MASOOR DAL 500G'),
(41, '96433220008', 'ORGANIC MOONG DAL 1KG'),
(42, '96433220009', 'ORGANIC MOONG DAL 500G'),
(43, '96433110009', 'ORGANIC TOOR DAL 1KG'),
(44, '96433110010', 'ORGANIC TOOR DAL 500G'),
(45, '96433130010', 'ORGANIC URAD DAL 500G'),
(46, '96443160008', 'PANEER MASALA 60 X 100 GMS CARTONS'),
(47, '96443160003', 'PANEER  MASALA 120 X 45 G CARTONS'),
(48, '96443210008', 'PAV BHAJI MASALA 60 X 100G CARTONS'),
(49, '96443210001', 'PAV BHAJI  MASALA 120 X 100 G CARTONS'),
(50, '96443210002', 'PAV BHAJI  MASALA 120 X 45 G CARTONS'),
(51, '96443180001', 'PREMIUM CHILLI POWDER 180 X 100 GM POUCH'),
(52, '96443180003', 'PREMIUM CHILLI POWDER 90 X 200 GM POUCH'),
(53, '96443200001', 'PREMIUM CORIANDER POWDER 180 X 100 GM PO'),
(54, '96443190001', 'PREMIUM TURMERIC POWDER 180 X 100 GM POU'),
(55, '96443190003', 'PREMIUM TURMERIC POWDER 90 X 200 GM POUC'),
(56, '96443130001', 'PUNJABI CHHOLE MASALA 120 X 100 GMS CTN.'),
(57, '96443130008', 'PUNJABI CHHOLE MASALA 60 X 100 GMS CARTO'),
(58, '96443130007', 'PUNJABI CHHOLE  MASALA 120 X 45 G CARTON'),
(59, '96433180006', 'RAJMA  CHITRA  500 GM'),
(60, '95429130004', 'Tata  Salt Sprinkler 25 x 100 gm'),
(61, '96429110002', 'Tata Lite Salt Packed 50 X 1 kg'),
(62, '95429120018', 'TATA SALT 1 KG PET JAR- 15 X 1 KG'),
(63, '96429630001', 'TATA SALT BLACK SALT CRUSHER- 30 X 100 G'),
(64, '96429630002', 'TATA SALT BLACK SALT REFILL POUCH- 50 X'),
(65, '95429140004', 'Tata Salt Lite Sprinkler 25 x 100 gm'),
(66, '95429120001', 'Tata Salt Packed 50 x 1 kg'),
(67, '95429120021', 'TATA SALT PACKED 50 X 1 KG (MRP 19)'),
(68, '96429640003', 'TATA SALT ROCK SALT 16 X 500 G'),
(69, '96429640004', 'TATA SALT ROCK SALT 24 X 200 G'),
(70, '96429640001', 'TATA SALT ROCK SALT CRUSHER- 30 X 100 G'),
(71, '96429640002', 'TATA SALT ROCK SALT REFILL POUCH- 50 X 1'),
(72, '96433350003', 'TATA SAMPANN MG CHILLA MIX 24X180G'),
(73, '96433350001', 'TATA SAMPANN MG KHICHDI MIX 24X200G'),
(74, '96433350002', 'TATA SAMPANN MOONGDAL CHILLA MIX 24X180G'),
(75, '96433350004', 'TATA SAMPANN PAKODA MIX 24X180G'),
(76, '96443190007', 'TOMATO CHUNTEY 24 X 100G'),
(77, '96433110001', 'Toor Dal 1 Kg'),
(78, '96433110002', 'TOOR DAL 500 GMS'),
(79, '96443190005', 'TURMERIC POWDER 36 X 500 GM POUCH'),
(80, '96433140002', 'URAD  DAL KALI    1 KG PACKED'),
(81, '96433140003', 'URAD  DAL KALI   500 GMS PACKED'),
(82, '96433130006', 'URAD DAL 1 KG'),
(83, '96433130014', 'URAD DAL 1KG (12 MONTHS)'),
(84, '96433130007', 'URAD DAL 500 GMS'),
(85, '96433130017', 'URAD DAL 500G (12 MONTHS)'),
(86, '96433130003', 'URAD DAL WHOLE 1 KG'),
(87, '96433130004', 'URAD DAL WHOLE 500 GMS'),
(88, '96433130015', 'URAD WHOLE 1KG (9 MONTHS)'),
(89, '96443140011', 'WEST CHICKEN MASALA 60 X 100 GMS CARTONS'),
(90, '96443140009', 'WEST CHICKEN  MASALA 120 X 45 GMS CARTON'),
(91, '96443110011', 'WEST GARAM MASALA 60 X 100 GMS CARTONS'),
(92, '96443110009', 'WEST GARAM  MASALA 120 X 45 G CARTONS'),
(93, '96443120011', 'WEST MEAT MASALA 60 X 100 GMS CARTONS');

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
(19, 1, 'B01K4F72RY', 1),
(20, 1, 'B01K4F7IWS', 1),
(21, 1, 'B01K4F78NC', 1),
(22, 1, 'B01K4F7DMS', 1),
(23, 1, 'B01K4F59E2', 1),
(24, 1, 'B01MXSK7QM', 1),
(25, 1, 'B01HBFXGO8', 1),
(26, 1, 'B01K4F40JW', 1),
(27, 1, 'B01K4F4G4Q', 1),
(28, 1, 'B01K4F4L96', 1),
(29, 1, 'B01K4F4G4Q', 1),
(30, 1, 'B01K4F50P0', 1),
(31, 1, 'B01MQQDJ2K', 1),
(32, 1, 'B01K4F3S72', 1),
(33, 1, 'B01K4F3W00', 1),
(34, 1, 'B01K4F3W00', 1),
(35, 1, 'B01K4F3NPE', 1),
(36, 1, 'B01K4F3NPE', 1),
(37, 1, 'B01HBFVM94', 1),
(38, 1, 'B07BGC43KD', 1),
(39, 1, 'B07BGC5C1Z', 1),
(40, 1, 'B07BGCZCB3', 1),
(41, 1, 'B07BGCB6M7', 1),
(42, 1, 'B07BGC61TC', 1),
(43, 1, 'B07BGCNMBB', 1),
(44, 1, 'B07BGCWY83', 1),
(45, 1, 'B07BGD2283', 1),
(46, 1, 'B01K4F5R3K', 1),
(47, 1, 'B01N7CJHBT', 1),
(48, 1, 'B01N59O6RL', 1),
(49, 1, 'B01N59O6RL', 1),
(50, 1, 'B01MRRRUJK', 1),
(51, 1, 'B01K4F5WI0', 1),
(52, 1, 'B01K4F6HJ8', 1),
(53, 1, 'B01K4F66YY', 1),
(54, 1, 'B01K4F62HK', 1),
(55, 1, 'B01K4F6CBG', 1),
(56, 1, 'B01K4F5FIC', 1),
(57, 1, 'B01K4F5FIC', 1),
(58, 11, 'B01N9BWYQS', 1),
(59, 1, 'B01K4F7QWU', 1),
(60, 1, 'B01K4F2DQO', 1),
(61, 1, 'B01HBEUAI4', 1),
(62, 1, 'B01N0GN72Y', 1),
(63, 1, 'B01K4F2TN6', 1),
(64, 1, 'B01K4F2XVO', 1),
(65, 1, 'XXXXX', 0),
(66, 1, 'B01HBF5WBI', 1),
(67, 1, 'B01HBF5WBI', 1),
(68, 1, 'B078SFTDTY', 1),
(69, 1, 'B078SDRVXY', 1),
(70, 1, 'B01K4F3264', 1),
(71, 1, 'B01N6MVEN4', 1),
(72, 1, 'B07B6H75SQ', 1),
(73, 1, 'B078SFQVBR', 1),
(74, 1, 'B07B6H751L', 1),
(75, 1, 'XXXXX', 0),
(76, 1, 'B07DLMRVBY', 1),
(77, 1, 'B01HBEQ006', 1),
(78, 1, 'B01K4F3IVS', 1),
(79, 1, 'B01NBEWANN', 1),
(80, 1, 'B01K4F3APM', 1),
(81, 1, 'B01K4F3EYO', 1),
(82, 1, 'B01HBFTGPQ', 1),
(83, 1, 'B01HBFTGPQ', 1),
(84, 1, 'B01HBFUCTA', 1),
(85, 1, 'B01HBFUCTA', 1),
(86, 1, 'B01HBFSSUK', 1),
(87, 1, 'B01HBFXKO4', 1),
(88, 1, 'B01HBFSSUK', 1),
(89, 1, 'B01K4F55BE', 1),
(90, 1, 'B01N0L50QX', 1),
(91, 1, 'B01K4F4VXC', 1),
(92, 1, 'B01MQQDL4A', 1),
(93, 1, 'B01K4F50P0', 1);

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
-- Dumping data for table `report_recipients`
--

INSERT INTO `report_recipients` (`id`, `recipient_email`, `recipient_name`, `is_active`) VALUES
(1, 'vivek.iyer16@siesgst.ac.in', 'Vivek Iyer', 1),
(2, 'karthikmudaliar13@gmail.com', 'Karthik Mudaliar', 1);

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
  `item_name` varchar(50) NOT NULL,
  `stock_available` varchar(50) NOT NULL,
  `item_price` decimal(8,2) DEFAULT NULL,
  `store_rating` varchar(45) DEFAULT NULL,
  `scrape_datetime` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scrape_reports`
--

INSERT INTO `scrape_reports` (`id`, `scrape_session_id`, `sku_code`, `store_id`, `location_id`, `item_name`, `stock_available`, `item_price`, `store_rating`, `scrape_datetime`) VALUES
(1305, 379, '10000200', 3, 3, 'Fresho Tomato Hybrid/Tomato Sankarit, 1 kg ', 'Available', '17.90', 'Not Applicable', '2018-09-30 18:38:39'),
(1306, 379, '10000200', 3, 3, 'Fresho Tomato Hybrid/Tomato Sankarit, 500 gm ', 'Available', '9.95', 'Not Applicable', '2018-09-30 18:38:41'),
(1307, 379, '10000200', 3, 3, 'Fresho Tomato - Hybrid, 2 kg ', 'Available', '33.80', 'Not Applicable', '2018-09-30 18:38:42'),
(1308, 379, '10000178', 3, 3, 'Fresho Sambhar Onion - Grade A/Sambhar Kanda - Gra', 'Available', '34.00', 'Not Applicable', '2018-09-30 18:39:04'),
(1309, 379, '10000178', 3, 3, 'Fresho Sambhar Onion - Grade A/Sambhar Kanda - Gra', 'Available', '119.00', 'Not Applicable', '2018-09-30 18:39:06'),
(1310, 379, '10000178', 3, 3, 'Fresho Sambhar Onion - Grade A/Sambhar Kanda - Gra', 'Available', '62.00', 'Not Applicable', '2018-09-30 18:39:10'),
(1311, 379, '10000068', 3, 3, 'Fresho Capsicum Hybrid Green/Sankarit Dhobli Mirch', 'Available', '14.00', 'Not Applicable', '2018-09-30 18:39:32'),
(1312, 379, '10000068', 3, 3, 'Fresho Capsicum Hybrid Green/Sankarit Dhobli Mirch', 'Available', '55.00', 'Not Applicable', '2018-09-30 18:39:33'),
(1313, 379, '10000068', 3, 3, 'Fresho Capsicum Hybrid Green/Sankarit Dhobli Mirch', 'Available', '28.00', 'Not Applicable', '2018-09-30 18:39:34'),
(1314, 379, 'B01K4F2TN6', 1, 1, 'Tata Salt Black Salt, 100g', 'In Stock.', '104.00', 'Not applicable', '2018-09-30 18:40:40'),
(1315, 379, 'B01N0GN72Y', 1, 1, 'Tata Salt Pet Jar, 1kg', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:40:42'),
(1316, 379, 'B01K4F3NPE', 1, 1, 'Tata Sampann Moong Dal Split, 1kg', 'In Stock.', '105.00', '4.0 out of 5 stars', '2018-09-30 18:40:43'),
(1317, 379, 'B01N6MVEN4', 1, 1, 'Tata Salt Refill Pack, Black Salt, 100g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:40:44'),
(1318, 379, '389683', 2, 2, 'Grofers Mother\'s Choice Raw Peanuts', 'Curently Unavailable', '66.00', 'Not Applicable', '2018-09-30 18:40:44'),
(1319, 379, 'B01N4893Q0', 1, 1, 'Tata Sampann Chilli Powder, 500g', 'In Stock.', '145.00', 'Not applicable', '2018-09-30 18:40:45'),
(1320, 379, 'B01HBF5WBI', 1, 1, 'Tata Salt, 1kg', 'In Stock.', '16.00', '4.2 out of 5 stars', '2018-09-30 18:40:45'),
(1321, 379, 'B01K4F5KWS', 1, 1, 'Tata Sampann Dal Tadka Masala, 100g', 'In Stock.', '48.00', 'Not applicable', '2018-09-30 18:40:46'),
(1322, 379, '375919', 2, 2, 'Dhuli Moong Dal', '1 kg', '81.00', 'Not Applicable', '2018-09-30 18:40:46'),
(1323, 379, 'B01HBFXGO8', 1, 1, 'Tata Sampann Masoor Dal Split, 1kg', 'In Stock.', '85.00', '4.0 out of 5 stars', '2018-09-30 18:40:47'),
(1324, 379, 'B07DLGX4KK', 1, 1, 'Tata Sampann Chinese Chutney, 100g', 'In Stock.', '50.00', 'Not applicable', '2018-09-30 18:40:47'),
(1325, 379, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 18:40:47'),
(1326, 379, 'B01K4F3264', 1, 1, 'Tata Rock Salt, 100g', 'In Stock.', '117.00', 'Not applicable', '2018-09-30 18:40:47'),
(1327, 379, 'B01K4F4L96', 1, 1, 'Tata Sampann Masoor Dal, Whole, 500g', 'In Stock.', '43.00', 'Not applicable', '2018-09-30 18:40:48'),
(1328, 379, 'B01K4F2XVO', 1, 1, 'Tata Salt Refill Black Salt, 100g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:40:48'),
(1329, 379, 'B01HBFSSUK', 1, 1, 'Tata Sampann Urad Whole, 1kg', 'In Stock.', '94.00', '3.9 out of 5 stars', '2018-09-30 18:40:49'),
(1330, 379, 'B01K4F5WI0', 1, 1, 'Tata Sampann Chilli Powder Masala, 100g', 'In Stock.', '25.00', '3.9 out of 5 stars', '2018-09-30 18:40:49'),
(1331, 379, 'B01K4F4QG4', 1, 1, 'Tata Sampann Besan, 500g', 'In Stock.', '46.00', '3.8 out of 5 stars', '2018-09-30 18:40:50'),
(1332, 379, 'B01HBFSSUK', 1, 1, 'Tata Sampann Urad Whole, 1kg', 'In Stock.', '94.00', '3.9 out of 5 stars', '2018-09-30 18:40:50'),
(1333, 379, 'B01K4F6SHO', 1, 1, 'Tata Sampann Besan, 1kg', 'In Stock.', '90.00', 'Not applicable', '2018-09-30 18:40:50'),
(1334, 379, '114408', 2, 2, 'Satyam Peanuts', '500 gm', '75.00', 'Not Applicable', '2018-09-30 18:40:51'),
(1335, 379, 'B01K4F4B9Q', 1, 1, 'Tata Sampann Chana Dal, 500g', 'Currently Unavailable.', '0.00', '4.2 out of 5 stars', '2018-09-30 18:40:51'),
(1336, 379, 'B07BGCNMBB', 1, 1, 'Tata Sampann Organic Toor Dal, 1kg', 'In Stock.', '144.00', 'Not applicable', '2018-09-30 18:40:51'),
(1337, 379, 'B07BGC5C1Z', 1, 1, 'Tata Sampann Organic Chana Dal, 500g', 'In Stock.', '68.00', 'Not applicable', '2018-09-30 18:40:51'),
(1338, 379, 'B01MTUXLEQ', 1, 1, 'Tata Sampann Dal Tadka Masala, 45g', 'In Stock.', '32.00', '4.0 out of 5 stars', '2018-09-30 18:40:52'),
(1339, 379, 'B01K4F59E2', 1, 1, 'Tata Sampann Kitchen King Masala, 100g', 'In Stock.', '56.00', '3.8 out of 5 stars', '2018-09-30 18:40:52'),
(1340, 379, 'B01HBEUAI4', 1, 1, 'Tata Salt Lite, Low Sodium, 1kg', 'In Stock.', '28.00', 'Not applicable', '2018-09-30 18:40:52'),
(1341, 379, 'B01K4F45LU', 1, 1, 'Tata Sampann Chana Dal, 1kg', 'In Stock.', '86.00', '3.9 out of 5 stars', '2018-09-30 18:40:53'),
(1342, 379, 'B01HBFXKO4', 1, 1, 'Tata Sampann Urad Whole, 500g', 'In Stock.', '50.00', 'Not applicable', '2018-09-30 18:40:53'),
(1343, 379, 'B01K4F7QWU', 1, 1, 'Tata Sampann Rajma, 500g', 'In Stock.', '75.00', '4.2 out of 5 stars', '2018-09-30 18:40:53'),
(1344, 379, 'B01HBFUCTA', 1, 1, 'Tata Sampann Urad Dal Split, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 18:40:53'),
(1345, 379, 'B01MQQDL4A', 1, 1, 'Tata Sampann Garam Masala, 45g', 'In Stock.', '40.00', 'Not applicable', '2018-09-30 18:40:54'),
(1346, 379, 'B01MQQDJ2K', 1, 1, 'Tata Sampann Meat Masala, 45g', 'In Stock.', '38.00', '4.2 out of 5 stars', '2018-09-30 18:40:54'),
(1347, 379, 'B07BGC61TC', 1, 1, 'Tata Sampann Organic Moong Dal, 500g', 'In Stock.', '79.00', '3.8 out of 5 stars', '2018-09-30 18:40:54'),
(1348, 379, 'B01K4F6N2E', 1, 1, 'Tata Sampann Coriander Powder Masala, 200g', 'In Stock.', '50.00', '4.0 out of 5 stars', '2018-09-30 18:40:54'),
(1349, 379, 'B01K4F50P0', 1, 1, 'Tata Sampann Meat Masala, 100g', 'In Stock.', '72.00', 'Not applicable', '2018-09-30 18:40:55'),
(1350, 379, 'B07B6H75SQ', 1, 1, 'Tata Sampann Multigrain Chilla Mix, 180g', 'In Stock.', '56.00', 'Not applicable', '2018-09-30 18:40:55'),
(1351, 379, 'B01K4F5KWS', 1, 1, 'Tata Sampann Dal Tadka Masala, 100g', 'In Stock.', '48.00', 'Not applicable', '2018-09-30 18:40:55'),
(1352, 379, 'B07BGC43KD', 1, 1, 'Tata Sampann Organic Chana Dal, 1kg', 'In Stock.', '135.00', 'Not applicable', '2018-09-30 18:40:55'),
(1353, 379, 'B07BGCZCB3', 1, 1, 'Tata Sampann Organic Masoor Dal, 500g', 'In Stock.', '69.00', 'Not applicable', '2018-09-30 18:40:55'),
(1354, 379, 'B01K4F3IVS', 1, 1, 'Tata Sampann Toor Dal, 500g', 'In Stock.', '45.00', 'Not applicable', '2018-09-30 18:40:56'),
(1355, 379, 'B01MSTFSXA', 1, 1, 'Tata Sampann Coriander Powder, 500g', 'In Stock.', '120.00', '4.2 out of 5 stars', '2018-09-30 18:40:56'),
(1356, 379, 'B01K4F3NPE', 1, 1, 'Tata Sampann Moong Dal Split, 1kg', 'In Stock.', '105.00', '4.0 out of 5 stars', '2018-09-30 18:40:56'),
(1357, 379, 'B07DLBXGF1', 1, 1, 'Tata Sampann Tamarind Date Chutney, 100g', 'In Stock.', '44.00', 'Not applicable', '2018-09-30 18:40:57'),
(1358, 379, 'B01K4F3W00', 1, 1, 'Tata Sampann Moong Chilka, 500g', 'In Stock.', '53.00', '4.2 out of 5 stars', '2018-09-30 18:40:57'),
(1359, 379, 'B01K4F2DQO', 1, 1, 'Tata Salt Lite Sprinkler, 100g', 'In Stock.', '18.00', 'Not applicable', '2018-09-30 18:40:57'),
(1360, 379, 'B07DLMRVBY', 1, 1, 'Tata Sampann Tomato Chutney, 100g', 'In Stock.', '44.00', '4.2 out of 5 stars', '2018-09-30 18:40:57'),
(1361, 379, 'B01K4F3EYO', 1, 1, 'Tata Sampann Urad Kali, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 18:40:57'),
(1362, 379, 'B01MQQDL4A', 1, 1, 'Tata Sampann Garam Masala, 45g', 'In Stock.', '40.00', 'Not applicable', '2018-09-30 18:40:57'),
(1363, 379, 'B01HBFTGPQ', 1, 1, 'Tata Sampann Urad Dal Split, 1kg', 'In Stock.', '98.00', '4.1 out of 5 stars', '2018-09-30 18:40:58'),
(1364, 379, 'B01N7CJHBT', 1, 1, 'Tata Sampann Paneer Masala, 45g', 'Currently Unavailable.', '0.00', '3.8 out of 5 stars', '2018-09-30 18:40:58'),
(1365, 379, 'B01K4F5FIC', 1, 1, 'Tata Sampann Punjabi Chhole Masala, 100g', 'In Stock.', '64.00', '4.2 out of 5 stars', '2018-09-30 18:40:58'),
(1366, 379, 'B01K4F4G4Q', 1, 1, 'Tata Sampann Masoor Dal, Whole, 1kg', 'In Stock.', '81.00', 'Not applicable', '2018-09-30 18:40:58'),
(1367, 379, 'B07BGCB6M7', 1, 1, 'Tata Sampann Organic Moong Dal, 1kg', 'In Stock.', '154.00', 'Not applicable', '2018-09-30 18:40:59'),
(1368, 379, 'B01K4F6SHO', 1, 1, 'Tata Sampann Besan, 1kg', 'In Stock.', '90.00', 'Not applicable', '2018-09-30 18:40:59'),
(1369, 379, 'B01K4F40JW', 1, 1, 'Tata Sampann Masoor Dal Split, 500g', 'In Stock.', '43.00', 'Not applicable', '2018-09-30 18:40:59'),
(1370, 379, 'B078SFTDTY', 1, 1, 'Tata Rock Salt, 500g', 'In Stock.', '57.00', 'Not applicable', '2018-09-30 18:40:59'),
(1371, 379, 'B01K4F7IWS', 1, 1, 'Tata Sampann Kabuli, 500g', 'In Stock.', '65.00', '3.9 out of 5 stars', '2018-09-30 18:40:59'),
(1372, 379, 'B01MRRRUJK', 1, 1, 'Tata Sampann Pav Bhaji Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:41:00'),
(1373, 379, 'B01N0L50QX', 1, 1, 'Tata Sampann Chicken Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:41:00'),
(1374, 379, 'B01N59O6RL', 1, 1, 'Tata Sampann Pav Bhaji Masala, 100g', 'In Stock.', '71.00', 'Not applicable', '2018-09-30 18:41:01'),
(1375, 379, 'B01K4F62HK', 1, 1, 'Tata Sampann Turmeric Powder Masala, 100g', 'In Stock.', '24.00', 'Not applicable', '2018-09-30 18:41:01'),
(1376, 379, 'B01K4F55BE', 1, 1, 'Tata Sampann Chicken Masala, 100g', 'Currently Unavailable.', '0.00', '4.1 out of 5 stars', '2018-09-30 18:41:01'),
(1377, 379, 'B01N0L50QX', 1, 1, 'Tata Sampann Chicken Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:41:02'),
(1378, 379, 'B01HBFVM94', 1, 1, 'Tata Sampann Moong Dal Split, 500g', 'In Stock.', '54.00', 'Not applicable', '2018-09-30 18:41:02'),
(1379, 379, 'B01K4F66YY', 1, 1, 'Tata Sampann Coriander Powder Masala, 100g', 'In Stock.', '25.00', 'Not applicable', '2018-09-30 18:41:02'),
(1380, 379, 'B078SFQVBR', 1, 1, 'Tata Sampann  Multigrain Khichdi, 200g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:41:02'),
(1381, 379, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 18:41:02'),
(1382, 379, 'B01HBEQ006', 1, 1, 'Tata Sampann Pulses Toor Dal, 1kg', 'In Stock.', '90.00', '4.1 out of 5 stars', '2018-09-30 18:41:03'),
(1383, 379, 'B01K4F6CBG', 1, 1, 'Tata Sampann Turmeric Powder Masala, 200g', 'In Stock.', '42.00', 'Not applicable', '2018-09-30 18:41:03'),
(1384, 379, 'B01K4F5R3K', 1, 1, 'Tata Sampann Paneer Masala, 100g', 'In Stock.', '66.00', 'Not applicable', '2018-09-30 18:41:03'),
(1385, 379, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 18:41:04'),
(1386, 379, 'B01K4F5FIC', 1, 1, 'Tata Sampann Punjabi Chhole Masala, 100g', 'In Stock.', '64.00', '4.2 out of 5 stars', '2018-09-30 18:41:04'),
(1387, 379, 'B01HBF5WBI', 1, 1, 'Tata Salt, 1kg', 'In Stock.', '16.00', '4.2 out of 5 stars', '2018-09-30 18:41:04'),
(1388, 379, 'B01K4F7DMS', 1, 1, 'Tata Sampann Kali Masoor, 1kg', 'In Stock.', '89.00', 'Not applicable', '2018-09-30 18:41:04'),
(1389, 379, 'B01MXSK7QM', 1, 1, 'Tata Sampann Kitchen King Masala, 45g', 'In Stock.', '28.00', 'Not applicable', '2018-09-30 18:41:05'),
(1390, 379, 'B01NBEWANN', 1, 1, 'Tata Sampann Turmeric Powder, 500g', 'In Stock.', '112.00', 'Not applicable', '2018-09-30 18:41:05'),
(1391, 379, 'B01K4F55BE', 1, 1, 'Tata Sampann Chicken Masala, 100g', 'Currently Unavailable.', '0.00', '4.1 out of 5 stars', '2018-09-30 18:41:05'),
(1392, 379, 'B01HBFUCTA', 1, 1, 'Tata Sampann Urad Dal Split, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 18:41:05'),
(1393, 379, 'B07B6H751L', 1, 1, 'Tata Sampann Moong Dal Chilla Mix, 180g', 'In Stock.', '56.00', 'Not applicable', '2018-09-30 18:41:05'),
(1394, 379, 'B01N59O6RL', 1, 1, 'Tata Sampann Pav Bhaji Masala, 100g', 'In Stock.', '71.00', 'Not applicable', '2018-09-30 18:41:06'),
(1395, 379, 'B01HBFTGPQ', 1, 1, 'Tata Sampann Urad Dal Split, 1kg', 'In Stock.', '98.00', '4.1 out of 5 stars', '2018-09-30 18:41:06'),
(1396, 379, 'B01K4F6HJ8', 1, 1, 'Tata Sampann Chilli Powder Masala, 200g', 'In Stock.', '60.00', 'Not applicable', '2018-09-30 18:41:06'),
(1397, 379, 'B07BGD2283', 1, 1, 'Tata Sampann Organic Urad Dal, 500g', 'In Stock.', '68.00', 'Not applicable', '2018-09-30 18:41:06'),
(1398, 379, 'B07BGCWY83', 1, 1, 'Tata Sampann Organic Toor Dal, 500g', 'In Stock.', '73.00', 'Not applicable', '2018-09-30 18:41:07'),
(1399, 379, 'B01K4F50P0', 1, 1, 'Tata Sampann Meat Masala, 100g', 'In Stock.', '72.00', 'Not applicable', '2018-09-30 18:41:07'),
(1400, 379, 'B01K4F3APM', 1, 1, 'Tata Sampann Urad Kali, 1kg', 'In Stock.', '91.00', 'Not applicable', '2018-09-30 18:41:07'),
(1401, 379, 'B01K4F3S72', 1, 1, 'Tata Sampann Green Moong, Whole, 500g', 'In Stock.', '52.00', '3.9 out of 5 stars', '2018-09-30 18:41:07'),
(1402, 379, 'B01K4F3W00', 1, 1, 'Tata Sampann Moong Chilka, 500g', 'In Stock.', '53.00', '4.2 out of 5 stars', '2018-09-30 18:41:08'),
(1403, 379, 'B01K4F4G4Q', 1, 1, 'Tata Sampann Masoor Dal, Whole, 1kg', 'In Stock.', '81.00', 'Not applicable', '2018-09-30 18:41:08'),
(1404, 379, 'B078SDRVXY', 1, 1, 'Tata Rock Salt, 200g', 'In Stock.', '30.00', '4.1 out of 5 stars', '2018-09-30 18:41:08'),
(1405, 379, 'B01K4F72RY', 1, 1, 'Tata Sampann Kabuli, 1kg', 'In Stock.', '129.00', '3.9 out of 5 stars', '2018-09-30 18:41:09'),
(1406, 379, 'B01K4F78NC', 1, 1, 'Tata Sampann Kala Chana, 1kg', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 18:41:22'),
(1407, 380, '114408', 2, 2, 'Satyam Peanuts', '500 gm', '66.00', 'Not Applicable', '2018-09-30 19:07:26'),
(1408, 380, 'B01K4F78NC', 1, 1, 'Tata Sampann Kala Chana, 1kg', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:31'),
(1409, 380, 'B01K4F45LU', 1, 1, 'Tata Sampann Chana Dal, 1kg', 'In Stock.', '86.00', '3.9 out of 5 stars', '2018-09-30 19:07:31'),
(1410, 380, 'B078SFQVBR', 1, 1, 'Tata Sampann  Multigrain Khichdi, 200g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:32'),
(1411, 380, 'B01N0L50QX', 1, 1, 'Tata Sampann Chicken Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:32'),
(1412, 380, 'B01K4F6SHO', 1, 1, 'Tata Sampann Besan, 1kg', 'In Stock.', '90.00', 'Not applicable', '2018-09-30 19:07:32'),
(1413, 380, '375919', 2, 2, 'Dhuli Moong Dal', '1 kg', '81.00', 'Not Applicable', '2018-09-30 19:07:33'),
(1414, 380, '389683', 2, 2, 'Grofers Mother\'s Choice Raw Peanuts', 'Curently Unavailable', '66.00', 'Not Applicable', '2018-09-30 19:07:34'),
(1415, 380, 'B01MQQDL4A', 1, 1, 'Tata Sampann Garam Masala, 45g', 'In Stock.', '40.00', 'Not applicable', '2018-09-30 19:07:35'),
(1416, 380, 'B01K4F4L96', 1, 1, 'Tata Sampann Masoor Dal, Whole, 500g', 'In Stock.', '43.00', 'Not applicable', '2018-09-30 19:07:35'),
(1417, 380, 'B01K4F2TN6', 1, 1, 'Tata Salt Black Salt, 100g', 'In Stock.', '104.00', 'Not applicable', '2018-09-30 19:07:35'),
(1418, 380, 'B07BGCZCB3', 1, 1, 'Tata Sampann Organic Masoor Dal, 500g', 'In Stock.', '69.00', 'Not applicable', '2018-09-30 19:07:36'),
(1419, 380, 'B01K4F4B9Q', 1, 1, 'Tata Sampann Chana Dal, 500g', 'Currently Unavailable.', '0.00', '4.2 out of 5 stars', '2018-09-30 19:07:37'),
(1420, 380, 'B07BGCNMBB', 1, 1, 'Tata Sampann Organic Toor Dal, 1kg', 'In Stock.', '144.00', 'Not applicable', '2018-09-30 19:07:37'),
(1421, 380, 'B01HBFTGPQ', 1, 1, 'Tata Sampann Urad Dal Split, 1kg', 'In Stock.', '98.00', '4.1 out of 5 stars', '2018-09-30 19:07:37'),
(1422, 380, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 19:07:38'),
(1423, 380, 'B07DLGX4KK', 1, 1, 'Tata Sampann Chinese Chutney, 100g', 'In Stock.', '50.00', 'Not applicable', '2018-09-30 19:07:38'),
(1424, 380, 'B01K4F2XVO', 1, 1, 'Tata Salt Refill Black Salt, 100g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:38'),
(1425, 380, 'B078SFTDTY', 1, 1, 'Tata Rock Salt, 500g', 'In Stock.', '57.00', 'Not applicable', '2018-09-30 19:07:38'),
(1426, 380, 'B01MQQDJ2K', 1, 1, 'Tata Sampann Meat Masala, 45g', 'In Stock.', '38.00', '4.2 out of 5 stars', '2018-09-30 19:07:39'),
(1427, 380, 'B07DLBXGF1', 1, 1, 'Tata Sampann Tamarind Date Chutney, 100g', 'In Stock.', '44.00', 'Not applicable', '2018-09-30 19:07:41'),
(1428, 380, 'B01HBFVM94', 1, 1, 'Tata Sampann Moong Dal Split, 500g', 'In Stock.', '54.00', 'Not applicable', '2018-09-30 19:07:41'),
(1429, 380, 'B01K4F59E2', 1, 1, 'Tata Sampann Kitchen King Masala, 100g', 'In Stock.', '56.00', '3.8 out of 5 stars', '2018-09-30 19:07:42'),
(1430, 380, 'B01K4F3EYO', 1, 1, 'Tata Sampann Urad Kali, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 19:07:42'),
(1431, 380, 'B01K4F40JW', 1, 1, 'Tata Sampann Masoor Dal Split, 500g', 'In Stock.', '43.00', 'Not applicable', '2018-09-30 19:07:42'),
(1432, 380, 'B01HBFSSUK', 1, 1, 'Tata Sampann Urad Whole, 1kg', 'In Stock.', '94.00', '3.9 out of 5 stars', '2018-09-30 19:07:43'),
(1433, 380, 'B01K4F3W00', 1, 1, 'Tata Sampann Moong Chilka, 500g', 'In Stock.', '53.00', '4.2 out of 5 stars', '2018-09-30 19:07:43'),
(1434, 380, 'B07BGC43KD', 1, 1, 'Tata Sampann Organic Chana Dal, 1kg', 'In Stock.', '135.00', 'Not applicable', '2018-09-30 19:07:43'),
(1435, 380, 'B01HBFTGPQ', 1, 1, 'Tata Sampann Urad Dal Split, 1kg', 'In Stock.', '98.00', '4.1 out of 5 stars', '2018-09-30 19:07:43'),
(1436, 380, 'B01K4F6N2E', 1, 1, 'Tata Sampann Coriander Powder Masala, 200g', 'In Stock.', '50.00', '4.0 out of 5 stars', '2018-09-30 19:07:44'),
(1437, 380, 'B01HBFXKO4', 1, 1, 'Tata Sampann Urad Whole, 500g', 'In Stock.', '50.00', 'Not applicable', '2018-09-30 19:07:44'),
(1438, 380, 'B07BGC5C1Z', 1, 1, 'Tata Sampann Organic Chana Dal, 500g', 'In Stock.', '68.00', 'Not applicable', '2018-09-30 19:07:45'),
(1439, 380, 'B01K4F7DMS', 1, 1, 'Tata Sampann Kali Masoor, 1kg', 'In Stock.', '89.00', 'Not applicable', '2018-09-30 19:07:45'),
(1440, 380, 'B01K4F3NPE', 1, 1, 'Tata Sampann Moong Dal Split, 1kg', 'In Stock.', '105.00', '4.0 out of 5 stars', '2018-09-30 19:07:45'),
(1441, 380, 'B01K4F72RY', 1, 1, 'Tata Sampann Kabuli, 1kg', 'In Stock.', '129.00', '3.9 out of 5 stars', '2018-09-30 19:07:45'),
(1442, 380, 'B01MSTFSXA', 1, 1, 'Tata Sampann Coriander Powder, 500g', 'In Stock.', '120.00', '4.2 out of 5 stars', '2018-09-30 19:07:46'),
(1443, 380, 'B01K4F66YY', 1, 1, 'Tata Sampann Coriander Powder Masala, 100g', 'In Stock.', '25.00', 'Not applicable', '2018-09-30 19:07:46'),
(1444, 380, 'B01N6MVEN4', 1, 1, 'Tata Salt Refill Pack, Black Salt, 100g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:46'),
(1445, 380, 'B01MRRRUJK', 1, 1, 'Tata Sampann Pav Bhaji Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:47'),
(1446, 380, 'B01K4F5FIC', 1, 1, 'Tata Sampann Punjabi Chhole Masala, 100g', 'In Stock.', '64.00', '4.2 out of 5 stars', '2018-09-30 19:07:47'),
(1447, 380, 'B01K4F7IWS', 1, 1, 'Tata Sampann Kabuli, 500g', 'In Stock.', '65.00', '3.9 out of 5 stars', '2018-09-30 19:07:47'),
(1448, 380, 'B01K4F4G4Q', 1, 1, 'Tata Sampann Masoor Dal, Whole, 1kg', 'In Stock.', '81.00', 'Not applicable', '2018-09-30 19:07:47'),
(1449, 380, 'B01HBF5WBI', 1, 1, 'Tata Salt, 1kg', 'In Stock.', '16.00', '4.2 out of 5 stars', '2018-09-30 19:07:47'),
(1450, 380, 'B01N59O6RL', 1, 1, 'Tata Sampann Pav Bhaji Masala, 100g', 'In Stock.', '71.00', 'Not applicable', '2018-09-30 19:07:48'),
(1451, 380, 'B01K4F3S72', 1, 1, 'Tata Sampann Green Moong, Whole, 500g', 'In Stock.', '52.00', '3.9 out of 5 stars', '2018-09-30 19:07:48'),
(1452, 380, 'B01HBEQ006', 1, 1, 'Tata Sampann Pulses Toor Dal, 1kg', 'In Stock.', '90.00', '4.1 out of 5 stars', '2018-09-30 19:07:48'),
(1453, 380, 'B07BGD2283', 1, 1, 'Tata Sampann Organic Urad Dal, 500g', 'In Stock.', '68.00', 'Not applicable', '2018-09-30 19:07:48'),
(1454, 380, 'B01MTUXLEQ', 1, 1, 'Tata Sampann Dal Tadka Masala, 45g', 'In Stock.', '32.00', '4.0 out of 5 stars', '2018-09-30 19:07:48'),
(1455, 380, 'B01K4F62HK', 1, 1, 'Tata Sampann Turmeric Powder Masala, 100g', 'In Stock.', '24.00', 'Not applicable', '2018-09-30 19:07:49'),
(1456, 380, 'B01HBFUCTA', 1, 1, 'Tata Sampann Urad Dal Split, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 19:07:49'),
(1457, 380, 'B01K4F4QG4', 1, 1, 'Tata Sampann Besan, 500g', 'In Stock.', '46.00', '3.8 out of 5 stars', '2018-09-30 19:07:49'),
(1458, 380, 'B01HBEUAI4', 1, 1, 'Tata Salt Lite, Low Sodium, 1kg', 'In Stock.', '28.00', 'Not applicable', '2018-09-30 19:07:49'),
(1459, 380, 'B01K4F7QWU', 1, 1, 'Tata Sampann Rajma, 500g', 'In Stock.', '75.00', '4.2 out of 5 stars', '2018-09-30 19:07:50'),
(1460, 380, 'B01K4F5KWS', 1, 1, 'Tata Sampann Dal Tadka Masala, 100g', 'In Stock.', '48.00', 'Not applicable', '2018-09-30 19:07:50'),
(1461, 380, 'B07DLMRVBY', 1, 1, 'Tata Sampann Tomato Chutney, 100g', 'In Stock.', '44.00', '4.2 out of 5 stars', '2018-09-30 19:07:50'),
(1462, 380, 'B01K4F6CBG', 1, 1, 'Tata Sampann Turmeric Powder Masala, 200g', 'In Stock.', '42.00', 'Not applicable', '2018-09-30 19:07:50'),
(1463, 380, 'B01K4F55BE', 1, 1, 'Tata Sampann Chicken Masala, 100g', 'Currently Unavailable.', '0.00', '4.1 out of 5 stars', '2018-09-30 19:07:50'),
(1464, 380, 'B01MXSK7QM', 1, 1, 'Tata Sampann Kitchen King Masala, 45g', 'In Stock.', '28.00', 'Not applicable', '2018-09-30 19:07:51'),
(1465, 380, 'B07B6H75SQ', 1, 1, 'Tata Sampann Multigrain Chilla Mix, 180g', 'In Stock.', '56.00', 'Not applicable', '2018-09-30 19:07:51'),
(1466, 380, 'B01K4F50P0', 1, 1, 'Tata Sampann Meat Masala, 100g', 'In Stock.', '72.00', 'Not applicable', '2018-09-30 19:07:51'),
(1467, 380, 'B01K4F50P0', 1, 1, 'Tata Sampann Meat Masala, 100g', 'In Stock.', '72.00', 'Not applicable', '2018-09-30 19:07:51'),
(1468, 380, 'B01K4F6HJ8', 1, 1, 'Tata Sampann Chilli Powder Masala, 200g', 'In Stock.', '60.00', 'Not applicable', '2018-09-30 19:07:52'),
(1469, 380, 'B07BGCB6M7', 1, 1, 'Tata Sampann Organic Moong Dal, 1kg', 'In Stock.', '154.00', 'Not applicable', '2018-09-30 19:07:52'),
(1470, 380, 'B01HBFSSUK', 1, 1, 'Tata Sampann Urad Whole, 1kg', 'In Stock.', '94.00', '3.9 out of 5 stars', '2018-09-30 19:07:52'),
(1471, 380, 'B01K4F5KWS', 1, 1, 'Tata Sampann Dal Tadka Masala, 100g', 'In Stock.', '48.00', 'Not applicable', '2018-09-30 19:07:53'),
(1472, 380, 'B01K4F3W00', 1, 1, 'Tata Sampann Moong Chilka, 500g', 'In Stock.', '53.00', '4.2 out of 5 stars', '2018-09-30 19:07:53'),
(1473, 380, 'B01HBF5WBI', 1, 1, 'Tata Salt, 1kg', 'In Stock.', '16.00', '4.2 out of 5 stars', '2018-09-30 19:07:53'),
(1474, 380, 'B01N7CJHBT', 1, 1, 'Tata Sampann Paneer Masala, 45g', 'Currently Unavailable.', '0.00', '3.8 out of 5 stars', '2018-09-30 19:07:53'),
(1475, 380, 'B01N4893Q0', 1, 1, 'Tata Sampann Chilli Powder, 500g', 'In Stock.', '145.00', 'Not applicable', '2018-09-30 19:07:54'),
(1476, 380, 'B078SDRVXY', 1, 1, 'Tata Rock Salt, 200g', 'In Stock.', '30.00', '4.1 out of 5 stars', '2018-09-30 19:07:54'),
(1477, 380, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 19:07:54'),
(1478, 380, 'B01N0GN72Y', 1, 1, 'Tata Salt Pet Jar, 1kg', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:55'),
(1479, 380, 'B07BGCWY83', 1, 1, 'Tata Sampann Organic Toor Dal, 500g', 'In Stock.', '73.00', 'Not applicable', '2018-09-30 19:07:55'),
(1480, 380, 'B01K4F5R3K', 1, 1, 'Tata Sampann Paneer Masala, 100g', 'In Stock.', '66.00', 'Not applicable', '2018-09-30 19:07:55'),
(1481, 380, 'B01HBFUCTA', 1, 1, 'Tata Sampann Urad Dal Split, 500g', 'In Stock.', '47.00', 'Not applicable', '2018-09-30 19:07:55'),
(1482, 380, 'B01K4F3264', 1, 1, 'Tata Rock Salt, 100g', 'In Stock.', '117.00', 'Not applicable', '2018-09-30 19:07:56'),
(1483, 380, 'B01K4F4G4Q', 1, 1, 'Tata Sampann Masoor Dal, Whole, 1kg', 'In Stock.', '81.00', 'Not applicable', '2018-09-30 19:07:56'),
(1484, 380, 'B07B6H751L', 1, 1, 'Tata Sampann Moong Dal Chilla Mix, 180g', 'In Stock.', '56.00', 'Not applicable', '2018-09-30 19:07:56'),
(1485, 380, 'B01MQQDL4A', 1, 1, 'Tata Sampann Garam Masala, 45g', 'In Stock.', '40.00', 'Not applicable', '2018-09-30 19:07:56'),
(1486, 380, 'B01N59O6RL', 1, 1, 'Tata Sampann Pav Bhaji Masala, 100g', 'In Stock.', '71.00', 'Not applicable', '2018-09-30 19:07:57'),
(1487, 380, 'B01K4F6SHO', 1, 1, 'Tata Sampann Besan, 1kg', 'In Stock.', '90.00', 'Not applicable', '2018-09-30 19:07:57'),
(1488, 380, 'B01K4F2DQO', 1, 1, 'Tata Salt Lite Sprinkler, 100g', 'In Stock.', '18.00', 'Not applicable', '2018-09-30 19:07:57'),
(1489, 380, 'B01K4F55BE', 1, 1, 'Tata Sampann Chicken Masala, 100g', 'Currently Unavailable.', '0.00', '4.1 out of 5 stars', '2018-09-30 19:07:57'),
(1490, 380, 'B01K4F5FIC', 1, 1, 'Tata Sampann Punjabi Chhole Masala, 100g', 'In Stock.', '64.00', '4.2 out of 5 stars', '2018-09-30 19:07:57'),
(1491, 380, 'B01HBFXGO8', 1, 1, 'Tata Sampann Masoor Dal Split, 1kg', 'In Stock.', '85.00', '4.0 out of 5 stars', '2018-09-30 19:07:58'),
(1492, 380, 'B01N0L50QX', 1, 1, 'Tata Sampann Chicken Masala, 45g', 'Currently Unavailable.', '0.00', 'Not applicable', '2018-09-30 19:07:58'),
(1493, 380, 'B01K4F5WI0', 1, 1, 'Tata Sampann Chilli Powder Masala, 100g', 'In Stock.', '25.00', '3.9 out of 5 stars', '2018-09-30 19:07:59'),
(1494, 380, 'B01K4F3NPE', 1, 1, 'Tata Sampann Moong Dal Split, 1kg', 'In Stock.', '105.00', '4.0 out of 5 stars', '2018-09-30 19:08:00'),
(1495, 380, 'B01NBEWANN', 1, 1, 'Tata Sampann Turmeric Powder, 500g', 'In Stock.', '112.00', 'Not applicable', '2018-09-30 19:08:00'),
(1496, 380, 'B01K4F4VXC', 1, 1, 'Tata Sampann Garam Masala, 100g', 'In Stock.', '41.00', '4.1 out of 5 stars', '2018-09-30 19:08:01'),
(1497, 380, 'B01K4F3APM', 1, 1, 'Tata Sampann Urad Kali, 1kg', 'In Stock.', '91.00', 'Not applicable', '2018-09-30 19:08:10'),
(1498, 380, 'B07BGC61TC', 1, 1, 'Tata Sampann Organic Moong Dal, 500g', 'In Stock.', '79.00', '3.8 out of 5 stars', '2018-09-30 19:10:23'),
(1499, 380, 'B01K4F3IVS', 1, 1, 'Tata Sampann Toor Dal, 500g', 'In Stock.', '45.00', 'Not applicable', '2018-09-30 19:10:24');

-- --------------------------------------------------------

--
-- Table structure for table `scrape_sessions`
--

CREATE TABLE `scrape_sessions` (
  `id` int(11) NOT NULL,
  `session_start_datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `session_end_datetime` datetime DEFAULT NULL,
  `scrape_result` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scrape_sessions`
--

INSERT INTO `scrape_sessions` (`id`, `session_start_datetime`, `session_end_datetime`, `scrape_result`) VALUES
(164, '2018-09-29 09:57:58', '2018-09-29 09:58:34', 'SUCCESSFUL'),
(165, '2018-09-29 10:00:31', '2018-09-29 10:00:58', 'SUCCESSFUL'),
(166, '2018-09-29 10:11:34', '2018-09-29 10:12:19', 'SUCCESSFUL'),
(167, '2018-09-29 10:16:12', '2018-09-29 10:16:36', 'SUCCESSFUL'),
(168, '2018-09-29 10:17:54', '2018-09-29 10:18:25', 'SUCCESSFUL'),
(169, '2018-09-29 10:19:33', '2018-09-29 10:19:33', 'SCRAPING IN PROGRESS'),
(170, '2018-09-29 10:22:09', '2018-09-29 10:22:09', 'SCRAPING IN PROGRESS'),
(171, '2018-09-29 10:22:10', '2018-09-29 10:22:54', 'SUCCESSFUL'),
(172, '2018-09-29 10:27:26', '2018-09-29 10:27:26', 'SCRAPING IN PROGRESS'),
(173, '2018-09-29 10:27:26', '2018-09-29 10:27:26', 'SCRAPING IN PROGRESS'),
(174, '2018-09-29 10:32:23', '2018-09-29 10:32:23', 'SCRAPING IN PROGRESS'),
(175, '2018-09-29 10:36:24', '2018-09-29 10:36:24', 'SCRAPING IN PROGRESS'),
(176, '2018-09-29 10:36:24', '2018-09-29 10:36:24', 'SCRAPING IN PROGRESS'),
(177, '2018-09-29 10:44:01', '2018-09-29 10:44:01', 'SCRAPING IN PROGRESS'),
(178, '2018-09-29 10:47:48', '2018-09-29 10:48:21', 'SUCCESSFUL'),
(179, '2018-09-29 10:49:51', '2018-09-29 10:50:16', 'SUCCESSFUL'),
(180, '2018-09-29 10:51:06', '2018-09-29 10:51:31', 'SUCCESSFUL'),
(181, '2018-09-29 10:53:45', '2018-09-29 10:54:11', 'SUCCESSFUL'),
(182, '2018-09-29 11:11:28', '2018-09-29 11:11:53', 'SUCCESSFUL'),
(183, '2018-09-29 11:13:38', '2018-09-29 11:14:04', 'SUCCESSFUL'),
(184, '2018-09-29 11:15:32', '2018-09-29 11:16:00', 'SUCCESSFUL'),
(185, '2018-09-29 11:16:41', '2018-09-29 11:17:09', 'SUCCESSFUL'),
(186, '2018-09-29 11:20:21', '2018-09-29 11:20:59', 'SUCCESSFUL'),
(187, '2018-09-29 11:29:13', '2018-09-29 11:29:41', 'SUCCESSFUL'),
(188, '2018-09-29 11:31:35', '2018-09-29 11:32:02', 'SUCCESSFUL'),
(189, '2018-09-29 11:35:05', '2018-09-29 11:35:35', 'SUCCESSFUL'),
(190, '2018-09-29 11:46:44', '2018-09-29 11:46:44', 'SCRAPING IN PROGRESS'),
(191, '2018-09-29 11:50:23', '2018-09-29 11:50:23', 'SCRAPING IN PROGRESS'),
(192, '2018-09-29 11:51:03', '2018-09-29 11:51:03', 'SCRAPING IN PROGRESS'),
(193, '2018-09-29 11:51:42', '2018-09-29 11:51:44', 'SUCCESSFUL'),
(194, '2018-09-29 11:53:23', '2018-09-29 11:53:46', 'SUCCESSFUL'),
(195, '2018-09-29 11:54:34', '2018-09-29 11:55:02', 'SUCCESSFUL'),
(196, '2018-09-29 11:58:16', '2018-09-29 11:58:53', 'SUCCESSFUL'),
(197, '2018-09-29 12:01:20', '2018-09-29 12:01:50', 'SUCCESSFUL'),
(198, '2018-09-29 12:03:45', '2018-09-29 12:04:05', 'SUCCESSFUL'),
(199, '2018-09-29 12:03:54', '2018-09-29 12:04:32', 'SUCCESSFUL'),
(200, '2018-09-29 12:08:51', '2018-09-29 12:09:36', 'SUCCESSFUL'),
(201, '2018-09-29 12:11:00', '2018-09-29 12:11:40', 'SUCCESSFUL'),
(202, '2018-09-29 12:14:11', '2018-09-29 12:14:11', 'SCRAPING IN PROGRESS'),
(203, '2018-09-29 12:15:59', '2018-09-29 12:16:36', 'SUCCESSFUL'),
(204, '2018-09-29 12:18:47', '2018-09-29 12:18:47', 'SCRAPING IN PROGRESS'),
(205, '2018-09-29 12:19:46', '2018-09-29 12:19:46', 'SCRAPING IN PROGRESS'),
(206, '2018-09-29 12:21:57', '2018-09-29 12:22:27', 'SUCCESSFUL'),
(207, '2018-09-29 12:27:08', '2018-09-29 12:27:45', 'SUCCESSFUL'),
(208, '2018-09-29 12:33:57', '2018-09-29 12:33:57', 'SCRAPING IN PROGRESS'),
(209, '2018-09-29 12:35:06', '2018-09-29 12:35:06', 'SCRAPING IN PROGRESS'),
(210, '2018-09-29 12:36:24', '2018-09-29 12:36:24', 'SCRAPING IN PROGRESS'),
(211, '2018-09-29 12:37:45', '2018-09-29 12:37:45', 'SCRAPING IN PROGRESS'),
(212, '2018-09-29 12:38:12', '2018-09-29 12:38:35', 'SUCCESSFUL'),
(213, '2018-09-29 14:02:13', '2018-09-29 14:04:14', 'SUCCESSFUL'),
(215, '2018-09-29 14:11:41', '2018-09-29 14:11:41', 'SCRAPING IN PROGRESS'),
(216, '2018-09-29 14:15:11', '2018-09-29 14:15:11', 'SCRAPING IN PROGRESS'),
(217, '2018-09-29 14:19:51', '2018-09-29 14:19:51', 'SCRAPING IN PROGRESS'),
(218, '2018-09-29 14:27:56', '2018-09-29 14:27:56', 'SCRAPING IN PROGRESS'),
(219, '2018-09-29 14:27:56', '2018-09-29 14:27:56', 'SCRAPING IN PROGRESS'),
(223, '2018-09-29 14:34:10', '2018-09-29 14:34:10', 'SCRAPING IN PROGRESS'),
(224, '2018-09-29 14:44:48', '2018-09-29 14:44:48', 'SCRAPING IN PROGRESS'),
(225, '2018-09-29 14:45:46', '2018-09-29 14:45:49', 'SUCCESSFUL'),
(226, '2018-09-29 14:46:19', '2018-09-29 14:46:22', 'SUCCESSFUL'),
(227, '2018-09-29 14:46:56', '2018-09-29 14:47:02', 'SUCCESSFUL'),
(228, '2018-09-29 14:51:57', '2018-09-29 14:52:03', 'SUCCESSFUL'),
(229, '2018-09-29 14:53:14', '2018-09-29 14:53:20', 'SUCCESSFUL'),
(230, '2018-09-29 14:58:08', '2018-09-29 14:58:10', 'SUCCESSFUL'),
(231, '2018-09-29 15:01:38', '2018-09-29 15:01:44', 'SUCCESSFUL'),
(232, '2018-09-29 15:35:50', '2018-09-29 15:35:55', 'SUCCESSFUL'),
(233, '2018-09-29 15:43:17', '2018-09-29 15:43:23', 'SUCCESSFUL'),
(234, '2018-09-29 16:12:16', '2018-09-29 16:12:21', 'SUCCESSFUL'),
(235, '2018-09-29 16:21:09', '2018-09-29 16:21:13', 'SUCCESSFUL'),
(236, '2018-09-29 16:30:46', '2018-09-29 16:30:50', 'SUCCESSFUL'),
(237, '2018-09-29 16:31:46', '2018-09-29 16:31:46', 'SCRAPING IN PROGRESS'),
(238, '2018-09-29 16:43:27', '2018-09-29 16:44:34', 'SUCCESSFUL'),
(239, '2018-09-29 17:11:44', '2018-09-29 17:12:12', 'SUCCESSFUL'),
(240, '2018-09-29 17:12:40', '2018-09-29 17:13:07', 'SUCCESSFUL'),
(241, '2018-09-29 17:16:25', '2018-09-29 17:16:25', 'SCRAPING IN PROGRESS'),
(242, '2018-09-29 17:19:06', '2018-09-29 17:19:06', 'SUCCESSFUL'),
(243, '2018-09-29 17:20:31', '2018-09-29 17:20:32', 'SUCCESSFUL'),
(244, '2018-09-29 17:21:20', '2018-09-29 17:21:20', 'SCRAPING IN PROGRESS'),
(245, '2018-09-29 17:24:47', '2018-09-29 17:24:47', 'SUCCESSFUL'),
(246, '2018-09-29 17:25:39', '2018-09-29 17:25:40', 'SUCCESSFUL'),
(247, '2018-09-29 17:26:26', '2018-09-29 17:26:27', 'SUCCESSFUL'),
(248, '2018-09-29 17:31:07', '2018-09-29 17:31:07', 'SCRAPING IN PROGRESS'),
(249, '2018-09-29 17:32:10', '2018-09-29 17:32:10', 'SCRAPING IN PROGRESS'),
(250, '2018-09-29 17:37:04', '2018-09-29 17:37:04', 'SCRAPING IN PROGRESS'),
(251, '2018-09-29 17:37:29', '2018-09-29 17:37:29', 'SCRAPING IN PROGRESS'),
(252, '2018-09-29 17:39:34', '2018-09-29 17:39:34', 'SCRAPING IN PROGRESS'),
(253, '2018-09-29 17:40:23', '2018-09-29 17:40:23', 'SUCCESSFUL'),
(254, '2018-09-29 17:40:55', '2018-09-29 17:40:56', 'SUCCESSFUL'),
(255, '2018-09-29 17:41:43', '2018-09-29 17:41:43', 'SCRAPING IN PROGRESS'),
(256, '2018-09-29 17:46:02', '2018-09-29 17:46:03', 'SUCCESSFUL'),
(257, '2018-09-29 17:47:01', '2018-09-29 17:47:02', 'SUCCESSFUL'),
(258, '2018-09-29 17:48:38', '2018-09-29 17:48:38', 'SCRAPING IN PROGRESS'),
(259, '2018-09-29 17:48:56', '2018-09-29 17:48:56', 'SUCCESSFUL'),
(260, '2018-09-29 17:49:38', '2018-09-29 17:49:38', 'SUCCESSFUL'),
(261, '2018-09-29 17:49:57', '2018-09-29 17:49:57', 'SCRAPING IN PROGRESS'),
(262, '2018-09-29 17:51:11', '2018-09-29 17:51:11', 'SUCCESSFUL'),
(263, '2018-09-29 17:51:40', '2018-09-29 17:51:40', 'SCRAPING IN PROGRESS'),
(264, '2018-09-29 17:52:44', '2018-09-29 17:52:44', 'SCRAPING IN PROGRESS'),
(265, '2018-09-29 17:55:16', '2018-09-29 17:55:16', 'SCRAPING IN PROGRESS'),
(266, '2018-09-29 17:56:46', '2018-09-29 17:59:06', 'SUCCESSFUL'),
(267, '2018-09-29 18:34:36', '2018-09-29 18:34:36', 'SCRAPING IN PROGRESS'),
(268, '2018-09-29 18:35:58', '2018-09-29 18:35:58', 'SCRAPING IN PROGRESS'),
(269, '2018-09-29 18:46:27', '2018-09-29 18:46:45', 'SUCCESSFUL'),
(270, '2018-09-29 18:48:40', '2018-09-29 18:48:40', 'SCRAPING IN PROGRESS'),
(271, '2018-09-29 18:49:43', '2018-09-29 18:50:13', 'SUCCESSFUL'),
(272, '2018-09-29 19:05:17', '2018-09-29 19:07:18', 'SUCCESSFUL'),
(273, '2018-09-29 19:11:10', '2018-09-29 19:11:10', 'SCRAPING IN PROGRESS'),
(274, '2018-09-29 19:16:45', '2018-09-29 19:16:45', 'SCRAPING IN PROGRESS'),
(275, '2018-09-29 19:18:52', '2018-09-29 19:20:58', 'SUCCESSFUL'),
(276, '2018-09-29 19:26:48', '2018-09-29 19:26:48', 'SCRAPING IN PROGRESS'),
(277, '2018-09-29 19:29:02', '2018-09-29 19:29:02', 'SCRAPING IN PROGRESS'),
(278, '2018-09-29 19:30:58', '2018-09-29 19:30:58', 'SCRAPING IN PROGRESS'),
(279, '2018-09-29 19:36:01', '2018-09-29 19:36:01', 'SCRAPING IN PROGRESS'),
(280, '2018-09-29 19:37:03', '2018-09-29 19:38:51', 'SUCCESSFUL'),
(281, '2018-09-29 19:40:05', '2018-09-29 19:40:07', 'SUCCESSFUL'),
(282, '2018-09-29 19:41:46', '2018-09-29 19:41:48', 'SUCCESSFUL'),
(283, '2018-09-29 19:42:22', '2018-09-29 19:42:25', 'SUCCESSFUL'),
(284, '2018-09-29 19:42:56', '2018-09-29 19:42:58', 'SUCCESSFUL'),
(285, '2018-09-29 19:56:25', '2018-09-29 19:56:27', 'SUCCESSFUL'),
(286, '2018-09-29 20:10:26', '2018-09-29 20:10:29', 'SUCCESSFUL'),
(287, '2018-09-29 20:12:22', '2018-09-29 20:12:24', 'SUCCESSFUL'),
(288, '2018-09-29 20:16:25', '2018-09-29 20:18:18', 'SUCCESSFUL'),
(289, '2018-09-29 20:34:18', '2018-09-29 20:34:18', 'SCRAPING IN PROGRESS'),
(290, '2018-09-29 20:34:53', '2018-09-29 20:34:53', 'SCRAPING IN PROGRESS'),
(291, '2018-09-29 20:34:56', '2018-09-29 20:34:56', 'SCRAPING IN PROGRESS'),
(292, '2018-09-29 20:35:29', '2018-09-29 20:35:29', 'SCRAPING IN PROGRESS'),
(293, '2018-09-29 20:38:01', '2018-09-29 20:38:01', 'SCRAPING IN PROGRESS'),
(294, '2018-09-29 20:39:41', '2018-09-29 20:39:41', 'SCRAPING IN PROGRESS'),
(295, '2018-09-29 20:41:45', '2018-09-29 20:41:45', 'SCRAPING IN PROGRESS'),
(296, '2018-09-29 20:41:45', '2018-09-29 20:41:45', 'SCRAPING IN PROGRESS'),
(297, '2018-09-29 20:47:53', '2018-09-29 20:47:53', 'SCRAPING IN PROGRESS'),
(298, '2018-09-29 20:48:24', '2018-09-29 20:48:24', 'SCRAPING IN PROGRESS'),
(299, '2018-09-29 20:49:38', '2018-09-29 20:49:38', 'SCRAPING IN PROGRESS'),
(300, '2018-09-29 20:50:12', '2018-09-29 20:50:12', 'SCRAPING IN PROGRESS'),
(301, '2018-09-29 20:50:51', '2018-09-29 20:50:51', 'SCRAPING IN PROGRESS'),
(302, '2018-09-29 20:52:33', '2018-09-29 20:52:33', 'SCRAPING IN PROGRESS'),
(303, '2018-09-29 20:52:38', '2018-09-29 20:52:38', 'SCRAPING IN PROGRESS'),
(304, '2018-09-29 20:55:28', '2018-09-29 20:55:28', 'SCRAPING IN PROGRESS'),
(305, '2018-09-29 20:56:09', '2018-09-29 20:56:09', 'SCRAPING IN PROGRESS'),
(306, '2018-09-29 20:56:46', '2018-09-29 20:56:46', 'SCRAPING IN PROGRESS'),
(307, '2018-09-29 21:00:21', '2018-09-29 21:00:21', 'SCRAPING IN PROGRESS'),
(308, '2018-09-29 21:01:26', '2018-09-29 21:01:26', 'SCRAPING IN PROGRESS'),
(309, '2018-09-29 21:02:14', '2018-09-29 21:02:14', 'SCRAPING IN PROGRESS'),
(310, '2018-09-29 21:02:58', '2018-09-29 21:02:58', 'SCRAPING IN PROGRESS'),
(311, '2018-09-29 21:05:13', '2018-09-29 21:05:13', 'SCRAPING IN PROGRESS'),
(312, '2018-09-29 21:05:56', '2018-09-29 21:05:56', 'SCRAPING IN PROGRESS'),
(313, '2018-09-29 21:06:56', '2018-09-29 21:06:56', 'SCRAPING IN PROGRESS'),
(314, '2018-09-29 21:11:09', '2018-09-29 21:11:09', 'SCRAPING IN PROGRESS'),
(315, '2018-09-29 21:11:09', '2018-09-29 21:11:09', 'SCRAPING IN PROGRESS'),
(316, '2018-09-29 21:24:31', '2018-09-29 21:24:31', 'SCRAPING IN PROGRESS'),
(317, '2018-09-30 01:06:15', '2018-09-30 01:06:15', 'SCRAPING IN PROGRESS'),
(318, '2018-09-30 01:08:04', '2018-09-30 01:10:14', 'SUCCESSFUL'),
(319, '2018-09-30 01:12:39', '2018-09-30 01:12:39', 'SCRAPING IN PROGRESS'),
(320, '2018-09-30 01:14:35', '2018-09-30 01:17:41', 'SUCCESSFUL'),
(321, '2018-09-30 12:54:11', '2018-09-30 12:54:11', 'SCRAPING IN PROGRESS'),
(322, '2018-09-30 12:56:29', '2018-09-30 12:56:29', 'SCRAPING IN PROGRESS'),
(323, '2018-09-30 12:57:05', '2018-09-30 12:57:05', 'SCRAPING IN PROGRESS'),
(324, '2018-09-30 13:05:57', '2018-09-30 13:05:57', 'SCRAPING IN PROGRESS'),
(325, '2018-09-30 13:13:06', '2018-09-30 13:13:06', 'SCRAPING IN PROGRESS'),
(326, '2018-09-30 13:26:43', '2018-09-30 13:26:43', 'SCRAPING IN PROGRESS'),
(327, '2018-09-30 13:35:34', '2018-09-30 13:35:34', 'SCRAPING IN PROGRESS'),
(328, '2018-09-30 13:38:04', '2018-09-30 13:38:04', 'SCRAPING IN PROGRESS'),
(329, '2018-09-30 13:43:43', '2018-09-30 13:43:43', 'SCRAPING IN PROGRESS'),
(330, '2018-09-30 13:43:48', '2018-09-30 13:43:48', 'SCRAPING IN PROGRESS'),
(331, '2018-09-30 13:48:37', '2018-09-30 13:48:37', 'SCRAPING IN PROGRESS'),
(332, '2018-09-30 13:48:37', '2018-09-30 13:48:37', 'SCRAPING IN PROGRESS'),
(333, '2018-09-30 13:48:43', '2018-09-30 13:48:43', 'SCRAPING IN PROGRESS'),
(334, '2018-09-30 14:00:17', '2018-09-30 14:02:40', 'SUCCESSFUL'),
(335, '2018-09-30 14:03:55', '2018-09-30 14:03:55', 'SCRAPING IN PROGRESS'),
(336, '2018-09-30 14:04:50', '2018-09-30 14:04:50', 'SCRAPING IN PROGRESS'),
(337, '2018-09-30 14:09:50', '2018-09-30 14:09:50', 'SCRAPING IN PROGRESS'),
(338, '2018-09-30 14:10:43', '2018-09-30 14:10:43', 'SCRAPING IN PROGRESS'),
(339, '2018-09-30 14:13:23', '2018-09-30 14:13:23', 'SCRAPING IN PROGRESS'),
(340, '2018-09-30 14:14:59', '2018-09-30 14:14:59', 'SCRAPING IN PROGRESS'),
(341, '2018-09-30 14:19:59', '2018-09-30 14:19:59', 'SCRAPING IN PROGRESS'),
(342, '2018-09-30 14:25:41', '2018-09-30 14:25:41', 'SCRAPING IN PROGRESS'),
(343, '2018-09-30 14:27:01', '2018-09-30 14:27:01', 'SCRAPING IN PROGRESS'),
(344, '2018-09-30 14:29:33', '2018-09-30 14:29:33', 'SCRAPING IN PROGRESS'),
(345, '2018-09-30 14:30:51', '2018-09-30 14:30:51', 'SCRAPING IN PROGRESS'),
(346, '2018-09-30 14:47:17', '2018-09-30 14:47:17', 'SCRAPING IN PROGRESS'),
(347, '2018-09-30 14:48:30', '2018-09-30 14:48:30', 'SCRAPING IN PROGRESS'),
(348, '2018-09-30 14:52:14', '2018-09-30 14:52:14', 'SCRAPING IN PROGRESS'),
(349, '2018-09-30 14:55:00', '2018-09-30 14:55:00', 'SCRAPING IN PROGRESS'),
(350, '2018-09-30 14:56:45', '2018-09-30 14:56:45', 'SCRAPING IN PROGRESS'),
(351, '2018-09-30 14:57:34', '2018-09-30 14:57:34', 'SCRAPING IN PROGRESS'),
(352, '2018-09-30 15:01:07', '2018-09-30 15:01:07', 'SCRAPING IN PROGRESS'),
(353, '2018-09-30 15:05:39', '2018-09-30 15:05:39', 'SCRAPING IN PROGRESS'),
(354, '2018-09-30 15:06:46', '2018-09-30 15:06:46', 'SCRAPING IN PROGRESS'),
(355, '2018-09-30 15:08:47', '2018-09-30 15:08:47', 'SCRAPING IN PROGRESS'),
(356, '2018-09-30 15:15:04', '2018-09-30 15:15:04', 'SCRAPING IN PROGRESS'),
(357, '2018-09-30 15:17:51', '2018-09-30 15:19:35', 'SUCCESSFUL'),
(358, '2018-09-30 15:17:51', '2018-09-30 15:19:40', 'SUCCESSFUL'),
(359, '2018-09-30 15:24:06', '2018-09-30 15:24:06', 'SCRAPING IN PROGRESS'),
(360, '2018-09-30 15:25:56', '2018-09-30 15:25:56', 'SCRAPING IN PROGRESS'),
(361, '2018-09-30 15:26:47', '2018-09-30 15:26:47', 'SCRAPING IN PROGRESS'),
(362, '2018-09-30 15:36:35', '2018-09-30 15:36:35', 'SCRAPING IN PROGRESS'),
(363, '2018-09-30 15:43:25', '2018-09-30 15:43:25', 'SCRAPING IN PROGRESS'),
(364, '2018-09-30 15:44:34', '2018-09-30 15:44:34', 'SCRAPING IN PROGRESS'),
(365, '2018-09-30 15:45:47', '2018-09-30 15:45:47', 'SCRAPING IN PROGRESS'),
(366, '2018-09-30 15:46:24', '2018-09-30 15:46:24', 'SCRAPING IN PROGRESS'),
(367, '2018-09-30 15:54:33', '2018-09-30 15:54:33', 'SCRAPING IN PROGRESS'),
(368, '2018-09-30 15:55:20', '2018-09-30 15:55:20', 'SCRAPING IN PROGRESS'),
(369, '2018-09-30 15:55:26', '2018-09-30 15:55:26', 'SCRAPING IN PROGRESS'),
(370, '2018-09-30 15:56:09', '2018-09-30 15:56:09', 'SCRAPING IN PROGRESS'),
(371, '2018-09-30 16:10:40', '2018-09-30 16:10:40', 'SCRAPING IN PROGRESS'),
(372, '2018-09-30 16:22:13', '2018-09-30 16:22:13', 'SCRAPING IN PROGRESS'),
(373, '2018-09-30 16:22:41', '2018-09-30 16:22:41', 'SCRAPING IN PROGRESS'),
(374, '2018-09-30 16:30:50', '2018-09-30 16:30:50', 'SCRAPING IN PROGRESS'),
(375, '2018-09-30 16:32:21', '2018-09-30 16:32:21', 'SCRAPING IN PROGRESS'),
(376, '2018-09-30 16:54:21', '2018-09-30 16:55:53', 'SUCCESSFUL'),
(377, '2018-09-30 17:33:38', '2018-09-30 17:40:01', 'SUCCESSFUL'),
(378, '2018-09-30 18:32:45', '2018-09-30 18:32:45', 'SCRAPING IN PROGRESS'),
(379, '2018-09-30 18:35:34', '2018-09-30 18:41:23', 'SUCCESSFUL'),
(380, '2018-09-30 19:07:14', '2018-09-30 19:10:24', 'SUCCESSFUL');

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
-- Dumping data for table `stores`
--

INSERT INTO `stores` (`id`, `store_name`, `base_url`) VALUES
(1, 'amazon', 'http://www.amazon.in/dp/'),
(2, 'grofers', 'http://www.grofers.com/prn//prid/'),
(3, 'bigbasket', 'https://www.bigbasket.com/pd/');

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
-- Dumping data for table `store_locations`
--

INSERT INTO `store_locations` (`id`, `store_id`, `city_area`, `pin_code`) VALUES
(3, 1, 'Mumbai_Fort', '400701'),
(6, 2, 'Mumbai_Dombivli', '400086'),
(7, 3, 'Mumbai_Kalbadevi', '400025');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `report_recipients`
--
ALTER TABLE `report_recipients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `scrape_reports`
--
ALTER TABLE `scrape_reports`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1500;

--
-- AUTO_INCREMENT for table `scrape_sessions`
--
ALTER TABLE `scrape_sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=381;

--
-- AUTO_INCREMENT for table `stores`
--
ALTER TABLE `stores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `store_locations`
--
ALTER TABLE `store_locations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `system_users`
--
ALTER TABLE `system_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
