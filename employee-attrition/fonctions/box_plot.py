# Importer les librairies nécessaires au travail

import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Définir la fonction pour visualiser les boxplots

def box_plot(data, x_column, y_column, color, 
             cmap={"Yes":"red", "No":"green"}, **kwargs):

    # Visualisation
    fig = px.box(data, x=x_column, y=y_column,
                 color=color,
                 title="Attrition basée sur {}".format(y_column),
                 color_discrete_map=cmap,
                 width=700, height=600)
    
    # Mettre à jour le graphique
    fig.update_traces(quartilemethod="exclusive")
    # Afficher le graphique
    fig.show()