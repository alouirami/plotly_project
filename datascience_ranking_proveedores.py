import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

# Leer y procesar los datos
data_file = 'Lectura OCR ALSA.csv'
df = pd.read_csv(data_file)





df_ranking = df.sort_values(by='Cantidad facturas', ascending=False)
df_ranking['Ranking'] = range(1, len(df_ranking) + 1)

ranking_chart = px.bar(df_ranking, x='Cantidad facturas', y='Proveedor', orientation='h', title='Ranking de proveedores por cantidad de facturas')
ranking_chart.update_yaxes(categoryorder='total ascending')




# Crear la aplicación Dash
app = dash.Dash(__name__)


# Diseño de la aplicación
app.layout = html.Div([
    html.A(html.Button("informe facturas"), href="https://itbid-facturas-informe.onrender.com/"),
    html.A(html.Button("distribución facturas"), href="https://itbid-distribucion-facturas.onrender.com/"),
    html.A(html.Button("lectura correcta"), href="https://itbid-lectura-correcta.onrender.com/"),
    html.A(html.Button("lectura incorrecta"), href="https://itbid-lectura-incorrecta.onrender.com/"),
    html.H1('Ranking de proveedores por cantidad de facturas', style={'textAlign': 'center'}),
    dcc.Graph(figure=ranking_chart, id='ranking_chart')
    
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
