-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 19, 2018 at 12:19 PM
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
-- Database: `web-scrapper`
--

-- --------------------------------------------------------

--
-- Table structure for table `bigbasket`
--

CREATE TABLE `bigbasket` (
  `sku` text NOT NULL,
  `web_url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bigbasket`
--

INSERT INTO `bigbasket` (`sku`, `web_url`) VALUES
('CauliFlower', 'https://www.bigbasket.com/pd/10000074/fresho-cauliflower-1-pc/'),
('Kiwi', 'https://www.bigbasket.com/pd/20000911/fresho-kiwi-green-3-pcs/'),
('Potato', 'https://www.bigbasket.com/pd/10000159/fresho-potato-1-kg/?nc=Fruits%20Vegetables&t_pg=HomePage-T1-Aug-Sep&t_p=T1-25th_Aug_2018&t_s=Fruits%20Vegetables&t_pos_sec=3&t_pos_item=1&t_ch=desktop'),
('Sambhar Onion', 'https://www.bigbasket.com/pd/10000178/fresho-onion-sambhar-250-gm/'),
('Watermelon', 'https://www.bigbasket.com/pd/10000207/fresho-watermelon-small-1-pc/');

-- --------------------------------------------------------

--
-- Table structure for table `productdetails`
--

CREATE TABLE `productdetails` (
  `name` varchar(100) NOT NULL DEFAULT 'NOT NULL',
  `price` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `offer` varchar(25) NOT NULL DEFAULT 'NOT NUL',
  `stock` varchar(50) NOT NULL DEFAULT 'NOT NULL',
  `rating` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `productdetails`
--

INSERT INTO `productdetails` (`name`, `price`, `offer`, `stock`, `rating`) VALUES
('Kellogg\'s Original & the Best Corn Flakes (Pouch)', '219', '25% OFF', 'Data Unavailable', 'Not available'),
('Kissan Fresh Tomato Ketchup (Pouch)', '110', '12% OFF', 'Data Unavailable', 'Not available'),
('Aashirvaad Atta, Multigrains, 5kg', ' 242.00', ' 43.00 (15%)', 'In Stock.', '3.8 out of 5 stars');

-- --------------------------------------------------------

--
-- Table structure for table `skus`
--

CREATE TABLE `skus` (
  `id` varchar(20) NOT NULL,
  `website` varchar(25) NOT NULL DEFAULT 'NOT NULL',
  `producturlname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `skus`
--

INSERT INTO `skus` (`id`, `website`, `producturlname`) VALUES
('106', 'grofers', 'tata-lite-salt');

-- --------------------------------------------------------

--
-- Table structure for table `sku_master`
--

CREATE TABLE `sku_master` (
  `sku` longtext NOT NULL,
  `website_url` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sku_master`
--

INSERT INTO `sku_master` (`sku`, `website_url`) VALUES
('aashirvaad-shudh-chakki-whole-wheat-atta', 'https://grofers.com/prn/aashirvaad-shudh-chakki-whole-wheat-atta/prid/333324'),
('Agro-Fresh-Premium-Ground-500g', 'https://www.amazon.in/Agro-Fresh-Premium-Ground-500g/dp/B01L22XRFO?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('Amazon-Brand-Vedaka-Popular-Chana', 'https://www.amazon.in/Amazon-Brand-Vedaka-Popular-Chana/dp/B079NQKQH8?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('choostix-pet-a-sure-lactocer-milk-cereals-n-vegeteables-400-gm', 'https://www.bigbasket.com/pd/40100672/choostix-pet-a-sure-lactocer-milk-cereals-n-vegeteables-400-gm/'),
('dettol-original-soap-pack-of-4', 'https://grofers.com/prn/dettol-original-soap-pack-of-4/prid/254121'),
('fresho-onion-1-kg', 'https://www.bigbasket.com/pd/10000148/fresho-onion-1-kg/?nc=Fruits%20Vegetables&t_pg=HomePage-T1-Aug-Sep&t_p=T1-25th_Aug_2018&t_s=Fruits%20Vegetables&t_pos_sec=3&t_pos_item=1&t_ch=desktop'),
('fresho-tomato-hybrid-1-kg', 'https://www.bigbasket.com/pd/10000200/fresho-tomato-hybrid-1-kg/?nc=Fruits%20Vegetables&t_pg=HomePage-T1-Aug-Sep&t_p=T1-25th_Aug_2018&t_s=Fruits%20Vegetables&t_pos_sec=3&t_pos_item=1&t_ch=desktop'),
('Godrej-Protekt-Master-Blaster-Handwash', 'https://www.amazon.in/Godrej-Protekt-Master-Blaster-Handwash/dp/B078X5298B?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('grofers-printed-20x30-cm-plastic-chopping-board-assorted', 'https://grofers.com/prn/grofers-printed-20x30-cm-plastic-chopping-board-assorted/prid/386061'),
('kitchen-garden-pets/pet-food-accessories', 'https://www.bigbasket.com/pc/kitchen-garden-pets/pet-food-accessories/?nc=Linear&t_pg=HomePage-T1-Aug-Sep&t_p=T1-25th_Aug_2018&t_s=Linear&t_pos_sec=10&t_pos_item=2&t_ch=desktop'),
('liberty-sunday-refined-sunflower-oil-pouch', 'https://grofers.com/prn/liberty-sunday-refined-sunflower-oil-pouch/prid/60164'),
('Madhur-Pure-Hygienic-Sugar-1kg', 'https://www.amazon.in/Madhur-Pure-Hygienic-Sugar-1kg/dp/B01GCEGCP4?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('Maggi-2-Minutes-Noodles-Masala-560g', 'https://www.amazon.in/Maggi-2-Minutes-Noodles-Masala-560g/dp/B01H6QIOXK?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('pedigree-dry-dog-food-meat-rice-for-adult-dogs-10-kg', 'https://www.bigbasket.com/pd/182218/pedigree-dry-dog-food-meat-rice-for-adult-dogs-10-kg/?nc=L2Category&t_pg=L2Cagegory&t_p=L2Category&t_s=L2Category&t_pos=3&t_ch=desktop'),
('surf-excel-easy-wash-detergent-powder', 'https://grofers.com/prn/surf-excel-easy-wash-detergent-powder/prid/27070'),
('Tata-Salt-Lite-Low-Sodium', 'https://www.amazon.in/Tata-Salt-Lite-Low-Sodium/dp/B01HBEUAI4?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('Tata-Sampann-Pulses-Toor-Dal', 'https://www.amazon.in/Tata-Sampann-Pulses-Toor-Dal/dp/B01HBEQ006?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('TooYumm-Veggie-Stix-Cheese-Herbs', 'https://www.amazon.in/TooYumm-Veggie-Stix-Cheese-Herbs/dp/B075YPF9JK?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af'),
('Vim-Dishwash-Bar-3x200-g', 'https://www.amazon.in/Vim-Dishwash-Bar-3x200-g/dp/B01CJW6PFK?pd_rd_wg=WdKI1&pd_rd_r=6157ebba-0d32-4022-8b0e-5a1eb1d88ac5&pd_rd_w=GHz42&ref_=pd_gw_simh&pf_rd_r=MGZHZQ2WR5FKDK061X43&pf_rd_p=c2ebdb65-3bcd-59df-a62a-6b0e925df1af');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bigbasket`
--
ALTER TABLE `bigbasket`
  ADD PRIMARY KEY (`sku`(767));

--
-- Indexes for table `skus`
--
ALTER TABLE `skus`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `producturlname` (`producturlname`);

--
-- Indexes for table `sku_master`
--
ALTER TABLE `sku_master`
  ADD PRIMARY KEY (`sku`(767));
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
