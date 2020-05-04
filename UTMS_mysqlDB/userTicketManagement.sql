CREATE TABLE `cPanelUser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT '',
  `password` varchar(100) DEFAULT '',
  PRIMARY KEY (`id`)
)

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total_price` varchar(50) DEFAULT NULL,
  `total_tickets` varchar(100) DEFAULT '0',
  `payment_method` varchar(100) DEFAULT '',
  `card_number` varchar(25) DEFAULT '',
  `fullname` varchar(200) DEFAULT '',
  `expiry_date` varchar(100) DEFAULT '',
  `sec_number` varchar(15) DEFAULT '',
  PRIMARY KEY (`payment_id`)
)

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT '',
  `last_name` varchar(100) DEFAULT '',
  `Joined` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) 