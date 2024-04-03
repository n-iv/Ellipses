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

/*Modifier la requête pour obtenir la sortie demandée.*/
SELECT titre as Titre, prenom as Prénom, nom as Nom, annee as Année, nomPays as Pays, langue as Langue
FROM livres
JOIN auteurs on livres.idAuteur = auteurs.idAuteur
JOIN pays on auteurs.idPays = pays.idPays
ORDER BY titre;


