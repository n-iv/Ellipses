/* La ligne suivante sert uniquement à améliorer l'affichage à droite */
.mode column


/*Création des deux relations*/
CREATE TABLE livres (
  titre TEXT,
  auteur TEXT,
  annee INT
);

CREATE TABLE auteurs (
  nom TEXT,
  prenom TEXT,
  dateNaissance DATE
);

/* Population des deux relations */
.separator ';'
.import books.csv livres
.import authors.csv auteurs

/* Ajout de deux livres */
INSERT INTO livres VALUES
  ('La nuit des temps','René Barjavel',1968),
  ('Ravage','René Barjavel',1943);

/*Ajout, modification et suppression d'un livre*/
INSERT INTO livres(titre,annee) VALUES
  ('Le roman de Renart',1300);

SELECT *
FROM livres;

UPDATE livres 
SET annee='XIVème', auteur='Inconnu'
WHERE titre='Le roman de Renart';

SELECT *
FROM livres;

DELETE FROM livres 
WHERE titre='Le roman de Renart';

SELECT *
FROM livres;
