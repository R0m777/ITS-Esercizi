create table DOCENTE(
    mat integer not null,
    nome character varying (100) not null,
    cognome character varying (100) not null,
    email character varying (100) not null,
    primary key (mat)
);

create table CORSO(
    codice integer not null,
    nome character varying (100) not null,
    aula character varying (100) not null,
    primary key (codice)
);

create table INCARICO(
    docente integer not null,
    corso integer not null,
    primary key (docente,corso),
    foreign key (docente)
    references docente(mat),
    foreign key (corso)
    references corso(codice)

);