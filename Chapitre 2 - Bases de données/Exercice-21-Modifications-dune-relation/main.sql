/* La ligne suivante sert uniquement à améliorer l'affichage à droite */
.mode column

/*Création des deux relations*/
CREATE TABLE livres (
  titre TEXT,
  idAuteur INT,
  annee INT
);

CREATE TABLE auteurs (
  nom TEXT,
  prenom TEXT,
  dateNaissance DATE,
  idAuteur INT
);

/* Population des deux relations */
.separator ';'
.import books.csv livres
.import authors.csv auteurs


/*Requêtes basiques pour afficher le contenu des relations*/
SELECT *
FROM livres;

SELECT *
FROM auteurs;

/*À décommenter une fois la table pays créée.*/
/*
SELECT *
FROM pays;
*/