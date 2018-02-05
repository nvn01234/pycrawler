/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : pycrawler

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2018-02-06 01:21:07
*/

SET FOREIGN_KEY_CHECKS=0;

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
-- Records of isi_keys
-- ----------------------------
INSERT INTO `isi_keys` VALUES ('1', 'issn');
INSERT INTO `isi_keys` VALUES ('2', 'keywords_plus');
INSERT INTO `isi_keys` VALUES ('3', 'abstract');
INSERT INTO `isi_keys` VALUES ('4', 'usage_count_last_180_days');
INSERT INTO `isi_keys` VALUES ('5', 'number');
INSERT INTO `isi_keys` VALUES ('6', 'month');
INSERT INTO `isi_keys` VALUES ('7', 'affiliation');
INSERT INTO `isi_keys` VALUES ('8', 'doc_delivery_number');
INSERT INTO `isi_keys` VALUES ('9', 'year');
INSERT INTO `isi_keys` VALUES ('10', 'journal_iso');
INSERT INTO `isi_keys` VALUES ('11', 'web_of_science_categories');
INSERT INTO `isi_keys` VALUES ('12', 'title');
INSERT INTO `isi_keys` VALUES ('13', 'unique_id');
INSERT INTO `isi_keys` VALUES ('14', 'type');
INSERT INTO `isi_keys` VALUES ('15', 'author_email');
INSERT INTO `isi_keys` VALUES ('16', 'journal');
INSERT INTO `isi_keys` VALUES ('17', 'cited_references');
INSERT INTO `isi_keys` VALUES ('18', 'da');
INSERT INTO `isi_keys` VALUES ('19', 'volume');
INSERT INTO `isi_keys` VALUES ('20', 'orcid_numbers');
INSERT INTO `isi_keys` VALUES ('21', 'address');
INSERT INTO `isi_keys` VALUES ('22', 'eissn');
INSERT INTO `isi_keys` VALUES ('23', 'times_cited');
INSERT INTO `isi_keys` VALUES ('24', 'usage_count_since_2013');
INSERT INTO `isi_keys` VALUES ('25', 'publisher');
INSERT INTO `isi_keys` VALUES ('26', 'doi');
INSERT INTO `isi_keys` VALUES ('27', 'language');
INSERT INTO `isi_keys` VALUES ('28', 'keyword');
INSERT INTO `isi_keys` VALUES ('29', 'number_of_cited_references');
INSERT INTO `isi_keys` VALUES ('30', 'author');
INSERT INTO `isi_keys` VALUES ('31', 'research_areas');
INSERT INTO `isi_keys` VALUES ('32', 'oa');
INSERT INTO `isi_keys` VALUES ('33', 'article_number');
INSERT INTO `isi_keys` VALUES ('34', 'pages');
INSERT INTO `isi_keys` VALUES ('35', 'funding_text');
INSERT INTO `isi_keys` VALUES ('36', 'funding_acknowledgement');
INSERT INTO `isi_keys` VALUES ('37', 'researcherid_numbers');
INSERT INTO `isi_keys` VALUES ('38', 'meeting');
INSERT INTO `isi_keys` VALUES ('39', 'note');
INSERT INTO `isi_keys` VALUES ('40', 'organization');
INSERT INTO `isi_keys` VALUES ('42', 'isbn');
INSERT INTO `isi_keys` VALUES ('43', 'series');
INSERT INTO `isi_keys` VALUES ('44', 'booktitle');
INSERT INTO `isi_keys` VALUES ('45', 'editor');
INSERT INTO `isi_keys` VALUES ('46', 'book_author');
