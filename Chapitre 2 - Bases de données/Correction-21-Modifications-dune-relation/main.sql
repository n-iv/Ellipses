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
  idAuteur INT
);

CREATE TABLE pays (
  idPays INTEGER PRIMARY KEY AUTOINCREMENT,
  nomPays TEXT,
  langue TEXT
);


/* Population des trois relations */
.separator ';'
.import books.csv livres
.import authors.csv auteurs
  
INSERT INTO pays(nomPays,langue) VALUES
  ('Russie','Russe'),
  ('Autriche','Allemand'),
  ('Colombie','Espagnol'),
  ('Royaume-Uni','Anglais'),
  ('France','Français'),
  ('Norvège','Norvégien'),
  ('Japon','Japonais'),
  ('Allemagne','Allemand'),
  ('Etats-Unis','Anglais');

ALTER TABLE auteurs
ADD idPays int;

UPDATE auteurs
SET idPays = 1
WHERE prenom = 'Fiodor' or prenom = 'Léon';

UPDATE auteurs
SET idPays = 2
WHERE nom = 'Kafka';

UPDATE auteurs
SET idPays = 3
WHERE prenom = 'Gabriel';

UPDATE auteurs
SET idPays = 4
WHERE nom = 'Orwell' or nom = 'Woolf' or nom = 'Shakespeare';

UPDATE auteurs
SET idPays = 5
WHERE nom = 'Flaubert';

UPDATE auteurs
SET idPays = 6
WHERE nom = 'Ibsen';

UPDATE auteurs
SET idPays = 7
WHERE nom = 'Shikibu' or nom = 'Kawabata';

UPDATE auteurs
SET idPays = 8
WHERE nom = 'Mann';

UPDATE auteurs
SET idPays = 9
WHERE nom = 'Faulkner';

  
/*Requêtes basiques pour afficher le contenu des relations*/
SELECT *
FROM livres;

SELECT *
FROM auteurs;

SELECT *
FROM pays;
