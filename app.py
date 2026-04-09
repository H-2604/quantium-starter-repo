from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/output.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the line chart
fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time', labels={'date': 'Date', 'sales': 'Sales ($)'})

# Add a vertical line on Jan 15 2021 to show price increase
fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000, line_dash='dash', line_color='red', annotation_text='Price Increase')

app = Dash(__name__)

app.layout = html.Div([html.H1("Pink Morsel Sales Visualiser"), dcc.Graph(figure=fig)])

if __name__ == '__main__':
    app.run(debug=True)