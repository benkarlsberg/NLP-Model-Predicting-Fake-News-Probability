import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
import pickle
from src.helpers import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# random forest classifier model
model = pickle.load(open('../rfc_model_final.pkl', 'rb'))
# tfidf for transforming article
tfidf = pickle.load(open('../tfidf_model_final.pkl', 'rb'))

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('Fake News Detector', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    dcc.Textarea(
        id='input-article',
        value='Enter Article Here',
        style={'width': '100%', 'height': 200, 'backgroundColor': colors['text']
        },
    ),
    html.Button('Submit', id='submit-article', n_clicks=0,
                style={'color': colors['text'],  'marginLeft':10}
            ),
    html.Div(id='output-article', style={'whiteSpace': 'pre-line'}),
    html.H2('Truth Meter', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    daq.Gauge(
        id='daq-gauge',
        label='P(True) %',
        size=400,
        units='P(True) %',
        min=0,
        max=100,
        showCurrentValue=True,
        value=50,
        color={"gradient":True, "ranges":{"red":[0,35],"purple":[35,65],"blue":[65,100]}},
        style={'color': colors['text']},
    ),
    # dcc.Graph(
    #     id='bar-chart',)
])
@app.callback(
    [
        Output('output-article', 'children'),
        Output('daq-gauge', 'value'),
        # Output('bar-chart', 'figure'),
    ],
    [Input('submit-article', 'n_clicks')],
    [State('input-article', 'value')]
)
def update_truth(n_clicks, article):
    vector = tfidf.transform([article])
    pred = model.predict_proba(vector)
    c0, c1 = pred[0]
    s1 = ""
    # # bar chart, add return d1 to last output
    # d1 = {
    #     'data': [{
    #         'x': ['P(Fake)', 'P(Real)'],
    #         'y': [c0, c1],
    #         'type': 'bar',
    #         'name': 'truth'
    #     }],
    #     'layout': {
    #         # 'title': 'Truth Analysis',
    #         'yaxis': {'range': [0, 1]},
    #         'plot_bgcolor': colors['background'],
    #         'paper_bgcolor': colors['background'],
    #         'font': {
    #                 'color': colors['text']
    #     }
    # }}
    return s1, c1.round(3)*100
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8898)