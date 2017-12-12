-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema WebProject
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema WebProject
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `WebProject` DEFAULT CHARACTER SET utf8 ;
USE `WebProject` ;

-- -----------------------------------------------------
-- Table `WebProject`.`TypeOfUser`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `WebProject`.`TypeOfUser` (
  `idTypeOfUser` INT NOT NULL AUTO_INCREMENT,
  `UserName` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTypeOfUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `WebProject`.`Students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `WebProject`.`Students` (
  `idStudents` INT NOT NULL AUTO_INCREMENT,
  `StudentsName` NVARCHAR(45) NOT NULL,
  `StudentsLastName` NVARCHAR(45) NOT NULL,
  `StudentsEmail` NVARCHAR(45) NOT NULL,
  `StudentsPassword` NVARCHAR(45) NOT NULL,
  `idTypeOfUser` INT NOT NULL,
  `StudentLogin` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`idStudents`),
  INDEX `INDEX` (`idTypeOfUser` ASC),
  UNIQUE INDEX `StudentLogin_UNIQUE` (`StudentLogin` ASC),
  CONSTRAINT `fk_userType`
    FOREIGN KEY (`idTypeOfUser`)
    REFERENCES `WebProject`.`TypeOfUser` (`idTypeOfUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `WebProject`.`Company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `WebProject`.`Company` (
  `idCompany` INT NOT NULL AUTO_INCREMENT,
  `CompanyName` NVARCHAR(45) NOT NULL,
  `CompanyEmail` NVARCHAR(45) NOT NULL,
  `CompanyPassword` NVARCHAR(45) NOT NULL,
  `idTypeOfUser` INT NOT NULL,
  `CompanyLogin` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCompany`),
  INDEX `INDEX` (`idTypeOfUser` ASC),
  UNIQUE INDEX `CompanyLogin_UNIQUE` (`CompanyLogin` ASC),
  CONSTRAINT `fk_typeOfuser`
    FOREIGN KEY (`idTypeOfUser`)
    REFERENCES `WebProject`.`TypeOfUser` (`idTypeOfUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
