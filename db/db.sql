create schema rs_examen;

create table gebruikers(
geb_id int primary key auto_increment,
geb_naam varchar(100),
geb_voornaam varchar(100),
geb_email varchar(100), 
geb_password varchar(100),
geb_rol varchar(20),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table klas(
klas_id int auto_increment primary key, 
klas varchar(50),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


create table klas_formatie(
klf_id int auto_increment primary key, 
klas int, 
student int, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

constraint FK_klas_formatie foreign key (klas) references klas(klas_id)on delete cascade,
constraint FK_klas_student foreign key  (student) references gebruikers(geb_id) on delete cascade
);

create table vak(
vak_id int auto_increment primary key,
vak_naam varchar(100),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

create table examen(
examen_id int auto_increment primary key,
examen_titel varchar(100),
vak int, 
klas int, 
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);