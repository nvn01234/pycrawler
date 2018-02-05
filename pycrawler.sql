/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : pycrawler

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-02-06 01:04:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for isi_documents
-- ----------------------------
DROP TABLE IF EXISTS `isi_documents`;
CREATE TABLE `isi_documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abstract` longtext CHARACTER SET utf8,
  `address` longtext CHARACTER SET utf8,
  `affiliation` longtext CHARACTER SET utf8,
  `article_number` longtext CHARACTER SET utf8,
  `author` longtext CHARACTER SET utf8,
  `author_email` longtext CHARACTER SET utf8,
  `booktitle` longtext CHARACTER SET utf8,
  `book_author` longtext CHARACTER SET utf8,
  `cited_references` longtext CHARACTER SET utf8,
  `da` longtext CHARACTER SET utf8,
  `doc_delivery_number` longtext CHARACTER SET utf8,
  `doi` longtext CHARACTER SET utf8,
  `editor` longtext CHARACTER SET utf8,
  `eissn` longtext CHARACTER SET utf8,
  `funding_acknowledgement` longtext CHARACTER SET utf8,
  `funding_text` longtext CHARACTER SET utf8,
  `isbn` longtext CHARACTER SET utf8,
  `issn` longtext CHARACTER SET utf8,
  `journal` longtext CHARACTER SET utf8,
  `journal_iso` longtext CHARACTER SET utf8,
  `keyword` longtext CHARACTER SET utf8,
  `keywords_plus` longtext CHARACTER SET utf8,
  `language` longtext CHARACTER SET utf8,
  `meeting` longtext CHARACTER SET utf8,
  `month` longtext CHARACTER SET utf8,
  `note` longtext CHARACTER SET utf8,
  `number` longtext CHARACTER SET utf8,
  `number_of_cited_references` longtext CHARACTER SET utf8,
  `oa` longtext CHARACTER SET utf8,
  `orcid_numbers` longtext CHARACTER SET utf8,
  `organization` longtext CHARACTER SET utf8,
  `pages` longtext CHARACTER SET utf8,
  `publisher` longtext CHARACTER SET utf8,
  `researcherid_numbers` longtext CHARACTER SET utf8,
  `research_areas` longtext CHARACTER SET utf8,
  `series` longtext CHARACTER SET utf8,
  `times_cited` longtext CHARACTER SET utf8,
  `title` longtext CHARACTER SET utf8,
  `type` longtext CHARACTER SET utf8,
  `unique_id` longtext CHARACTER SET utf8,
  `usage_count_last_180_days` longtext CHARACTER SET utf8,
  `usage_count_since_2013` longtext CHARACTER SET utf8,
  `volume` longtext CHARACTER SET utf8,
  `web_of_science_categories` longtext CHARACTER SET utf8,
  `year` longtext CHARACTER SET utf8,
  `authors_json` longtext CHARACTER SET utf8,
  `start` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32567 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for isi_documents_2017
