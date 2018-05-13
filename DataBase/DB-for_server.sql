
CREATE TABLE IF NOT EXISTS `typeofusers` (
  `idTypeOfUsers` INT(11) NOT NULL AUTO_INCREMENT,
  `UserName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTypeOfUsers`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;



CREATE TABLE IF NOT EXISTS `company` (
  `idCompany` INT(11) NOT NULL AUTO_INCREMENT,
  `CompanyName` VARCHAR(45) NOT NULL,
  `CompanyEmail` VARCHAR(45) NOT NULL,
  `CompanyPassword` VARCHAR(200) NOT NULL,
  `CompanyLogin` VARCHAR(45) NOT NULL,
  `idTypeOfUsers` INT(11) NOT NULL,
  `Company_Check` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idCompany`),
  UNIQUE INDEX `CompanyLogin_UNIQUE` (`CompanyLogin` ASC),
  UNIQUE INDEX `CompanyEmail_UNIQUE` (`CompanyEmail` ASC),
  INDEX `FK_2` (`idTypeOfUsers` ASC),
  CONSTRAINT `FK_2`
    FOREIGN KEY (`idTypeOfUsers`)
    REFERENCES `typeofusers` (`idTypeOfUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`students`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `students` (
  `idStudents` INT(11) NOT NULL AUTO_INCREMENT,
  `StudentsName` VARCHAR(45) NOT NULL,
  `StudentsLastName` VARCHAR(45) NOT NULL,
  `StudentsEmail` VARCHAR(45) NOT NULL,
  `StudentsPassword` VARCHAR(200) NOT NULL,
  `StudentsLogin` VARCHAR(45) NOT NULL,
  `idTypeOfUsers` INT(11) NOT NULL,
  PRIMARY KEY (`idStudents`),
  UNIQUE INDEX `StudentsLogin_UNIQUE` (`StudentsLogin` ASC),
  UNIQUE INDEX `StudentsEmail_UNIQUE` (`StudentsEmail` ASC),
  INDEX `Index` (`idTypeOfUsers` ASC),
  CONSTRAINT `FK_1`
    FOREIGN KEY (`idTypeOfUsers`)
    REFERENCES `typeofusers` (`idTypeOfUsers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses` (
  `idCourse` INT(11) NOT NULL AUTO_INCREMENT,
  `idCompany` INT(11) NOT NULL,
  `CoursesName` VARCHAR(45) NOT NULL,
  `CoursesAmount` INT(11) NOT NULL,
  `CoursesCity` VARCHAR(45) NOT NULL,
  `CoursesCountry` VARCHAR(45) NOT NULL,
  `CoursesStart` DATE NOT NULL,
  `CoursesEnd` DATE NOT NULL,
  `CoursesInfo` VARCHAR(1000) NOT NULL,
  `CoursesStatus` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idCourse`),
  UNIQUE INDEX `idCourse_UNIQUE` (`idCourse` ASC),
  INDEX `FK_Courses_Company_idx` (`idCompany` ASC),
  CONSTRAINT `FK_Courses_Company`
    FOREIGN KEY (`idCompany`)
    REFERENCES `company` (`idCompany`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`coursereviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `coursereviews` (
  `id_course_reviews` INT(11) NOT NULL AUTO_INCREMENT,
  `idStudents` INT(11) NOT NULL,
  `idCourse` INT(11) NOT NULL,
  `review` VARCHAR(2000) NOT NULL,
  `time` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_course_reviews`),
  INDEX `FK_Student` (`idStudents` ASC),
  INDEX `FK_Course` (`idCourse` ASC),
  CONSTRAINT `Fk_sdasd`
    FOREIGN KEY (`idStudents`)
    REFERENCES `students` (`idStudents`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_sdasdkasd`
    FOREIGN KEY (`idCourse`)
    REFERENCES `courses` (`idCourse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`infoaboutcompany`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `infoaboutcompany` (
  `idInfoAboutCompany` INT(11) NOT NULL AUTO_INCREMENT,
  `idCompany` INT(11) NOT NULL,
  `WebSite` VARCHAR(45) NULL DEFAULT NULL,
  `AboutCompany` VARCHAR(1000) NULL DEFAULT NULL,
  `Photo` LONGBLOB NULL DEFAULT NULL,
  `City` VARCHAR(50) NULL DEFAULT NULL,
  `Country` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`idInfoAboutCompany`),
  UNIQUE INDEX `idCompany_UNIQUE` (`idCompany` ASC),
  INDEX `fk_About_Company_idx` (`idCompany` ASC),
  INDEX `idCompany_INDEX` (`idCompany` ASC),
  CONSTRAINT `fk_About_Company`
    FOREIGN KEY (`idCompany`)
    REFERENCES `company` (`idCompany`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`infoaboutstudent`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `infoaboutstudent` (
  `idInfoAboutStudent` INT(11) NOT NULL AUTO_INCREMENT,
  `Photo` LONGBLOB NULL DEFAULT NULL,
  `City` VARCHAR(100) NULL DEFAULT NULL,
  `Country` VARCHAR(100) NULL DEFAULT NULL,
  `DateOfBirth` DATE NULL DEFAULT NULL,
  `University` VARCHAR(100) NULL DEFAULT NULL,
  `TimeOfStyding` VARCHAR(100) NULL DEFAULT NULL,
  `LinktoLinkedIN` VARCHAR(100) NULL DEFAULT NULL,
  `AboutStudent` TEXT NULL DEFAULT NULL,
  `CV` LONGBLOB NULL DEFAULT NULL,
  `idStudents` INT(11) NOT NULL,
  PRIMARY KEY (`idInfoAboutStudent`),
  UNIQUE INDEX `idStudents_UNIQUE` (`idStudents` ASC),
  CONSTRAINT `fk_students`
    FOREIGN KEY (`idStudents`)
    REFERENCES `students` (`idStudents`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`student_apply`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `student_apply` (
  `idStudent_Apply` INT(11) NOT NULL AUTO_INCREMENT,
  `idStudents` INT(11) NOT NULL,
  `idCourse` INT(11) NOT NULL,
  `status` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idStudent_Apply`),
  INDEX `fk_students_21231_idx` (`idStudents` ASC),
  INDEX `fk_courses_12312_idx` (`idCourse` ASC),
  CONSTRAINT `fk_courses_12312`
    FOREIGN KEY (`idCourse`)
    REFERENCES `courses` (`idCourse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_students_21231`
    FOREIGN KEY (`idStudents`)
    REFERENCES `students` (`idStudents`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `webproject`.`studentsreviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `studentsreviews` (
  `idStudentsCompanyReviews` INT(11) NOT NULL AUTO_INCREMENT,
  `idCompany` INT(11) NOT NULL,
  `idStudents` INT(11) NOT NULL,
  `review` VARCHAR(2000) NOT NULL,
  `time` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idStudentsCompanyReviews`),
  INDEX `fk_fddsfd_idx` (`idCompany` ASC),
  INDEX `fk_erds_idx` (`idStudents` ASC),
  CONSTRAINT `fk_erds`
    FOREIGN KEY (`idStudents`)
    REFERENCES `students` (`idStudents`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fddsfd`
    FOREIGN KEY (`idCompany`)
    REFERENCES `company` (`idCompany`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;



