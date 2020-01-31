# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.20)
# Database: edu_component_eklenmis
# Generation Time: 2019-04-01 14:39:45 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_classroom
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_classroom`;

CREATE TABLE `companies_classroom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `year` smallint(5) unsigned NOT NULL,
  `grade` smallint(5) unsigned NOT NULL,
  `department_id` smallint(5) unsigned NOT NULL,
  `active` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `companies_classroom_school_id_16ec8db1_fk_companies_school_id` (`school_id`),
  CONSTRAINT `companies_classroom_school_id_16ec8db1_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_classroom_lesson
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_classroom_lesson`;

CREATE TABLE `companies_classroom_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_classroom__classroom_id_f4ce8f89_fk_companies` (`classroom_id`),
  KEY `companies_classroom__lesson_id_b6b57555_fk_companies` (`lesson_id`),
  CONSTRAINT `companies_classroom__classroom_id_f4ce8f89_fk_companies` FOREIGN KEY (`classroom_id`) REFERENCES `companies_classroom` (`id`),
  CONSTRAINT `companies_classroom__lesson_id_b6b57555_fk_companies` FOREIGN KEY (`lesson_id`) REFERENCES `companies_school_lesson_teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_classroom_student
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_classroom_student`;

CREATE TABLE `companies_classroom_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_classroom__classroom_id_fbd1fe0c_fk_companies` (`classroom_id`),
  KEY `companies_classroom_student_student_id_990f0a82_fk_users_user_id` (`student_id`),
  CONSTRAINT `companies_classroom__classroom_id_fbd1fe0c_fk_companies` FOREIGN KEY (`classroom_id`) REFERENCES `companies_classroom` (`id`),
  CONSTRAINT `companies_classroom_student_student_id_990f0a82_fk_users_user_id` FOREIGN KEY (`student_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_classroom_teacher
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_classroom_teacher`;

CREATE TABLE `companies_classroom_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_classroom__classroom_id_ae16d0a7_fk_companies` (`classroom_id`),
  KEY `companies_classroom_teacher_teacher_id_da93377d_fk_users_user_id` (`teacher_id`),
  CONSTRAINT `companies_classroom__classroom_id_ae16d0a7_fk_companies` FOREIGN KEY (`classroom_id`) REFERENCES `companies_classroom` (`id`),
  CONSTRAINT `companies_classroom_teacher_teacher_id_da93377d_fk_users_user_id` FOREIGN KEY (`teacher_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_companygroup
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_companygroup`;

CREATE TABLE `companies_companygroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `slug` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `companies_companygroup_user_id_64fa57cc_fk_users_user_id` (`user_id`),
  CONSTRAINT `companies_companygroup_user_id_64fa57cc_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_lesson
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_lesson`;

CREATE TABLE `companies_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `curricula_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `companies_lesson_curricula_id_f7a7e680_fk_curricula` (`curricula_id`),
  KEY `companies_lesson_school_id_4fb884bd_fk_companies_school_id` (`school_id`),
  CONSTRAINT `companies_lesson_curricula_id_f7a7e680_fk_curricula` FOREIGN KEY (`curricula_id`) REFERENCES `curricula_learning_lesson` (`id`),
  CONSTRAINT `companies_lesson_school_id_4fb884bd_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school`;

CREATE TABLE `companies_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `active` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `slug` varchar(50) NOT NULL,
  `address` longtext,
  `code` varchar(255) DEFAULT NULL,
  `group_id` int(11) NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `companies_school_group_id_9964c643_fk_companies_companygroup_id` (`group_id`),
  KEY `companies_school_type_id_b902d1e3_fk_companies_school_type_id` (`type_id`),
  CONSTRAINT `companies_school_group_id_9964c643_fk_companies_companygroup_id` FOREIGN KEY (`group_id`) REFERENCES `companies_companygroup` (`id`),
  CONSTRAINT `companies_school_type_id_b902d1e3_fk_companies_school_type_id` FOREIGN KEY (`type_id`) REFERENCES `companies_school_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_book
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_book`;

CREATE TABLE `companies_school_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_book_book_id_f1b6929a_fk_publishers_book_id` (`book_id`),
  KEY `companies_school_book_school_id_62bc7870_fk_companies_school_id` (`school_id`),
  CONSTRAINT `companies_school_book_book_id_f1b6929a_fk_publishers_book_id` FOREIGN KEY (`book_id`) REFERENCES `publishers_book` (`id`),
  CONSTRAINT `companies_school_book_school_id_62bc7870_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_lesson_teacher
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_lesson_teacher`;

CREATE TABLE `companies_school_lesson_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `duration` smallint(5) unsigned NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_les_lesson_id_86585cb9_fk_companies` (`lesson_id`),
  KEY `companies_school_les_teacher_id_45fab76a_fk_companies` (`teacher_id`),
  CONSTRAINT `companies_school_les_lesson_id_86585cb9_fk_companies` FOREIGN KEY (`lesson_id`) REFERENCES `companies_lesson` (`id`),
  CONSTRAINT `companies_school_les_teacher_id_45fab76a_fk_companies` FOREIGN KEY (`teacher_id`) REFERENCES `companies_school_teacher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_manager
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_manager`;

CREATE TABLE `companies_school_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_manager_manager_id_f53a902e_fk_users_user_id` (`manager_id`),
  KEY `companies_school_man_school_id_4e91040c_fk_companies` (`school_id`),
  CONSTRAINT `companies_school_man_school_id_4e91040c_fk_companies` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`),
  CONSTRAINT `companies_school_manager_manager_id_f53a902e_fk_users_user_id` FOREIGN KEY (`manager_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_student
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_student`;

CREATE TABLE `companies_school_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_stu_school_id_477ef099_fk_companies` (`school_id`),
  KEY `companies_school_student_student_id_dcfc7655_fk_users_user_id` (`student_id`),
  CONSTRAINT `companies_school_stu_school_id_477ef099_fk_companies` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`),
  CONSTRAINT `companies_school_student_student_id_dcfc7655_fk_users_user_id` FOREIGN KEY (`student_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_teacher
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_teacher`;

CREATE TABLE `companies_school_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_tea_school_id_27d7eed8_fk_companies` (`school_id`),
  KEY `companies_school_teacher_teacher_id_a8271b7c_fk_users_user_id` (`teacher_id`),
  CONSTRAINT `companies_school_tea_school_id_27d7eed8_fk_companies` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`),
  CONSTRAINT `companies_school_teacher_teacher_id_a8271b7c_fk_users_user_id` FOREIGN KEY (`teacher_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_test
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_test`;

CREATE TABLE `companies_school_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_test_school_id_732507ec_fk_companies_school_id` (`school_id`),
  KEY `companies_school_test_test_id_1282bee4_fk_tests_test_id` (`test_id`),
  CONSTRAINT `companies_school_test_school_id_732507ec_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`),
  CONSTRAINT `companies_school_test_test_id_1282bee4_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_type`;

CREATE TABLE `companies_school_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table companies_school_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `companies_school_user`;

CREATE TABLE `companies_school_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_school_user_school_id_460b1ad8_fk_companies_school_id` (`school_id`),
  KEY `companies_school_user_user_id_493bf4f6_fk_users_user_id` (`user_id`),
  CONSTRAINT `companies_school_user_school_id_460b1ad8_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`),
  CONSTRAINT `companies_school_user_user_id_493bf4f6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component`;

CREATE TABLE `components_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `level` smallint(6) NOT NULL,
  `active` smallint(6) NOT NULL DEFAULT '1',
  `group` smallint(6) NOT NULL DEFAULT '0',
  `seconds` smallint(6) NOT NULL DEFAULT '0',
  `file` longtext,
  `created` date NOT NULL DEFAULT '2017-02-07',
  `updated` date NOT NULL DEFAULT '2017-02-07',
  `edu_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_edu_category_id_652f310f_fk_educatego` (`edu_category_id`),
  CONSTRAINT `components_component_edu_category_id_652f310f_fk_educatego` FOREIGN KEY (`edu_category_id`) REFERENCES `educategories_edu_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component_answer_stat
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component_answer_stat`;

CREATE TABLE `components_component_answer_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_is_true` smallint(6) NOT NULL,
  `answer_is_empty` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `component_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `test_unique_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_component_id_823403c2_fk_component` (`component_id`),
  KEY `components_component_question_id_46db15a1_fk_questions` (`question_id`),
  KEY `components_component_test_unique_id_d57a81b7_fk_tests_tes` (`test_unique_id`),
  KEY `components_component_user_id_f2716a34_fk_users_use` (`user_id`),
  CONSTRAINT `components_component_component_id_823403c2_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `components_component_question_id_46db15a1_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `components_component_test_unique_id_d57a81b7_fk_tests_tes` FOREIGN KEY (`test_unique_id`) REFERENCES `tests_test_unique` (`id`),
  CONSTRAINT `components_component_user_id_f2716a34_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component_component
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component_component`;

CREATE TABLE `components_component_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component_id` int(11) NOT NULL,
  `parent_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_component_id_5a9cbc84_fk_component` (`component_id`),
  KEY `components_component_parent_id_7cc07a92_fk_component` (`parent_id`),
  CONSTRAINT `components_component_component_id_5a9cbc84_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `components_component_parent_id_7cc07a92_fk_component` FOREIGN KEY (`parent_id`) REFERENCES `components_component` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component_question_answer
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component_question_answer`;

CREATE TABLE `components_component_question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component_ok` smallint(6) NOT NULL,
  `created` date NOT NULL DEFAULT '2017-02-07',
  `updated` date NOT NULL DEFAULT '2017-02-07',
  `component_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_component_id_13921f7f_fk_component` (`component_id`),
  KEY `components_component_question_answer_id_19b8a421_fk_questions` (`question_answer_id`),
  CONSTRAINT `components_component_component_id_13921f7f_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `components_component_question_answer_id_19b8a421_fk_questions` FOREIGN KEY (`question_answer_id`) REFERENCES `questions_question_answer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component_stat
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component_stat`;

CREATE TABLE `components_component_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component_status` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `component_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_component_id_36ecfda2_fk_component` (`component_id`),
  KEY `components_component_stat_user_id_77678602_fk_users_user_id` (`user_id`),
  CONSTRAINT `components_component_component_id_36ecfda2_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `components_component_stat_user_id_77678602_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table components_component_status_change
# ------------------------------------------------------------

DROP TABLE IF EXISTS `components_component_status_change`;

CREATE TABLE `components_component_status_change` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `old_status` smallint(6) NOT NULL,
  `new_status` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `component_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `components_component_component_id_cdcaf691_fk_component` (`component_id`),
  KEY `components_component_user_id_b04476eb_fk_users_use` (`user_id`),
  CONSTRAINT `components_component_component_id_cdcaf691_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `components_component_user_id_b04476eb_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_domain
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_domain`;

CREATE TABLE `curricula_learning_domain` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `position` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_domain_slug_e74df5c0` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture`;

CREATE TABLE `curricula_learning_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `summary` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `position` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `practice_id` int(11) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_l_content_type_id_bdeebe91_fk_django_co` (`content_type_id`),
  KEY `curricula_learning_lecture_practice_id_98532f74_fk_tests_test_id` (`practice_id`),
  KEY `curricula_learning_l_subject_id_e8e73f6b_fk_curricula` (`subject_id`),
  KEY `curricula_learning_l_publisher_id_a3181547_fk_publisher` (`publisher_id`),
  KEY `curricula_learning_lecture_slug_464f5220` (`slug`),
  CONSTRAINT `curricula_learning_l_content_type_id_bdeebe91_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `curricula_learning_l_publisher_id_a3181547_fk_publisher` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`),
  CONSTRAINT `curricula_learning_l_subject_id_e8e73f6b_fk_curricula` FOREIGN KEY (`subject_id`) REFERENCES `curricula_learning_subject` (`id`),
  CONSTRAINT `curricula_learning_lecture_practice_id_98532f74_fk_tests_test_id` FOREIGN KEY (`practice_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_component
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_component`;

CREATE TABLE `curricula_learning_lecture_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learninglecture_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `curricula_learning_lectu_learninglecture_id_compo_7be4a7f4_uniq` (`learninglecture_id`,`component_id`),
  KEY `curricula_learning_l_component_id_3ee5e60a_fk_component` (`component_id`),
  CONSTRAINT `curricula_learning_l_component_id_3ee5e60a_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `curricula_learning_l_learninglecture_id_d4a671d5_fk_curricula` FOREIGN KEY (`learninglecture_id`) REFERENCES `curricula_learning_lecture` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_livescribe
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_livescribe`;

CREATE TABLE `curricula_learning_lecture_livescribe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `media_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_l_media_id_ffd15130_fk_library_m` (`media_id`),
  CONSTRAINT `curricula_learning_l_media_id_ffd15130_fk_library_m` FOREIGN KEY (`media_id`) REFERENCES `library_media` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_stat
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_stat`;

CREATE TABLE `curricula_learning_lecture_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lecture_status` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `lecture_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `practice_status` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_l_lecture_id_1d4b04e6_fk_curricula` (`lecture_id`),
  KEY `curricula_learning_l_user_id_baf8184b_fk_users_use` (`user_id`),
  CONSTRAINT `curricula_learning_l_lecture_id_1d4b04e6_fk_curricula` FOREIGN KEY (`lecture_id`) REFERENCES `curricula_learning_lecture` (`id`),
  CONSTRAINT `curricula_learning_l_user_id_baf8184b_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_tag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_tag`;

CREATE TABLE `curricula_learning_lecture_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learninglecture_id` int(11) NOT NULL,
  `learningtag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `curricula_learning_lectu_learninglecture_id_learn_4e543de8_uniq` (`learninglecture_id`,`learningtag_id`),
  KEY `curricula_learning_l_learningtag_id_d83dbf96_fk_curricula` (`learningtag_id`),
  CONSTRAINT `curricula_learning_l_learninglecture_id_e8fe1092_fk_curricula` FOREIGN KEY (`learninglecture_id`) REFERENCES `curricula_learning_lecture` (`id`),
  CONSTRAINT `curricula_learning_l_learningtag_id_d83dbf96_fk_curricula` FOREIGN KEY (`learningtag_id`) REFERENCES `curricula_learning_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_text
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_text`;

CREATE TABLE `curricula_learning_lecture_text` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `content` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_video
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_video`;

CREATE TABLE `curricula_learning_lecture_video` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `media_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_l_media_id_b9d3519e_fk_library_m` (`media_id`),
  CONSTRAINT `curricula_learning_l_media_id_b9d3519e_fk_library_m` FOREIGN KEY (`media_id`) REFERENCES `library_media` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lecture_youtube
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lecture_youtube`;

CREATE TABLE `curricula_learning_lecture_youtube` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `name` varchar(255) NOT NULL,
  `desc` longtext NOT NULL,
  `file` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_lesson
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_lesson`;

CREATE TABLE `curricula_learning_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `active` smallint(5) unsigned NOT NULL,
  `public` smallint(5) unsigned NOT NULL,
  `duration` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `edu_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_lesson_slug_e71b329f` (`slug`),
  KEY `curricula_learning_l_edu_category_id_d5589443_fk_educatego` (`edu_category_id`),
  CONSTRAINT `curricula_learning_l_edu_category_id_d5589443_fk_educatego` FOREIGN KEY (`edu_category_id`) REFERENCES `educategories_edu_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_subject
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_subject`;

CREATE TABLE `curricula_learning_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `position` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `unit_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_subject_slug_7e0f142a` (`slug`),
  KEY `curricula_learning_s_unit_id_9ba3d4e8_fk_curricula` (`unit_id`),
  CONSTRAINT `curricula_learning_s_unit_id_9ba3d4e8_fk_curricula` FOREIGN KEY (`unit_id`) REFERENCES `curricula_learning_unit` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_tag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_tag`;

CREATE TABLE `curricula_learning_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_tag_slug_6c278311` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_test
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_test`;

CREATE TABLE `curricula_learning_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `position` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_test_slug_92f4f96a` (`slug`),
  KEY `curricula_learning_t_content_type_id_2949fb39_fk_django_co` (`content_type_id`),
  KEY `curricula_learning_test_test_id_d32c8d00_fk_tests_test_id` (`test_id`),
  CONSTRAINT `curricula_learning_t_content_type_id_2949fb39_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `curricula_learning_test_test_id_d32c8d00_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_test_unique
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_test_unique`;

CREATE TABLE `curricula_learning_test_unique` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `learning_test_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_t_learning_test_id_ffaaf953_fk_curricula` (`learning_test_id`),
  KEY `curricula_learning_test_unique_user_id_d45c72b0_fk_users_user_id` (`user_id`),
  CONSTRAINT `curricula_learning_t_learning_test_id_ffaaf953_fk_curricula` FOREIGN KEY (`learning_test_id`) REFERENCES `curricula_learning_test` (`id`),
  CONSTRAINT `curricula_learning_test_unique_user_id_d45c72b0_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_unit
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_unit`;

CREATE TABLE `curricula_learning_unit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` longtext NOT NULL,
  `position` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `domain_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curricula_learning_u_domain_id_a1ebb05f_fk_curricula` (`domain_id`),
  KEY `curricula_learning_u_lesson_id_0e4ca00f_fk_curricula` (`lesson_id`),
  KEY `curricula_learning_unit_slug_ac59d095` (`slug`),
  CONSTRAINT `curricula_learning_u_domain_id_a1ebb05f_fk_curricula` FOREIGN KEY (`domain_id`) REFERENCES `curricula_learning_domain` (`id`),
  CONSTRAINT `curricula_learning_u_lesson_id_0e4ca00f_fk_curricula` FOREIGN KEY (`lesson_id`) REFERENCES `curricula_learning_lesson` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table curricula_learning_unit_component
# ------------------------------------------------------------

DROP TABLE IF EXISTS `curricula_learning_unit_component`;

CREATE TABLE `curricula_learning_unit_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `learningunit_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `curricula_learning_unit__learningunit_id_componen_44761f33_uniq` (`learningunit_id`,`component_id`),
  KEY `curricula_learning_u_component_id_a3c4cf51_fk_component` (`component_id`),
  CONSTRAINT `curricula_learning_u_component_id_a3c4cf51_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `curricula_learning_u_learningunit_id_d6ca6eb3_fk_curricula` FOREIGN KEY (`learningunit_id`) REFERENCES `curricula_learning_unit` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table django_migrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table django_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table educategories_edu_categories
# ------------------------------------------------------------

DROP TABLE IF EXISTS `educategories_edu_categories`;

CREATE TABLE `educategories_edu_categories` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `depth` smallint(6) NOT NULL,
  `active` smallint(6) NOT NULL,
  `sort_category` int(11) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `lesson_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `educategories_edu_ca_lesson_id_ae5afb96_fk_educatego` (`lesson_id`),
  KEY `educategories_edu_ca_parent_id_c22ee93c_fk_educatego` (`parent_id`),
  KEY `educategories_edu_ca_subject_id_965d9af3_fk_educatego` (`subject_id`),
  KEY `educategories_edu_ca_unit_id_324cd352_fk_educatego` (`unit_id`),
  KEY `educategories_edu_categories_slug_bb7d6ea5` (`slug`),
  CONSTRAINT `educategories_edu_ca_lesson_id_ae5afb96_fk_educatego` FOREIGN KEY (`lesson_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `educategories_edu_ca_parent_id_c22ee93c_fk_educatego` FOREIGN KEY (`parent_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `educategories_edu_ca_subject_id_965d9af3_fk_educatego` FOREIGN KEY (`subject_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `educategories_edu_ca_unit_id_324cd352_fk_educatego` FOREIGN KEY (`unit_id`) REFERENCES `educategories_edu_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table library_backendperms
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library_backendperms`;

CREATE TABLE `library_backendperms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `view_name` varchar(50) NOT NULL,
  `view_action` varchar(50) NOT NULL,
  `permission_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table library_exam
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library_exam`;

CREATE TABLE `library_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `sort_order` smallint(6) NOT NULL,
  `active` smallint(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table library_media
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library_media`;

CREATE TABLE `library_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `media_name` varchar(255) NOT NULL,
  `media_desc` longtext,
  `date_created` datetime(6) NOT NULL,
  `media_file` varchar(100) NOT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `library_media_publisher_id_2ce64670_fk_publishers_publisher_id` (`publisher_id`),
  CONSTRAINT `library_media_publisher_id_2ce64670_fk_publishers_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table library_province
# ------------------------------------------------------------

DROP TABLE IF EXISTS `library_province`;

CREATE TABLE `library_province` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_book
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_book`;

CREATE TABLE `publishers_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `active` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `publisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `publishers_book_publisher_id_e078663c_fk_publishers_publisher_id` (`publisher_id`),
  CONSTRAINT `publishers_book_publisher_id_e078663c_fk_publishers_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_book_exam
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_book_exam`;

CREATE TABLE `publishers_book_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publishers_book_exam_book_id_exam_id_d8ecbab3_uniq` (`book_id`,`exam_id`),
  KEY `publishers_book_exam_exam_id_3854dbe2_fk_library_exam_id` (`exam_id`),
  CONSTRAINT `publishers_book_exam_book_id_a472275d_fk_publishers_book_id` FOREIGN KEY (`book_id`) REFERENCES `publishers_book` (`id`),
  CONSTRAINT `publishers_book_exam_exam_id_3854dbe2_fk_library_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `library_exam` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_book_lesson
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_book_lesson`;

CREATE TABLE `publishers_book_lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `educategory_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publishers_book_lesson_book_id_educategory_id_0f924288_uniq` (`book_id`,`educategory_id`),
  KEY `publishers_book_less_educategory_id_28d3d7b1_fk_educatego` (`educategory_id`),
  CONSTRAINT `publishers_book_less_educategory_id_28d3d7b1_fk_educatego` FOREIGN KEY (`educategory_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `publishers_book_lesson_book_id_24a017ca_fk_publishers_book_id` FOREIGN KEY (`book_id`) REFERENCES `publishers_book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_publisher
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_publisher`;

CREATE TABLE `publishers_publisher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `active` smallint(5) unsigned NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `publishers_publisher_group_id_fbf18a36_fk_companies` (`group_id`),
  CONSTRAINT `publishers_publisher_group_id_fbf18a36_fk_companies` FOREIGN KEY (`group_id`) REFERENCES `companies_companygroup` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_publisher_manager
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_publisher_manager`;

CREATE TABLE `publishers_publisher_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_id` int(11) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `publishers_publisher_manager_id_1e225153_fk_users_use` (`manager_id`),
  KEY `publishers_publisher_publisher_id_a3110248_fk_publisher` (`publisher_id`),
  CONSTRAINT `publishers_publisher_manager_id_1e225153_fk_users_use` FOREIGN KEY (`manager_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `publishers_publisher_publisher_id_a3110248_fk_publisher` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_source
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_source`;

CREATE TABLE `publishers_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `sort_order` smallint(6) NOT NULL,
  `active` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `book_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `publishers_source_book_id_229f954f_fk_publishers_book_id` (`book_id`),
  KEY `publishers_source_parent_id_d45082f2_fk_publishers_source_id` (`parent_id`),
  CONSTRAINT `publishers_source_book_id_229f954f_fk_publishers_book_id` FOREIGN KEY (`book_id`) REFERENCES `publishers_book` (`id`),
  CONSTRAINT `publishers_source_parent_id_d45082f2_fk_publishers_source_id` FOREIGN KEY (`parent_id`) REFERENCES `publishers_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table publishers_source_question
# ------------------------------------------------------------

DROP TABLE IF EXISTS `publishers_source_question`;

CREATE TABLE `publishers_source_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publishers_source_question_source_id_question_id_e870b303_uniq` (`source_id`,`question_id`),
  KEY `publishers_source_qu_question_id_885d0d2e_fk_questions` (`question_id`),
  CONSTRAINT `publishers_source_qu_question_id_885d0d2e_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `publishers_source_qu_source_id_65f23bd4_fk_publisher` FOREIGN KEY (`source_id`) REFERENCES `publishers_source` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question`;

CREATE TABLE `questions_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `seconds` smallint(6) NOT NULL DEFAULT '0',
  `level` smallint(6) NOT NULL DEFAULT '0',
  `question_start_type` smallint(6) DEFAULT NULL,
  `question_start_value` longtext,
  `question_answer_type` smallint(6) DEFAULT NULL,
  `question_answer_value` longtext,
  `question_pattern` smallint(6) NOT NULL,
  `active` smallint(6) NOT NULL DEFAULT '1',
  `created` date NOT NULL DEFAULT '2017-02-07',
  `updated` date NOT NULL DEFAULT '2017-02-07',
  `edu_category_id` int(11) DEFAULT NULL,
  `question_unique_id` int(11) DEFAULT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_question_edu_category_id_ed35c9e7_fk_educatego` (`edu_category_id`),
  KEY `questions_question_question_unique_id_a2c70c20_fk_questions` (`question_unique_id`),
  KEY `questions_question_publisher_id_07c65a3c_fk_publisher` (`publisher_id`),
  CONSTRAINT `questions_question_edu_category_id_ed35c9e7_fk_educatego` FOREIGN KEY (`edu_category_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `questions_question_publisher_id_07c65a3c_fk_publisher` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`),
  CONSTRAINT `questions_question_question_unique_id_a2c70c20_fk_questions` FOREIGN KEY (`question_unique_id`) REFERENCES `questions_question_unique` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_answer
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_answer`;

CREATE TABLE `questions_question_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_type` smallint(6) NOT NULL,
  `answer_value` longtext NOT NULL,
  `answer_choice` smallint(6) DEFAULT NULL,
  `is_true_answer` smallint(6) NOT NULL,
  `created` date NOT NULL DEFAULT '2017-02-07',
  `updated` date NOT NULL DEFAULT '2017-02-07',
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_question_a_question_id_f82b8c7a_fk_questions` (`question_id`),
  CONSTRAINT `questions_question_a_question_id_f82b8c7a_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_answer_stat
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_answer_stat`;

CREATE TABLE `questions_question_answer_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_is_true` smallint(6) NOT NULL,
  `answer_seconds` smallint(6) NOT NULL,
  `answer_type` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `question_id` int(11) NOT NULL,
  `question_answer_id` int(11) NOT NULL,
  `test_unique_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_question_a_question_id_8ca19f07_fk_questions` (`question_id`),
  KEY `questions_question_a_question_answer_id_e70b9297_fk_questions` (`question_answer_id`),
  KEY `questions_question_a_test_unique_id_7db72336_fk_tests_tes` (`test_unique_id`),
  KEY `questions_question_answer_stat_user_id_77d8bca4_fk_users_user_id` (`user_id`),
  CONSTRAINT `questions_question_a_question_answer_id_e70b9297_fk_questions` FOREIGN KEY (`question_answer_id`) REFERENCES `questions_question_answer` (`id`),
  CONSTRAINT `questions_question_a_question_id_8ca19f07_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `questions_question_a_test_unique_id_7db72336_fk_tests_tes` FOREIGN KEY (`test_unique_id`) REFERENCES `tests_test_unique` (`id`),
  CONSTRAINT `questions_question_answer_stat_user_id_77d8bca4_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_book
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_book`;

CREATE TABLE `questions_question_book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `questions_question_book_question_id_book_id_75e14fd6_uniq` (`question_id`,`book_id`),
  KEY `questions_question_book_book_id_dc6b34f8_fk_publishers_book_id` (`book_id`),
  CONSTRAINT `questions_question_b_question_id_56539a2e_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `questions_question_book_book_id_dc6b34f8_fk_publishers_book_id` FOREIGN KEY (`book_id`) REFERENCES `publishers_book` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_component
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_component`;

CREATE TABLE `questions_question_component` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) NOT NULL,
  `component_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `questions_question_compo_question_id_component_id_22bdcd09_uniq` (`question_id`,`component_id`),
  KEY `questions_question_c_component_id_d7d85f55_fk_component` (`component_id`),
  CONSTRAINT `questions_question_c_component_id_d7d85f55_fk_component` FOREIGN KEY (`component_id`) REFERENCES `components_component` (`id`),
  CONSTRAINT `questions_question_c_question_id_a97e97ae_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_exam
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_exam`;

CREATE TABLE `questions_question_exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exam_year` smallint(6) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `exam_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_question_exam_exam_id_1cd0eb86_fk_library_exam_id` (`exam_id`),
  KEY `questions_question_e_question_id_d0f6a917_fk_questions` (`question_id`),
  CONSTRAINT `questions_question_e_question_id_d0f6a917_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `questions_question_exam_exam_id_1cd0eb86_fk_library_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `library_exam` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_unique
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_unique`;

CREATE TABLE `questions_question_unique` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_code` varchar(255) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_question_unique_stat
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_question_unique_stat`;

CREATE TABLE `questions_question_unique_stat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_code` varchar(255) NOT NULL,
  `status` smallint(6) NOT NULL,
  `answers` longtext NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `question_unique_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_question_u_question_unique_id_9402a4c2_fk_questions` (`question_unique_id`),
  KEY `questions_question_unique_stat_user_id_82e20f73_fk_users_user_id` (`user_id`),
  CONSTRAINT `questions_question_u_question_unique_id_9402a4c2_fk_questions` FOREIGN KEY (`question_unique_id`) REFERENCES `questions_question_unique` (`id`),
  CONSTRAINT `questions_question_unique_stat_user_id_82e20f73_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table questions_user_question_answers
# ------------------------------------------------------------

DROP TABLE IF EXISTS `questions_user_question_answers`;

CREATE TABLE `questions_user_question_answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer` varchar(255) NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `check` smallint(6) NOT NULL,
  `question_id` int(11) NOT NULL,
  `source_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `questions_user_quest_question_id_e3f669eb_fk_questions` (`question_id`),
  KEY `questions_user_quest_source_id_936d5661_fk_publisher` (`source_id`),
  KEY `questions_user_quest_user_id_154e33dc_fk_users_use` (`user_id`),
  CONSTRAINT `questions_user_quest_question_id_e3f669eb_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `questions_user_quest_source_id_936d5661_fk_publisher` FOREIGN KEY (`source_id`) REFERENCES `publishers_source` (`id`),
  CONSTRAINT `questions_user_quest_user_id_154e33dc_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_report
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_report`;

CREATE TABLE `tests_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report` longtext NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_report_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_report_type`;

CREATE TABLE `tests_report_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `report_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tests_report_type_report_id_f5f29afc_fk_tests_report_id` (`report_id`),
  KEY `tests_report_type_test_id_d82c6cc9_fk_tests_test_id` (`test_id`),
  CONSTRAINT `tests_report_type_report_id_f5f29afc_fk_tests_report_id` FOREIGN KEY (`report_id`) REFERENCES `tests_report` (`id`),
  CONSTRAINT `tests_report_type_test_id_d82c6cc9_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_test
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_test`;

CREATE TABLE `tests_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `test_seconds` smallint(6) NOT NULL,
  `test_start` longtext NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `active` smallint(6) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  `test_type_id` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tests_test_publisher_id_f0e89aad_fk_publishers_publisher_id` (`publisher_id`),
  CONSTRAINT `tests_test_publisher_id_f0e89aad_fk_publishers_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `publishers_publisher` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_test_edu_category
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_test_edu_category`;

CREATE TABLE `tests_test_edu_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL,
  `educategory_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tests_test_edu_category_test_id_educategory_id_efe9d81e_uniq` (`test_id`,`educategory_id`),
  KEY `tests_test_edu_categ_educategory_id_ddf6b759_fk_educatego` (`educategory_id`),
  CONSTRAINT `tests_test_edu_categ_educategory_id_ddf6b759_fk_educatego` FOREIGN KEY (`educategory_id`) REFERENCES `educategories_edu_categories` (`id`),
  CONSTRAINT `tests_test_edu_category_test_id_7328c4e2_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_test_question
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_test_question`;

CREATE TABLE `tests_test_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `test_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tests_test_question_test_id_question_id_19a8e377_uniq` (`test_id`,`question_id`),
  KEY `tests_test_question_question_id_bee89eed_fk_questions` (`question_id`),
  CONSTRAINT `tests_test_question_question_id_bee89eed_fk_questions` FOREIGN KEY (`question_id`) REFERENCES `questions_question` (`id`),
  CONSTRAINT `tests_test_question_test_id_f053d72d_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table tests_test_unique
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tests_test_unique`;

CREATE TABLE `tests_test_unique` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `report` longtext NOT NULL,
  `created` date NOT NULL,
  `updated` date NOT NULL,
  `test_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tests_test_unique_test_id_e72cdd0b_fk_tests_test_id` (`test_id`),
  KEY `tests_test_unique_user_id_14eaa6d0_fk_users_user_id` (`user_id`),
  CONSTRAINT `tests_test_unique_test_id_e72cdd0b_fk_tests_test_id` FOREIGN KEY (`test_id`) REFERENCES `tests_test` (`id`),
  CONSTRAINT `tests_test_unique_user_id_14eaa6d0_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users_pattern
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_pattern`;

CREATE TABLE `users_pattern` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `object_id` int(10) unsigned NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_pattern_content_type_id_12f1c9d5_fk_django_content_type_id` (`content_type_id`),
  KEY `users_pattern_role_id_ae425730_fk_users_user_group_id` (`role_id`),
  CONSTRAINT `users_pattern_content_type_id_12f1c9d5_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `users_pattern_role_id_ae425730_fk_users_user_group_id` FOREIGN KEY (`role_id`) REFERENCES `users_user_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_user`;

CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `identity_number` varchar(25) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `phone` varchar(30) NOT NULL,
  `password_reset_token` varchar(255) NOT NULL,
  `register_email_activate_token` varchar(255) NOT NULL,
  `blocked_token` varchar(255) NOT NULL,
  `country` smallint(5) unsigned NOT NULL,
  `city` smallint(5) unsigned NOT NULL,
  `captcha_count` smallint(5) unsigned NOT NULL,
  `is_blocked` smallint(5) unsigned NOT NULL,
  `jwt_secret` char(32) NOT NULL,
  `email` varchar(254) NOT NULL,
  `school_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `identity_number` (`identity_number`),
  UNIQUE KEY `email` (`email`),
  KEY `users_user_school_id_e82aaa0a_fk_companies_school_id` (`school_id`),
  CONSTRAINT `users_user_school_id_e82aaa0a_fk_companies_school_id` FOREIGN KEY (`school_id`) REFERENCES `companies_school` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users_user_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_user_group`;

CREATE TABLE `users_user_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page` varchar(255) NOT NULL,
  `group_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_user_group_group_id_43f40a6e_fk_auth_group_id` (`group_id`),
  KEY `users_user_group_user_id_1577467e_fk_users_user_id` (`user_id`),
  CONSTRAINT `users_user_group_group_id_43f40a6e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_group_user_id_1577467e_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_user_user_permissions`;

CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table users_userprofile
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_userprofile`;

CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_userprofile_user_id_87251ef1_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