-- ----------------------------
DROP TABLE IF EXISTS `isi_documents_2017`;
CREATE TABLE `isi_documents_2017` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abstract` longtext CHARACTER SET utf8,
  `address` longtext CHARACTER SET utf8,
  `affiliation` longtext CHARACTER SET utf8,
  `article_number` longtext CHARACTER SET utf8,
  `author` longtext CHARACTER SET utf8,
  `author_email` longtext CHARACTER SET utf8,
  `booktitle` longtext CHARACTER SET utf8,
  `book_author` longtext CHARACTER SET utf8,
  `cited_references` longtext CHARACTER SET utf8,
  `da` longtext CHARACTER SET utf8,
  `doc_delivery_number` longtext CHARACTER SET utf8,
  `doi` longtext CHARACTER SET utf8,
  `editor` longtext CHARACTER SET utf8,
  `eissn` longtext CHARACTER SET utf8,
  `funding_acknowledgement` longtext CHARACTER SET utf8,
  `funding_text` longtext CHARACTER SET utf8,
  `isbn` longtext CHARACTER SET utf8,
  `issn` longtext CHARACTER SET utf8,
  `journal` longtext CHARACTER SET utf8,
  `journal_iso` longtext CHARACTER SET utf8,
  `keyword` longtext CHARACTER SET utf8,
  `keywords_plus` longtext CHARACTER SET utf8,
  `language` longtext CHARACTER SET utf8,
  `meeting` longtext CHARACTER SET utf8,
  `month` longtext CHARACTER SET utf8,
  `note` longtext CHARACTER SET utf8,
  `number` longtext CHARACTER SET utf8,
  `number_of_cited_references` longtext CHARACTER SET utf8,
  `oa` longtext CHARACTER SET utf8,
  `orcid_numbers` longtext CHARACTER SET utf8,
  `organization` longtext CHARACTER SET utf8,
  `pages` longtext CHARACTER SET utf8,
  `publisher` longtext CHARACTER SET utf8,
  `researcherid_numbers` longtext CHARACTER SET utf8,
  `research_areas` longtext CHARACTER SET utf8,
  `series` longtext CHARACTER SET utf8,
  `times_cited` longtext CHARACTER SET utf8,
  `title` longtext CHARACTER SET utf8,
  `type` longtext CHARACTER SET utf8,
  `unique_id` longtext CHARACTER SET utf8,
  `usage_count_last_180_days` longtext CHARACTER SET utf8,
  `usage_count_since_2013` longtext CHARACTER SET utf8,
  `volume` longtext CHARACTER SET utf8,
  `web_of_science_categories` longtext CHARACTER SET utf8,
  `year` longtext CHARACTER SET utf8,
  `authors_json` longtext CHARACTER SET utf8,
  `start` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4813 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for isi_keys
-- ----------------------------
DROP TABLE IF EXISTS `isi_keys`;
CREATE TABLE `isi_keys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for isi_paginate
-- ----------------------------
DROP TABLE IF EXISTS `isi_paginate`;
CREATE TABLE `isi_paginate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` int(11) DEFAULT NULL,
  `end` int(11) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `key_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for scopus_documents
-- ----------------------------
DROP TABLE IF EXISTS `scopus_documents`;
CREATE TABLE `scopus_documents` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authors` longtext CHARACTER SET utf8,
  `title` longtext CHARACTER SET utf8,
  `year` longtext CHARACTER SET utf8,
  `source_title` longtext CHARACTER SET utf8,
  `volume` longtext CHARACTER SET utf8,
  `issue` longtext CHARACTER SET utf8,
  `art_no` longtext CHARACTER SET utf8,
  `page_start` longtext CHARACTER SET utf8,
  `page_end` longtext CHARACTER SET utf8,
  `page_count` longtext CHARACTER SET utf8,
  `cited_by` longtext CHARACTER SET utf8,
  `doi` longtext CHARACTER SET utf8,
  `link` longtext CHARACTER SET utf8,
  `affiliations` longtext CHARACTER SET utf8,
  `authors_with_affiliations` longtext CHARACTER SET utf8,
  `abstract` longtext CHARACTER SET utf8,
  `author_keywords` longtext CHARACTER SET utf8,
  `index_keywords` longtext CHARACTER SET utf8,
  `molecular_sequence_numbers` longtext CHARACTER SET utf8,
  `chemicals_cas` longtext CHARACTER SET utf8,
  `tradenames` longtext CHARACTER SET utf8,
  `manufacturers` longtext CHARACTER SET utf8,
  `funding_details` longtext CHARACTER SET utf8,
  `funding_text` longtext CHARACTER SET utf8,
  `references` longtext CHARACTER SET utf8,
  `correspondence_address` longtext CHARACTER SET utf8,
  `editors` longtext CHARACTER SET utf8,
  `sponsors` longtext CHARACTER SET utf8,
  `publisher` longtext CHARACTER SET utf8,
  `conference_name` longtext CHARACTER SET utf8,
  `conference_date` longtext CHARACTER SET utf8,
  `conference_location` longtext CHARACTER SET utf8,
  `conference_code` longtext CHARACTER SET utf8,
  `issn` longtext CHARACTER SET utf8,
  `isbn` longtext CHARACTER SET utf8,
  `coden` longtext CHARACTER SET utf8,
  `pubmed_id` longtext CHARACTER SET utf8,
  `language_of_original_document` longtext CHARACTER SET utf8,
  `abbreviated_source_title` longtext CHARACTER SET utf8,
  `document_type` longtext CHARACTER SET utf8,
  `source` longtext CHARACTER SET utf8,
  `eid` longtext CHARACTER SET utf8,
  `authors_json` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52970 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for scopus_documents_2017
