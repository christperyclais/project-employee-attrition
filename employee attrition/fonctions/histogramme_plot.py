# Importer la librairie nécessaire au travail
import matplotlib.pyplot as plt

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
