import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv("cleaned_googleplaystore.csv")

fig1 = px.histogram(df, x='Rating', nbins=30, marginal='rug', title='Distribution of Ratings')

category_counts = df['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'count']
fig2 = px.bar(category_counts, x='Category', y='count', title='Number of Apps in Each Category')

fig3 = px.histogram(df, x='Price', nbins=50, marginal='rug', title='Distribution of App Prices')
fig4 = px.histogram(df, x='Size', nbins=50, marginal='rug', title='Distribution of App Sizes')
fig5 = px.scatter(df, x='Size', y='Rating', title='Ratings vs. Size of Apps', opacity=0.5)
fig6 = px.scatter_matrix(df, dimensions=['Rating', 'Price', 'Size'], title='Pairplot of Rating, Price, and Size')
fig7 = px.histogram(df, x='Year', title='Number of Apps Released per Year', nbins=len(df['Year'].unique()))
fig8 = px.box(df, x='Category', y='Rating', title='Boxplot of Ratings by Category')

# Store the figures in a dictionary
fig_dict = {
    'Distribution of Ratings': fig1,
    'Number of Apps in Each Category': fig2,
    'Distribution of App Prices': fig3,
    'Distribution of App Sizes': fig4,
    'Ratings vs. Size of Apps': fig5,
    'Pairplot of Rating, Price, and Size': fig6,
    'Number of Apps Released per Year': fig7,
    'Boxplot of Ratings by Category': fig8
}

app = Dash(__name__)

app.layout = html.Div([
    html.H1("App Data Visualizations"),
    dcc.Dropdown(
        id='graph-dropdown',
        options=[{'label': key, 'value': key} for key in fig_dict.keys()],
        value='Distribution of Ratings'
    ),
    dcc.Graph(id='graph-display')
])

@app.callback(
    Output('graph-display', 'figure'),
    [Input('graph-dropdown', 'value')]
)
def update_graph(selected_graph):
    return fig_dict[selected_graph]

if __name__ == '__main__':
    app.run(debug=True, port=8050)
