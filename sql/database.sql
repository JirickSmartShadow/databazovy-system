
-- autor: Ji�� La�tovka
-- vytvo�en� datab�ze
create database kino;

--vstup do datab�ze
use kino;

-- vytv��en� struktury datab�ze
begin transaction;

create table reziser(
id int identity(1, 1),
jmeno varchar(50) not null,
prijmeni varchar(50) not null,
constraint PK_reziser primary key (id)
);

create table kategorie(
id int identity(1, 1),
-- check(in()) - alternativa misto enumu (mssql nema enum)
nazev varchar(50) not null check(nazev in('poh�dka', 'horor', 'thriler', 'romantika', 'sci-fi', 'fantasy', 'dokument', 'komedie')),
constraint PK_kategorie primary key (id)
);

create table kinosal(
id int identity(1, 1),
oznaceni varchar(50) not null,
kapacita int not null,
constraint PK_kinosal primary key (id)
);

create table film(
id int identity(1, 1),
kategorie_id int,
reziser_id int,
nazev varchar(50) not null,
delka_min int not null,
cena decimal(8, 2) not null,
tri_d bit not null,
constraint PK_film primary key (id),
constraint FK_film_kategorie foreign key (kategorie_id) references kategorie (id),
constraint FK_film_reziser foreign key (reziser_id) references reziser (id) on delete set null on update set null
);

create table promitani(
id int identity(1, 1),
film_id int,
kinosal_id int,
datum_cas datetime not null,
constraint PK_promitani primary key (id),
constraint FK_promitani_film foreign key (film_id) references film (id),
constraint FK_promitani_kinosal foreign key (kinosal_id) references kinosal (id)
);

go
create view prehled_filmu
as
select f.nazev 'n�zev', concat(f.delka_min, ' min') 'd�lka', case when f.tri_d = 1 then 'ano' else 'ne' end '3D', concat(f.cena, ' K�') 'cena', r.jmeno + ' ' + r.prijmeni 're�is�r'
from film f join reziser r on f.reziser_id = r.id;
go

go
create view prehled_promitani
as
select f.nazev 'n�zev', p.datum_cas 'datum a �as', k.oznaceni 's�l ��slo', concat(f.delka_min, ' min') 'd�lka', concat(f.cena, ' K�') 'cena', r.jmeno + ' ' + r.prijmeni 're�is�r'
from promitani p join kinosal k on p.kinosal_id = k.id 
join film f on f.id = p.film_id join reziser r on f.reziser_id = r.id;
go

go
create view celkovy_promitaci_cas
as
select sum(f.delka_min) / 60 'celkem odprom�t�no hodin'
from film f join promitani p on f.id = p.film_id;
go

commit;

-- vkl�d�n� dat do datab�ze

begin transaction;

insert into reziser(jmeno, prijmeni) values ('Jan', 'Zelen�');
insert into reziser(jmeno, prijmeni) values ('Jakub', 'Modr�');
insert into reziser(jmeno, prijmeni) values ('Petr', '�ern�');
insert into reziser(jmeno, prijmeni) values ('Luk�', '�lut�');
insert into reziser(jmeno, prijmeni) values ('Kate�ina', 'B�l�');

insert into kategorie(nazev) values ('poh�dka');
insert into kategorie(nazev) values ('horor');
insert into kategorie(nazev) values ('romantika');
insert into kategorie(nazev) values ('sci-fi');
insert into kategorie(nazev) values ('fantasy');

insert into kinosal(oznaceni, kapacita) values ('01', 150);
insert into kinosal(oznaceni, kapacita) values ('02', 130);
insert into kinosal(oznaceni, kapacita) values ('03', 120);
insert into kinosal(oznaceni, kapacita) values ('04', 200);
insert into kinosal(oznaceni, kapacita) values ('05', 150);

insert into film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) values (1, 1, 'T�i p��n�', 90, 220, 0);
insert into film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) values (2, 2, 'Temnota', 120, 250, 1);
insert into film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) values (3, 3, 'R��e', 115, 230, 0);
insert into film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) values (4, 4, 'Astronaut', 110, 280, 0);
insert into film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) values (5, 5, 'Drak', 100, 260, 1);

insert into promitani(film_id, kinosal_id, datum_cas) values (1, 1, '2023-01-10 16:20:00');
insert into promitani(film_id, kinosal_id, datum_cas) values (2, 2, '2022-09-06 17:00:00');
insert into promitani(film_id, kinosal_id, datum_cas) values (3, 3, '2022-11-15 18:40:00');
insert into promitani(film_id, kinosal_id, datum_cas) values (4, 4, '2022-04-30 20:20:00');
insert into promitani(film_id, kinosal_id, datum_cas) values (5, 5, '2022-07-25 12:30:00');

commit;
