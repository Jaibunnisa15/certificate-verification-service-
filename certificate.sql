CREATE DATABASE certificates_db;

USE certificates_db;

CREATE TABLE certificates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    certificate_id VARCHAR(100) UNIQUE,
    name VARCHAR(100),
    college VARCHAR(150),
    domain VARCHAR(100),
    duration VARCHAR(50),
    issue_date DATE
);

INSERT INTO certificates (certificate_id, name, college, domain, duration, issue_date)
VALUES ('CERT123', 'Alice Johnson', 'XYZ College', 'Python', '3 months', '2024-10-01');

insert into certificates (certificate_id, name, college, domain, duration, issue_date)
values('CERT124','Bob','ABC college', 'java' ,'2 months','2024-11-01');

insert into certificates (certificate_id, name, college, domain, duration, issue_date)
values('CERT111','Jhon','xxy college', 'web development' ,'6 months','2024-01-01');

select * from certificates;
