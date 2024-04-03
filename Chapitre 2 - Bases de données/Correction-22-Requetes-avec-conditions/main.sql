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

/*Requête des (quatre) livres écrits en 1925 ou en 1869.*/
SELECT *
FROM livres
WHERE annee = 1925 or annee = 1869;


/*Requête des (quatre) livres dont le titre commence par "Le "*/
SELECT titre,annee
FROM livres
WHERE titre > 'Le ' and titre < 'Le!' and annee <=2000 and annee > 1900;

