# Importer la librairie nécessaire
import matplotlib.pyplot as plt

# Définir une fonction pour décrire les visuels
def describe_graph(title="", x_label="", y_label=""):

    # Déscripion du graphique
    plt.title(title, fontsize=20)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
