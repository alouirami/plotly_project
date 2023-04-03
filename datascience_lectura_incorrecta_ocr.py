import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

# Leer y procesar los datos
data_file = 'Lectura OCR ALSA.csv'
df = pd.read_csv(data_file)
# Eliminar espacios adicionales en los nombres de las columnas
df.columns = df.columns.str.strip()
# Filtrar los datos que tienen "Leer bien" en la columna 'Estado lectura'
data_filtrada_mal = df[df['Estado lectura'] != 'Leer bien']

lectura_incorrecta_chart = px.bar(data_filtrada_mal, y='Cantidad facturas', x='Proveedor', orientation='v', title='Cantidad de facturas por proveedor con lectura incorrecta',width=600, height=700)
lectura_incorrecta_chart.update_traces(marker_color='rgb(199, 0, 57)')
# Crear la aplicación Dash
app = dash.Dash(__name__)
server = app.server
# Diseño de la aplicación
app.layout = html.Div([
    html.A(html.Button("informe facturas"), href="https://itbid-facturas-informe.onrender.com/"),
    html.A(html.Button("distribución facturas"), href="https://itbid-distribucion-facturas.onrender.com/"),
    html.A(html.Button("ranking proveedores"), href="https://itbid-ranking-proveedores.onrender.com/"),
    html.A(html.Button("lectura correcta"), href="https://itbid-lectura-correcta.onrender.com/"),
    html.H1('Cantidad de facturas por proveedor con lectura incorrecta', style={'textAlign': 'center'}),
    dcc.Graph(figure=lectura_incorrecta_chart, id= 'lectura_incorrecta_chart')

])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
