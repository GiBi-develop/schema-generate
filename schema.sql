CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `email` varchar(255) DEFAULT NULL,
    `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;

CREATE TABLE `order` (
     `id` bigint NOT NULL AUTO_INCREMENT,
     `user_id` int NOT NULL,
     `total_price` decimal(10,2) DEFAULT 0.00,
     PRIMARY KEY (`id`),
     CONSTRAINT `fk_order_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB;
