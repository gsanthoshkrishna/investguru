-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: 172.18.0.2    Database: murthy
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `history_data`
--

DROP TABLE IF EXISTS `history_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_data` (
  `SYMBOL` varchar(20) DEFAULT NULL,
  `SERIES` varchar(10) DEFAULT NULL,
  `OPEN` float DEFAULT NULL,
  `HIGH` float DEFAULT NULL,
  `LOW` float DEFAULT NULL,
  `CLOSE` float DEFAULT NULL,
  `LAST` float DEFAULT NULL,
  `PREVCLOSE` float DEFAULT NULL,
  `TOTTRDQTY` float DEFAULT NULL,
  `TOTTRDVAL` float DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  `TOTALTRADES` float DEFAULT NULL,
  `col1` varchar(20) DEFAULT NULL,
  `col2` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `invest_data`
--

DROP TABLE IF EXISTS `invest_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invest_data` (
  `name` varchar(50) DEFAULT NULL,
  `value` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `target` float DEFAULT NULL,
  `tag` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `notes`
--

DROP TABLE IF EXISTS `notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notes` (
  `note` varchar(100) DEFAULT NULL,
  `note_date` date DEFAULT NULL,
  `impact` varchar(20) DEFAULT NULL,
  `sector` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pending_trades`
--

DROP TABLE IF EXISTS `pending_trades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pending_trades` (
  `name` varchar(20) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `current_value` float DEFAULT NULL,
  `notes` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `reminders`
--

DROP TABLE IF EXISTS `reminders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reminders` (
  `name` varchar(20) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `dependancy` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `script_details`
--

DROP TABLE IF EXISTS `script_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `script_details` (
  `name` varchar(50) DEFAULT NULL,
  `avg_value` float DEFAULT NULL,
  `low_value` float DEFAULT NULL,
  `high_value` float DEFAULT NULL,
  `units` int(11) DEFAULT NULL,
  `perc_change` float DEFAULT NULL,
  `amt_change` float DEFAULT NULL,
  `tags` varchar(50) DEFAULT NULL,
  `status` enum('CLOSED','OPEN','COMPLETED','INACTIVE') DEFAULT NULL,
  `current_value` float DEFAULT NULL,
  `script_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`script_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `targets`
--

DROP TABLE IF EXISTS `targets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `targets` (
  `name` varchar(20) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `target` float DEFAULT NULL,
  `final_target_date` date DEFAULT NULL,
  `recurrance` varchar(20) DEFAULT NULL,
  `target_type` varchar(20) DEFAULT NULL COMMENT 'monthly/long/short',
  `description` varchar(50) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `status` enum('CLOSED','OPEN','COMPLETED','INACTIVE') DEFAULT NULL,
  `target_id` int(11) NOT NULL AUTO_INCREMENT,
  `target_perc_reached` int(11) DEFAULT NULL,
  `invested_amt` float DEFAULT NULL,
  `target_units` varchar(10) DEFAULT NULL COMMENT 'percentage or amount',
  `next_target_date` date DEFAULT NULL,
  PRIMARY KEY (`target_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `today_values`
--

DROP TABLE IF EXISTS `today_values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `today_values` (
  `SYMBOL` varchar(20) DEFAULT NULL,
  `SERIES` varchar(10) DEFAULT NULL,
  `OPEN` float DEFAULT NULL,
  `HIGH` float DEFAULT NULL,
  `LOW` float DEFAULT NULL,
  `CLOSE` float DEFAULT NULL,
  `LAST` float DEFAULT NULL,
  `PREVCLOSE` float DEFAULT NULL,
  `TOTTRDQTY` float DEFAULT NULL,
  `TOTTRDVAL` float DEFAULT NULL,
  `TIMESTAMP` varchar(20) DEFAULT NULL,
  `TOTALTRADES` float DEFAULT NULL,
  `col1` varchar(20) DEFAULT NULL,
  `col2` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tr_targets`
--

DROP TABLE IF EXISTS `tr_targets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tr_targets` (
  `name` varchar(20) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `target` float DEFAULT NULL,
  `target_date` date DEFAULT NULL,
  `recurrance` varchar(20) DEFAULT NULL,
  `target_type` varchar(20) DEFAULT NULL COMMENT 'monthly/long/short',
  `description` varchar(50) DEFAULT NULL,
  `startdate` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `target_id` int(11) NOT NULL AUTO_INCREMENT,
  `target_perc_reached` int(11) DEFAULT NULL,
  `invested_amt` float DEFAULT NULL,
  `target_units` varchar(10) DEFAULT NULL COMMENT 'percentage or amount',
  `days_completed` int(11) DEFAULT NULL,
  `amt_changed` float DEFAULT NULL,
  `script_id` varchar(20) DEFAULT NULL,
  `perc_changed` float(2,2) DEFAULT NULL,
  `stop_loss` float(2,2) DEFAULT NULL,
  PRIMARY KEY (`target_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tr_trades`
--

DROP TABLE IF EXISTS `tr_trades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tr_trades` (
  `name` varchar(50) DEFAULT NULL,
  `value` float DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `tag` varchar(50) DEFAULT NULL,
  `tr_date` date DEFAULT NULL,
  `tr_type` enum('SELL','BUY') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `watchlist`
--

DROP TABLE IF EXISTS `watchlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `watchlist` (
  `name` varchar(20) DEFAULT NULL,
  `priority` varchar(5) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `formula` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-19 14:56:36
