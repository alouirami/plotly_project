import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

# Leer y procesar los datos
data_file = 'Lectura OCR ALSA.csv'
df = pd.read_csv(data_file)





bar_chart = px.bar(df, x='Cantidad facturas', y='Proveedor', orientation='h', title='Distribución de facturas por proveedor')





# Crear la aplicación Dash
app = dash.Dash(__name__)


# Diseño de la aplicación
app.layout = html.Div([
    html.A(html.Button("informe facturas"), href="https://itbid-facturas-informe.onrender.com/"),
    html.A(html.Button("ranking proveedores"), href="https://itbid-ranking-proveedores.onrender.com/"),
    html.A(html.Button("lectura correcta"), href="https://itbid-lectura-correcta.onrender.com/"),
    html.A(html.Button("lectura incorrecta"), href="https://itbid-lectura-incorrecta.onrender.com/"),
    html.H1('Distribución de facturas por proveedor', style={'textAlign': 'center'}),
    dcc.Graph(figure=bar_chart, id='bar-chart')
    
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
