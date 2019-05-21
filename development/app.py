# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# ticker = 'AAPL'


app.layout = html.Div(children=[
    dcc.Dropdown(
        id='input',
        options=[{'label': i.title(), 'value': i} for i in df.columns.values[2:]],
        placeholder='Enter ticker...',
        value='',
        class
    ),
    html.Div(
        id='output'
    ),

])


@app.callback(
    Output('output', 'children'),
    [Input('input', 'value')])
def update_graph(input_data):
    input_data = input_data.upper()
    df = pd.read_csv('~/Projects/Finance/development/stock_dfs/{}.csv'.format(input_data),
                     parse_dates=True, index_col=0, header=0)

    return dcc.Graph(
        id='stock-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.adjusted_close, 'type': 'line', 'name': input_data},
                {'x': df.index, 'y': df.volume, 'type': 'bar', 'name': 'Volume'},
            ],
            'layout': go.Layout(
                title=input_data
            )
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
