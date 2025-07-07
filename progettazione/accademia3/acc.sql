--Definizione dei domini

create type Strutturato as
enum ('Ricercatore','Professore Associato','Professore Ordinario');

create type LavoroProgetto as
enum ('Ricerca e Sviluppo','Dimostrazione','Management','Altro');

create type LavoroNonProgettuale as
enum ('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Academico','Altro');

create type CausaAssenza as
enum ('Chiusura Universitaria','Maternita','Malattia');

create domain Postinteger as integer
    default 0
check(value>=0);

create domain StringaM as varchar(100);

create domain NumeroOre as integer
    default 0
check(value>=0 and value<=8);

create domain Denaro as real
    default 0
check(value>=0);

--Schema relazionale con vincoli della base dati

create table Persona (
    id Postinteger not null,
    nome StringaM not null,
    cognome StringaM not null,
    posizione Strutturato not null,
    stipendio Denaro not null,
    primary key (id)
);

create table Progetto (
    id Postinteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    budget Denaro,
    primary key(id),
    unique(nome),
    check (inizio < fine)
);

create table WP(
    progetto Postinteger not null,
    id Postinteger not null,
    nome StringaM not null,
    inizio date not null,
    fine date not null,
    primary key(progetto,id),
    unique(progetto,nome),
    check (inizio < fine),
    foreign key (progetto) references Progetto(id)
);

create table AttivitaProgetto (
    id Postinteger not null,
    persona Postinteger not null,
    progetto Postinteger not null,
    wp Postinteger not null,
    giorno date not null,
    tipo LavoroProgetto not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona (id),
    foreign key (progetto,wp) references WP (progetto,id)
);

create table AttivitaNonProgettuale (
    id Postinteger not null,
    persona Postinteger not null,
    tipo LavoroNonProgettuale not null,
    giorno date not null,
    oreDurata NumeroOre not null,
    primary key (id),
    foreign key (persona) references Persona(id)
);

create table Assenza (
    id Postinteger not null,
    persona Postinteger not null,
    tipo CausaAssenza not null,
    giorno date not null,
    primary key (id),
    unique (persona,giorno),
    foreign key (persona) references Persona(id)
);