-- ----------------------------
DROP TABLE IF EXISTS `scopus_documents_2017`;
CREATE TABLE `scopus_documents_2017` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `authors` longtext CHARACTER SET utf8,
  `title` longtext CHARACTER SET utf8,
  `year` longtext CHARACTER SET utf8,
  `source_title` longtext CHARACTER SET utf8,
  `volume` longtext CHARACTER SET utf8,
  `issue` longtext CHARACTER SET utf8,
  `art_no` longtext CHARACTER SET utf8,
  `page_start` longtext CHARACTER SET utf8,
  `page_end` longtext CHARACTER SET utf8,
  `page_count` longtext CHARACTER SET utf8,
  `cited_by` longtext CHARACTER SET utf8,
  `doi` longtext CHARACTER SET utf8,
  `link` longtext CHARACTER SET utf8,
  `affiliations` longtext CHARACTER SET utf8,
  `authors_with_affiliations` longtext CHARACTER SET utf8,
  `abstract` longtext CHARACTER SET utf8,
  `author_keywords` longtext CHARACTER SET utf8,
  `index_keywords` longtext CHARACTER SET utf8,
  `molecular_sequence_numbers` longtext CHARACTER SET utf8,
  `chemicals_cas` longtext CHARACTER SET utf8,
  `tradenames` longtext CHARACTER SET utf8,
  `manufacturers` longtext CHARACTER SET utf8,
  `funding_details` longtext CHARACTER SET utf8,
  `funding_text` longtext CHARACTER SET utf8,
  `references` longtext CHARACTER SET utf8,
  `correspondence_address` longtext CHARACTER SET utf8,
  `editors` longtext CHARACTER SET utf8,
  `sponsors` longtext CHARACTER SET utf8,
  `publisher` longtext CHARACTER SET utf8,
  `conference_name` longtext CHARACTER SET utf8,
  `conference_date` longtext CHARACTER SET utf8,
  `conference_location` longtext CHARACTER SET utf8,
  `conference_code` longtext CHARACTER SET utf8,
  `issn` longtext CHARACTER SET utf8,
  `isbn` longtext CHARACTER SET utf8,
  `coden` longtext CHARACTER SET utf8,
  `pubmed_id` longtext CHARACTER SET utf8,
  `language_of_original_document` longtext CHARACTER SET utf8,
  `abbreviated_source_title` longtext CHARACTER SET utf8,
  `document_type` longtext CHARACTER SET utf8,
  `source` longtext CHARACTER SET utf8,
  `eid` longtext CHARACTER SET utf8,
  `authors_json` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6003 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for scopus_subjects
-- ----------------------------
DROP TABLE IF EXISTS `scopus_subjects`;
CREATE TABLE `scopus_subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `selector` varchar(255) DEFAULT NULL,
  `doc_count` int(11) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `export_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=297 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for scopus_years
-- ----------------------------
DROP TABLE IF EXISTS `scopus_years`;
CREATE TABLE `scopus_years` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) DEFAULT NULL,
  `doc_count` int(11) DEFAULT NULL,
  `selector` varchar(255) DEFAULT NULL,
  `filename` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=latin1;
