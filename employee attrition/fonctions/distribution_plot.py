# Importer le module nécessaire
import seaborn as sns

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