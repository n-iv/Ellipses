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

/* Ajouter l'auteur Barjavel à la relation auteurs. */


/* Corriger les fautes à Flaubert. */


/* Effacer les livres publiés avant 1800. */


/*Requêtes basiques pour afficher le contenu des relations*/
SELECT *
FROM livres;

SELECT *
FROM auteurs;