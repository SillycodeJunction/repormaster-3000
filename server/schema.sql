CREATE DATABASE `reportmaster`;
USE `reportmaster`;
CREATE TABLE `projects`
(
`aindex` INTEGER AUTO_INCREMENT,
`status` ENUM('new', 'started') NOT NULL,
`description` TEXT NOT NULL,
PRIMARY KEY (`aindex`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;