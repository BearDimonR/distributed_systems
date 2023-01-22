CREATE DATABASE /*!32312 IF NOT EXISTS*/ `linkedin` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `linkedin`;

CREATE TABLE `user` (
	`id` int(11) PRIMARY KEY NOT NULL,
	login varchar(32) NOT NULL,
	password varchar(16) NOT NULL
);


CREATE TABLE `resume` (
	id int(11) PRIMARY KEY NOT NULL,
	summary text,
	userId int(11),
	CONSTRAINT `fk Resume.userId to User.id` FOREIGN KEY (userId) REFERENCES `user` (id)
) ;

CREATE TABLE hobbycategory (
	id int(11) PRIMARY KEY NOT NULL,
	name varchar(128)
) ;

CREATE TABLE city (
	id int(11) PRIMARY KEY NOT NULL,
	name varchar(128),
	code int
) ;

CREATE TABLE company (
	id int(11) PRIMARY KEY NOT NULL,
	name varchar(128)
) ;

CREATE TABLE hobby (
	hobbyId int(11) NOT NULL,
	resumeId int(11) NOT NULL,
	CONSTRAINT hobbies_key PRIMARY KEY (resumeId, hobbyId),
	CONSTRAINT `fk ResumeHobbies.hobbyId to Hobby.id` FOREIGN KEY (hobbyId) REFERENCES hobbycategory (id),
	CONSTRAINT `fk ResumeHobbies.resumeId to Resume.id` FOREIGN KEY (resumeId) REFERENCES `resume` (id)
) ;

CREATE TABLE position (
	id int(11) PRIMARY KEY NOT NULL,
	resumeId int(11),
	companyId int(11),
	name varchar(128),
	cityId int(11),
	CONSTRAINT `fk Positions.resumeId to Resume.id` FOREIGN KEY (resumeId) REFERENCES `resume` (id),
	CONSTRAINT `fk Positions.cityId to City.id` FOREIGN KEY (cityId) REFERENCES city (id),
	CONSTRAINT `fk Positions.companyId to Company.id` FOREIGN KEY (companyId) REFERENCES company (id)
) ;



-- user inserts

insert into `user` (id, login, password) values (1, "gnickols0@xinhuanet.com", "4zynnh");
insert into `user` (id, login, password) values (2, "imicklewright1@europa.eu", "abm7oIBb");

-- resume inserts

insert into `resume` (id, userId, summary) values (1, 1, "Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. Morbi porttitor lorem id ligula.");
insert into `resume` (id, userId, summary) values (2, 2, "Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit.");

-- hobbycategory

insert into hobbycategory (id, name) values (1, "Western Cordilleran Bunchberry");
insert into hobbycategory (id, name) values (2, "Alpine Sandmat");
insert into hobbycategory (id, name) values (3, "Biatora Lichen");
insert into hobbycategory (id, name) values (4, "Kauai Yellow Loosestrife");
insert into hobbycategory (id, name) values (5, "Aleutian Rim Lichen");

-- city inserts

insert into city (id, name, code) values (1, "Wilfrido Loor Moreira", 56);
insert into city (id, name, code) values (2, "Touho", 43);
insert into city (id, name, code) values (3, "Kuala Lumpur", 27);
insert into city (id, name, code) values (4, "Salinggara", 38);
insert into city (id, name, code) values (5, "Bukovany", 60);

-- company inserts

insert into company (id, name) values (1, "Vistra Energy Corp.");
insert into company (id, name) values (2, "Limelight Networks, Inc.");
insert into company (id, name) values (3, "Scorpio Bulkers Inc.");
insert into company (id, name) values (4, "Dreyfus High Yield Strategies Fund");
insert into company (id, name) values (5, "Fuel Tech, Inc.");

-- hobby inserts

insert into hobby (resumeId, hobbyId) values (1, 1);
insert into hobby (resumeId, hobbyId) values (1, 2);
insert into hobby (resumeId, hobbyId) values (1, 3);
insert into hobby (resumeId, hobbyId) values (1, 5);
insert into hobby (resumeId, hobbyId) values (2, 3);
insert into hobby (resumeId, hobbyId) values (2, 5);
insert into hobby (resumeId, hobbyId) values (2, 4);
insert into hobby (resumeId, hobbyId) values (2, 2);

-- position inserts

insert into position (id, resumeId, cityId, companyId, name) values (1, 1, 1, 1, "Upgradable executive attitude");
insert into position (id, resumeId, cityId, companyId, name) values (2, 1, 2, 2, "Visionary motivating access");
insert into position (id, resumeId, cityId, companyId, name) values (3, 1, 3, 3, "Organized exuding encryption");
insert into position (id, resumeId, cityId, companyId, name) values (4, 1, 4, 4, "Object-based multi-tasking initiative");
insert into position (id, resumeId, cityId, companyId, name) values (5, 2, 1, 5, "Profound object-oriented system engine");
insert into position (id, resumeId, cityId, companyId, name) values (6, 2, 3, 5, "Cross-platform zero defect utilisation");
insert into position (id, resumeId, cityId, companyId, name) values (7, 2, 3, 1, "Seamless zero administration core");
insert into position (id, resumeId, cityId, companyId, name) values (8, 2, 3, 1, "Inverse motivating budgetary management");