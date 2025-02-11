import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output

# Load the data from the CSV file
file_path = 'data/most_popular_1000_youtube_videos.csv'
data = pd.read_csv(file_path)

# Data Cleaning
data['Video views'] = data['Video views'].str.replace(',', '').astype(int)
data['Likes'] = data['Likes'].str.replace(',', '').astype(int)
data['Dislikes'] = data['Dislikes'].fillna('0').str.replace(',', '').astype(int)
data.dropna(inplace=True)

# Descriptive Statistics by Category
category_stats = data.groupby('Category').agg({
    'Video views': ['mean', 'sum', 'count'],
    'Likes': ['mean', 'sum'],
    'Dislikes': ['mean', 'sum']
}).reset_index()

# Rename columns for better readability
category_stats.columns = ['Category', 'Avg Views', 'Total Views', 'Total Videos', 'Avg Likes', 'Total Likes', 'Avg Dislikes', 'Total Dislikes']

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("YouTube Video Data Dashboard"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': category, 'value': category} for category in category_stats['Category']],
        value=['Education', 'Howto & Style', 'Film & Animation', 'Gaming', 'Automotive'],  # Default value
        multi=True
    ),
    dcc.Tabs([
        dcc.Tab(label='Video Statistics', children=[
            dash_table.DataTable(
                id='video-table',
                columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in data.columns],
                data=data.to_dict('records'),
                style_table={'height': '70vh', 'width': '100%', 'overflowY': 'auto'},  # Menggunakan vh untuk tinggi tabel
                style_cell={'textAlign': 'left', 'padding-left': '25px'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold', 'textAlign': 'center', 'textTransform': 'capitalize'},
                sort_action="native",  # Enable sorting
                sort_mode="multi",     # Allow sorting by multiple columns
                page_size=21,          # Menentukan jumlah baris per halaman
                page_action='native'   # Mengaktifkan pagination
            )
        ]),
        dcc.Tab(label='Category Statistics', children=[
            dash_table.DataTable(
                id='data-table',
                columns=[{"name": i, "id": i} for i in category_stats.columns],
                data=category_stats.to_dict('records'),
                style_table={'height': '70vh', 'overflowY': 'auto'},  # Menggunakan vh untuk tinggi tabel
                style_cell={'textAlign': 'left', 'padding-left': '25px'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold', 'textAlign': 'center', 'textTransform': 'capitalize'},
            )
        ]),
        dcc.Tab(label='Average Views', children=[
            dcc.Graph(id='avg-views-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Total Views', children=[
            dcc.Graph(id='total-views-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Average Likes', children=[
            dcc.Graph(id='avg-likes-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Total Likes', children=[
            dcc.Graph(id='total-likes-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Average Dislikes', children=[
            dcc.Graph(id='avg-dislikes-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Total Dislikes', children=[
            dcc.Graph(id='total-dislikes-graph', style={'height': '70vh'})
        ]),
        dcc.Tab(label='Number of Videos', children=[
            dcc.Graph(id='number-of-videos-graph', style={'height': '70vh'})
        ])
    ], style={'padding': '20px'})  # Menambahkan padding ke dcc.Tabs
])

# Define the callback functions
@app.callback(
    [Output('avg-views-graph', 'figure'),
     Output('total-views-graph', 'figure'),
     Output('avg-likes-graph', 'figure'),
     Output('total-likes-graph', 'figure'),
     Output('avg-dislikes-graph', 'figure'),
     Output('total-dislikes-graph', 'figure'),
     Output('number-of-videos-graph', 'figure'),
     Output('video-table', 'data'),
     Output('data-table', 'data')],
    [Input('category-dropdown', 'value')]
)
def update_graphs(selected_categories):
    # Ensure selected_categories is a list
    if not isinstance(selected_categories, list):
        selected_categories = [selected_categories]
    
    filtered_data = data[data['Category'].isin(selected_categories)]
    filtered_category_stats = category_stats[category_stats['Category'].isin(selected_categories)]

    avg_views_fig = px.bar(filtered_category_stats, x='Category', y='Avg Views', title='Rata-rata Views per Kategori', color='Category')
    total_views_fig = px.bar(filtered_category_stats, x='Category', y='Total Views', title='Total Views per Kategori', color='Category')
    avg_likes_fig = px.bar(filtered_category_stats, x='Category', y='Avg Likes', title='Rata-rata Likes per Kategori', color='Category')
    total_likes_fig = px.bar(filtered_category_stats, x='Category', y='Total Likes', title='Total Likes per Kategori', color='Category')
    avg_dislikes_fig = px.bar(filtered_category_stats, x='Category', y='Avg Dislikes', title='Rata-rata Dislikes per Kategori', color='Category')
    total_dislikes_fig = px.bar(filtered_category_stats, x='Category', y='Total Dislikes', title='Total Dislikes per Kategori', color='Category')
    number_of_videos_fig = px.pie(filtered_category_stats, names='Category', values='Total Videos', title='Jumlah Video per Kategori')

    return (avg_views_fig, total_views_fig, avg_likes_fig, total_likes_fig, avg_dislikes_fig, total_dislikes_fig, 
            number_of_videos_fig, filtered_data.to_dict('records'), filtered_category_stats.to_dict('records'))

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
