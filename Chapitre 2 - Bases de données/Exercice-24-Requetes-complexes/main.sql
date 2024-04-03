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

/*Requête des années de publication sans doublon.*/


/* Requête des décades (20s, 30s, 90s...) où ont été publiées les livres, ainsi que le total de chaque décade.*/

