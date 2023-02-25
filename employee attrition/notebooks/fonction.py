# Importer les librairies nécessaires au travail

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Définir la fonction pour visualiser les boxplots


def box_plot(data, x_column, y_column, color,
             cmap={"Yes": "red", "No": "green"}, **kwargs):

    # Visualisation
    fig = px.box(data, 
                 x=x_column, 
                 y=y_column,
                 color=color,
                 title="Attrition basée sur {}".format(y_column),
                 color_discrete_map=cmap,
                 width=700, height=600)

    # Mettre à jour le graphique
    fig.update_traces(quartilemethod="exclusive")
    # Afficher le graphique
    fig.show()


# Créer une fonction de traçage des histogrammes

def bar_plot(dataframe, column, **kwargs):
    """_summary_

    Args:
        dataframe (_type_): _description_
        column (_type_): _description_
    """
    # Tracer le graphique barres
    sns.countplot(x=column, data=dataframe, **kwargs)

# Définir la fonction


def distribution_plot(dataframe, column_name):
    """Cette fonction permet de tracer les distribution sans KDE

    Args:
        dataframe (DatFrame): L'ensemble de données à fournir dans lequel
                       se trouve les colonnes nécessaires
        column_name (string): La colonne sur laquelle on trace la distribution
    """
    # Tracer la distribution displot
    sns.histplot(dataframe[column_name], kde=True)


# Définir la fonction pour visualiser les hisgogrammes

def hist_plot(dataframe, column_name, **kwargs):
    """Cette fonction permet de tracer les histogrammes en fournissant
       le DataFrame, la colonne sur laquelle on trace cette histogramme 
       et nombre de cases qu'il faut prendre en compte

    Args:
        dataframe (Pandaas DataFrame): C'est le DataFrame qu'il faut donner en entrée
        column_name (string): La colonne sur laquelle on trace l'histogramme
        bins_edge (int): La taille de case de l'histogramme
    """

    # Tracer le graphique histogramme
    plt.hist(x=column_name, data=dataframe, **kwargs)


# Définir une fonction pour décrire les visuels

def describe_graph(title="", x_label="", y_label=""):

    # Déscripion du graphique
    plt.title(title, fontsize=20)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
