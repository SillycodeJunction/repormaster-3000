DROP DATABASE IF EXISTS `reportmaster`;
CREATE DATABASE `reportmaster`;
USE `reportmaster`;
CREATE TABLE `work_order`
(
`aindex` INTEGER AUTO_INCREMENT,
`status` ENUM('new', 'details requested','ready for work','assigned','delayed','failed','finished','feedback received') NOT NULL,
`description` TEXT NOT NULL,
`category` TEXT NOT NULL,
`images` TEXT,
`worker_id` INTEGER,
`created` DATETIME DEFAULT CURRENT_TIMESTAMP,
`modified` DATETIME ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`aindex`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;

CREATE TABLE `worker`
(
`aindex` INTEGER AUTO_INCREMENT,
`name` TEXT,
`role` TEXT,
PRIMARY KEY (`aindex`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 PACK_KEYS=1;
