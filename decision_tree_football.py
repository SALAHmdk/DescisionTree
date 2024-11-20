import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Charger les données
data = pd.read_csv('Vainqueurs des matchs de football clean.csv')

# Sélection des colonnes pertinentes pour l'entraînement
X = data[['gf', 'ga', 'venue_code', 'opp_code', 'hour', 'day_code']]
y = data['target']  # Variable cible

# Préparation des données : transformation des variables catégoriques si nécessaire
# (Dans ce cas, les colonnes sont déjà numériques)

# Création et entraînement de l'arbre de décision
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X, y)

# Visualisation de l'arbre de décision
plt.figure(figsize=(36, 24))
plot_tree(
    clf,
    feature_names=['gf', 'ga', 'venue_code', 'opp_code', 'hour', 'day_code'],
    class_names=['Lose/Draw', 'Win'],
    filled=True
)
plt.title("Arbre de Décision - Résultats des Matchs de Football", fontsize=16)
plt.savefig('football_decision_tree.png')  # Sauvegarde de l'image
plt.show()  # Affichage de l'arbre
