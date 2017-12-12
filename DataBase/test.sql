use Webproject;

insert into TypeOfUser(UserName)
values('Student'),('Company');

insert into students(StudentLogin,StudentsName,StudentsLastName,StudentsEmail,StudentsPassword,idTypeOfUser)
values('nazar12312','Nazar','Kulik','nazar.kulik1213@gmail.com','123213121',1);

insert into company(CompanyLogin,CompanyName,CompanyEmail,CompanyPassword,idTypeOfUser)
values('soft123123','SoftServe','softserve@gmail.com','123123',2);