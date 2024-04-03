/* La ligne suivante sert uniquement à améliorer l'affichage à droite */
.mode column

/*Création des trois relations*/
CREATE TABLE livres (
  titre TEXT,
  idAuteur INT,
  annee INT
);

CREATE TABLE auteurs (
  nom TEXT,
  prenom TEXT,
  dateNaissance DATE,
  idAuteur INT,
  idPays INT
);

CREATE TABLE pays (
  idPays INT,
  nomPays TEXT,
  langue TEXT
);

/* Population des trois relations */
.separator ';'
.import books.csv livres
.import authors.csv auteurs
.import pays.csv pays

/*Requête de la liste des titres des livres, dans l'ordre alphabétique.*/
SELECT titre
FROM livres
ORDER BY titre;


/* Requête du nom et de la date de naissance des auteurs dans l'ordre chronologique.*/
SELECT nom,dateNaissance
FROM auteurs
ORDER BY dateNaissance;

