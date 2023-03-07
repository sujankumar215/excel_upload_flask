show databases;
create user 'schoolappuser'@'localhost' identified with mysql_native_password by 'harika123';

grant all on school_app.* to 'schoolappuser'@'localhost';

select * from school_app.admissions_student

CREATE TABLE flask_tutorial.user_details (
    ID int NOT NULL auto_increment,
    name varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    phone varchar(50) NOT NULL,
    role varchar(20) NOT NULL,
    password varchar(20) NOT NULL,
    PRIMARY KEY (ID)
);
select * from flask_tutorial.user_details

CREATE TABLE flask_tutorial.user_roles (
    ID int NOT NULL auto_increment,
    title varchar(50) NOT NULL,
	PRIMARY KEY (ID)
);

select * from flask_tutorial.user_roles

CREATE TABLE flask_tutorial.App_endpoint (
    ID int NOT NULL auto_increment,
    endpoint varchar(100) NOT NULL,
    method varchar(20) NOT NULL,
	PRIMARY KEY (ID)
);

select * from flask_tutorial.App_endpoint

CREATE TABLE flask_tutorial.app_Accesibility (
    ID int NOT NULL auto_increment,
    endpoint_id int(11) NOT NULL,
    roles LONGTEXT NOT NULL,
	PRIMARY KEY (ID)
);

select * from flask_tutorial.app_Accesibility;


select end_t.endpoint,acc.roles from flask_tutorial.App_endpoint as end_t
join flask_tutorial.app_Accesibility as  acc on
end_t.ID = acc.endpoint_id

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `flask_tutorial`.`accesibility_view` AS
    SELECT 
        `end_t`.`endpoint` AS `endpoint`, `acc`.`roles` AS `roles`
    FROM
        (`flask_tutorial`.`app_endpoint` `end_t`
        JOIN `flask_tutorial`.`app_accesibility` `acc` ON ((`end_t`.`ID` = `acc`.`endpoint_id`)))

select * from flask_tutorial.accesibility_view