import dash
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

# Data Exploration with Pandas (python)
# -----------------------------------------------------------------

df = pd.read_excel("C:\\Users\\erbil\\Desktop\\DATAEWARNDaily work\\ewarn2021.xlsx") # data by GregorySmith from kaggle
df['Site_Name'] = df['Site Name']
#print(df.Genre.nunique())
#print(df.Genre.unique())
#print(sorted(df.Year.unique()))

# Data Visualization with Plotly (Python)
# -----------------------------------------------------------------

#fig_pie = px.pie(data_frame=df, names='governorate', values='total_consultations')
#fig_pie.show()

#fig_bar = px.bar(data_frame=df, x='governorate', y='total_consultations')
#fig_bar.show()

#fig_hist = px.histogram(data_frame=df, x='governorate', y='total_consultations')
#fig_hist.show()

# Interactive Graphs with Dash (Python, R, Julia)
# -----------------------------------------------------------------

app = dash.Dash(__name__)

app.layout=html.Div([
    html.H1("Graph Analysis with AURI of EWARN 2021"),
    dcc.Dropdown(id='Site_Name-choice',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.Site_Name.unique())],
                 value=''
                 ),
    dcc.Graph(id='my-graph',
              figure={}),
])
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='Site_Name-choice', component_property='value')
)
def interactive_graphs(value_week):
    #print(value_week)
    dff = df[df.Site_Name==value_week]
    fig = px.bar(data_frame=dff, x='week', y='Acute Upper Respiratory Tract Infections')
    return fig


if __name__=='__main__':
    app.run_server()