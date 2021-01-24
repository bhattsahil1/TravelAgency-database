-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: TRAVEL_AGENCY
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AREA_OF_EXPERTISE`
--

DROP TABLE IF EXISTS `AREA_OF_EXPERTISE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AREA_OF_EXPERTISE` (
  `Sno` int(11) NOT NULL,
  `Area_of_expertise` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AREA_OF_EXPERTISE`
--

LOCK TABLES `AREA_OF_EXPERTISE` WRITE;
/*!40000 ALTER TABLE `AREA_OF_EXPERTISE` DISABLE KEYS */;
/*!40000 ALTER TABLE `AREA_OF_EXPERTISE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMERS`
--

DROP TABLE IF EXISTS `CUSTOMERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMERS` (
  `Sno` int(11) NOT NULL AUTO_INCREMENT,
  `Fname` varchar(30) NOT NULL,
  `Mname` varchar(30) DEFAULT NULL,
  `Lname` varchar(30) NOT NULL,
  `Start_date` date NOT NULL,
  `Last_date` date NOT NULL,
  `HNo` int(11) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `DOB` date NOT NULL,
  `No_of_travellers` int(11) NOT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMERS`
--

LOCK TABLES `CUSTOMERS` WRITE;
/*!40000 ALTER TABLE `CUSTOMERS` DISABLE KEYS */;
INSERT INTO `CUSTOMERS` VALUES (1,'Sahil','Manoj','Bhatt','2013-04-05','2013-04-12',1,'Bandra','2000-09-15',4),(4,'Mohandas','Karamchand','Gandhi','2014-02-05','2014-02-10',125,'Delhi','1956-06-23',3),(5,'Srivathsan','-','Baskaran','2015-06-09','2015-06-20',217,'Chennai','2001-03-08',4);
/*!40000 ALTER TABLE `CUSTOMERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER_PACKAGE`
--

DROP TABLE IF EXISTS `CUSTOMER_PACKAGE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMER_PACKAGE` (
  `Sno` int(11) NOT NULL,
  `Package_Opted` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER_PACKAGE`
--

LOCK TABLES `CUSTOMER_PACKAGE` WRITE;
/*!40000 ALTER TABLE `CUSTOMER_PACKAGE` DISABLE KEYS */;
INSERT INTO `CUSTOMER_PACKAGE` VALUES (5,'4');
/*!40000 ALTER TABLE `CUSTOMER_PACKAGE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EMERGENCY_DETAILS`
--

DROP TABLE IF EXISTS `EMERGENCY_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EMERGENCY_DETAILS` (
  `Sno` int(11) DEFAULT NULL,
  `Emergency Contact Name` varchar(40) DEFAULT NULL,
  `Emergency Contact Number` int(11) DEFAULT NULL,
  `Emergency Contact Address` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMERGENCY_DETAILS`
--

LOCK TABLES `EMERGENCY_DETAILS` WRITE;
/*!40000 ALTER TABLE `EMERGENCY_DETAILS` DISABLE KEYS */;
INSERT INTO `EMERGENCY_DETAILS` VALUES (5,'Shiva Prasad',12123123,'252B Baker Street');
/*!40000 ALTER TABLE `EMERGENCY_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FLIGHT_DETAILS`
--

DROP TABLE IF EXISTS `FLIGHT_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FLIGHT_DETAILS` (
  `Sno` int(11) NOT NULL,
  `Flight_Opted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FLIGHT_DETAILS`
--

LOCK TABLES `FLIGHT_DETAILS` WRITE;
/*!40000 ALTER TABLE `FLIGHT_DETAILS` DISABLE KEYS */;
INSERT INTO `FLIGHT_DETAILS` VALUES (1,'6E-302'),(2,'S-1712');
/*!40000 ALTER TABLE `FLIGHT_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOTELS`
--

DROP TABLE IF EXISTS `HOTELS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOTELS` (
  `Hotel_Name` varchar(20) NOT NULL,
  `Hotel_address` varchar(40) DEFAULT NULL,
  `Rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`Hotel_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOTELS`
--

LOCK TABLES `HOTELS` WRITE;
/*!40000 ALTER TABLE `HOTELS` DISABLE KEYS */;
INSERT INTO `HOTELS` VALUES ('4 Seasons','14,Fuhrer Street, Berlin, Germany',3),('Ace Ventura','1,Ray Avenue,Chennai',5),('Marriot','252B_Baker_Street_London_UK',4),('Raj Bhavan','14,Wilbur St.,Lz Avenue, Montreal',5),('Red Velvet','1334, China Town, Shanghai, China',4);
/*!40000 ALTER TABLE `HOTELS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOTEL_DETAILS`
--

DROP TABLE IF EXISTS `HOTEL_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOTEL_DETAILS` (
  `Sno` int(11) NOT NULL,
  `Hotel_Opted` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOTEL_DETAILS`
--

LOCK TABLES `HOTEL_DETAILS` WRITE;
/*!40000 ALTER TABLE `HOTEL_DETAILS` DISABLE KEYS */;
INSERT INTO `HOTEL_DETAILS` VALUES (1,'Marriot'),(2,'4 Seasons'),(3,'Red Velvet'),(4,'Ace Ventura');
/*!40000 ALTER TABLE `HOTEL_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LANGUAGES_SPOKEN`
--

DROP TABLE IF EXISTS `LANGUAGES_SPOKEN`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LANGUAGES_SPOKEN` (
  `Tourguide_id` int(11) NOT NULL,
  `Languages_spoken` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LANGUAGES_SPOKEN`
--

LOCK TABLES `LANGUAGES_SPOKEN` WRITE;
/*!40000 ALTER TABLE `LANGUAGES_SPOKEN` DISABLE KEYS */;
INSERT INTO `LANGUAGES_SPOKEN` VALUES (1,'Tamil'),(1,'English'),(1,'Malayalam');
/*!40000 ALTER TABLE `LANGUAGES_SPOKEN` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MEDICINE`
--

DROP TABLE IF EXISTS `MEDICINE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MEDICINE` (
  `Sno` int(11) DEFAULT NULL,
  `Medicines` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MEDICINE`
--

LOCK TABLES `MEDICINE` WRITE;
/*!40000 ALTER TABLE `MEDICINE` DISABLE KEYS */;
/*!40000 ALTER TABLE `MEDICINE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PACKAGE`
--

DROP TABLE IF EXISTS `PACKAGE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PACKAGE` (
  `Package_id` int(11) NOT NULL AUTO_INCREMENT,
  `Package_category` varchar(20) DEFAULT NULL,
  `Transport_vehicle` varchar(15) DEFAULT NULL,
  `Package_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Package_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PACKAGE`
--

LOCK TABLES `PACKAGE` WRITE;
/*!40000 ALTER TABLE `PACKAGE` DISABLE KEYS */;
INSERT INTO `PACKAGE` VALUES (1,'Sight-seeing','TATA Sumo','VIP'),(4,'Sightseeing','Swift Maruti','Economy');
/*!40000 ALTER TABLE `PACKAGE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SPECIAL_REQUESTS`
--

DROP TABLE IF EXISTS `SPECIAL_REQUESTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SPECIAL_REQUESTS` (
  `Sno` int(11) DEFAULT NULL,
  `Child` varchar(40) DEFAULT NULL,
  `Diffrently Abled` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SPECIAL_REQUESTS`
--

LOCK TABLES `SPECIAL_REQUESTS` WRITE;
/*!40000 ALTER TABLE `SPECIAL_REQUESTS` DISABLE KEYS */;
INSERT INTO `SPECIAL_REQUESTS` VALUES (5,'yes','no'),(4,'no','yes');
/*!40000 ALTER TABLE `SPECIAL_REQUESTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TOUR_GUIDE`
--

DROP TABLE IF EXISTS `TOUR_GUIDE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TOUR_GUIDE` (
  `Tourguide_id` int(11) NOT NULL AUTO_INCREMENT,
  `Tourguide_name` varchar(20) NOT NULL,
  `Dob` date DEFAULT NULL,
  PRIMARY KEY (`Tourguide_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TOUR_GUIDE`
--

LOCK TABLES `TOUR_GUIDE` WRITE;
/*!40000 ALTER TABLE `TOUR_GUIDE` DISABLE KEYS */;
INSERT INTO `TOUR_GUIDE` VALUES (1,'gautham venugopal','2000-04-15'),(3,'Rocky Balboa','1987-09-14'),(4,'Madan Mohan','1998-04-02');
/*!40000 ALTER TABLE `TOUR_GUIDE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TRANSPORTATION`
--

DROP TABLE IF EXISTS `TRANSPORTATION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TRANSPORTATION` (
  `Flight_no` varchar(10) NOT NULL,
  `Airline` varchar(15) NOT NULL,
  `Boarding` varchar(15) NOT NULL,
  `Destination` varchar(15) NOT NULL,
  PRIMARY KEY (`Flight_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TRANSPORTATION`
--

LOCK TABLES `TRANSPORTATION` WRITE;
/*!40000 ALTER TABLE `TRANSPORTATION` DISABLE KEYS */;
/*!40000 ALTER TABLE `TRANSPORTATION` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-13  8:57:42
