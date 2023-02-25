# Importer les librairies nécessaires
import seaborn as sns

# Créer une fonction de traçage des histogrammes

def bar_plot(dataframe, column, **kwargs):
    """_summary_

    Args:
        dataframe (_type_): _description_
        column (_type_): _description_
    """
    # Tracer le graphique barres
    sns.countplot(x=column, data=dataframe, **kwargs)