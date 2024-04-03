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
SELECT 
  strftime(
    "%d",date(dateNaissance)
  ) as jour,
  strftime(
    "%m",date(dateNaissance)
  ) as mois,
  titre
FROM auteurs
JOIN livres ON auteurs.idAuteur = livres.idAuteur
WHERE jour = mois
ORDER BY jour;

