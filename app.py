from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div([

    # Header
    html.Div([
        html.H1("🍬 Pink Morsel Sales Dashboard",
                style={
                    'color': 'white',
                    'margin': '0',
                    'fontSize': '2rem',
                    'fontWeight': '700',
                    'letterSpacing': '1px'
                }),
        html.P("Soul Foods Sales Visualiser",
            style={'color': '#f0a0c0', 'margin': '5px 0 0 0', 'fontSize': '1rem'})
    ], style={
        'background': 'linear-gradient(135deg, #6c3483, #e8567a)',
        'padding': '30px 40px',
        'marginBottom': '30px',
        'borderRadius': '0 0 20px 20px',
        'boxShadow': '0 4px 20px rgba(233,30,140,0.3)'
    }),

    # Radio buttons
    html.Div([
        html.Label("Filter by Region",
                style={
                    'fontWeight': '600',
                    'fontSize': '1rem',
                    'color': '#333',
                    'marginBottom': '12px',
                    'display': 'block'
                }),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' All', 'value': 'all'},
                {'label': ' North', 'value': 'north'},
                {'label': ' South', 'value': 'south'},
                {'label': ' East', 'value': 'east'},
                {'label': ' West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            inputStyle={'marginRight': '6px', 'accentColor': '#e91e8c'},
            labelStyle={
                'marginRight': '20px',
                'fontSize': '0.95rem',
                'color': '#444',
                'cursor': 'pointer'
            }
        )
    ], style={
        'background': 'white',
        'padding': '20px 30px',
        'borderRadius': '12px',
        'boxShadow': '0 2px 12px rgba(0,0,0,0.08)',
        'margin': '0 30px 25px 30px'
    }),

    # Chart
    html.Div([
        dcc.Graph(id='sales-chart')
    ], style={
        'background': 'white',
        'borderRadius': '12px',
        'boxShadow': '0 2px 12px rgba(0,0,0,0.08)',
        'margin': '0 30px 30px 30px',
        'padding': '10px'
    })

], style={
    'fontFamily': 'Segoe UI, sans-serif',
    'background': '#f5f5f5',
    'minHeight': '100vh',
    'margin': '0',
    'padding': '0'
})

REGION_COLORS = {
    'north': '#3498db',
    'south': "#5abd83",
    'east': "#F3CD34",
    'west': '#9b59b6',
    'all': '#e8567a'
}

@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    color = REGION_COLORS[selected_region]

    fig = px.line(filtered_df, x='date', y='sales',
                title=f'Pink Morsel Sales Over Time — {selected_region.title()}',
                labels={'date': 'Date', 'sales': 'Sales ($)'})

    fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
                line_dash='dash', line_color='#000000',
                annotation_text='Price Increase on 15 January 2021')

    fig.update_traces(line_color=color, line_width=1.5)
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family='Segoe UI, sans-serif',
        title_font_size=16,
        title_font_color='#333',
        hovermode='x unified'
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)