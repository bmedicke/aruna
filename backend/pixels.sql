/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : PostgreSQL
 Source Server Version : 120003
 Source Host           : localhost:5432
 Source Catalog        : postgres
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120003
 File Encoding         : 65001

 Date: 06/07/2021 14:09:56
*/


-- ----------------------------
-- Table structure for pixels
-- ----------------------------
DROP TABLE IF EXISTS "public"."pixels";
CREATE TABLE "public"."pixels" (
  "id" int2 NOT NULL,
  "red" int2 NOT NULL DEFAULT 0,
  "green" int2 NOT NULL DEFAULT 0,
  "blue" int2 NOT NULL DEFAULT 0
)
;
ALTER TABLE "public"."pixels" OWNER TO "postgres";

-- ----------------------------
-- Primary Key structure for table pixels
-- ----------------------------
ALTER TABLE "public"."pixels" ADD CONSTRAINT "pixels_pkey" PRIMARY KEY ("id");
