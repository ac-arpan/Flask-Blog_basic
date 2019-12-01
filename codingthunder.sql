-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2019 at 05:08 PM
-- Server version: 10.1.32-MariaDB
-- PHP Version: 5.6.36

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno.` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `mes` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno.`, `name`, `email`, `phone_num`, `mes`, `date`) VALUES
(1, 'name', 'name@gmail.com', '1234567890', 'Entering first message to database', '2019-10-27 22:00:56'),
(2, 'Arpan Chowdhury', 'abc@gmail.com', '9876238201', 'TEST', '2019-10-27 22:35:30'),
(3, 'Shibam Das', 'shibarm@gmail.com', '9876238201', 'Hey! I wanna get in touch with you.\r\nPlease arrange a time.\r\n', '2019-10-29 11:27:22'),
(4, 'Random', 'random@gmail.com', '4532167834', 'Test Message', '2019-10-29 11:39:52'),
(5, 'Souvik Dey', 'sub@gmail.com', '3567128942', 'Hello!', '2019-10-29 11:43:29'),
(6, 'Rayan', 'rc@gmail.com', '6743128936', 'Hey! Bro What\'s Up!', '2019-10-29 11:51:41'),
(7, 'Paul', 'paul@gmail.com', '1234567891', 'I wanna talk to you.', '2019-11-02 10:12:02');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(20) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(30) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'This is first post title.', 'Tagline of first-post', 'first-post', 'I am very excited to add my first post to my coding thunder blog. ', 'home-bg.jpg', '2019-11-02 09:55:12'),
(2, 'This is my second post', 'Cool Tagline ', 'second-post', 'I am very glad to share my second post in my blog...', 'about-bg.jpg', '2019-10-30 12:29:39'),
(3, 'Let\'s learn about Python Django', 'Django Makes the world easy', 'third-post', 'Django is a cool framework of python used in web development backend programming. Using django we can easily handle those websites which has rich administrative background.', 'post-sample-image.jpg', '2019-10-30 12:46:09'),
(4, 'Let\'s learn about C++', 'C++ is very powerful', 'fourth-post', 'C++ is a object oriented language.', 'cpp.img', '2019-11-01 22:23:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno.`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno.` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
