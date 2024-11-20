Analyse et Prédiction des Résultats des Matchs de Football
Ce projet analyse les résultats des matchs de football à l'aide d'un modèle d'arbre de décision. Il explore les facteurs influençant le résultat d'un match et fournit une visualisation interprétable sous forme d'arbre.

Objectif du Projet
Analyser les données : Comprendre les facteurs comme les buts marqués, le lieu du match, ou l'adversaire.
Construire un modèle prédictif : Prédire si une équipe va gagner, faire match nul, ou perdre.
Visualiser l'arbre de décision : Fournir une interprétation claire des décisions prises par le modèle.
Étapes du Projet
1. Chargement des données
Le dataset utilisé contient des informations détaillées sur les matchs de football, telles que :

Les buts marqués (gf) et encaissés (ga).
Le lieu du match (venue, domicile ou extérieur).
L'adversaire (opp_code).
Les statistiques avancées (xg, ppda, etc.).
Code :

python
Copier le code
data = pd.read_csv('Vainqueurs des matchs de football clean.csv')
print(data.head())
2. Nettoyage des données
Les doublons ont été identifiés et supprimés dans Excel avant d'importer le fichier dans ce projet. Aucune autre étape de nettoyage n'a été réalisée dans le code.

3. Préparation des données pour le modèle
Sélection des colonnes pertinentes pour le modèle : ['gf', 'ga', 'venue_code', 'opp_code', 'hour', 'day_code'].
Division des données en ensembles d'entraînement et de test.
X = data[['gf', 'ga', 'venue_code', 'opp_code', 'hour', 'day_code']]
y = data['target']
4. Création et entraînement de l'arbre de décision
Un modèle d'arbre de décision est créé avec une profondeur maximale de 5 pour limiter sa complexité. Le modèle est ensuite entraîné avec les données.

Code :

python
Copier le code
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

5. Visualisation de l'arbre de décision
L'arbre est visualisé pour interpréter les règles utilisées par le modèle :

Les nœuds montrent les seuils utilisés pour diviser les données.
Les feuilles indiquent la prédiction finale.
L'image est également sauvegardée dans un fichier football_decision_tree.png.

Code :

python
Copier le code
plt.figure(figsize=(36, 24))
plot_tree(
    clf,
    feature_names=['gf', 'ga', 'venue_code', 'opp_code', 'hour', 'day_code'],
    class_names=['Lose/Draw', 'Win'],
    filled=True
)
plt.savefig('football_decision_tree.png')
plt.show()

6 Importation sur GITHUB
