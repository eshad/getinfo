--
-- Database: `getinfo`
--

-- --------------------------------------------------------

--
-- Table structure for table `personal`
--

CREATE TABLE `personal` (
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `mother` varchar(30) NOT NULL,
  `father` varchar(30) NOT NULL,
  `sibling` int(2) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `present_address` varchar(100) NOT NULL,
  `parmanent_address` varchar(100) NOT NULL,
  `child` int(2) NOT NULL,
  `marital_status` varchar(20) NOT NULL
) 



