import plotly.express as px

def plot_play_count_by_genre(df):
    fig = px.bar(df, x='genre', y='play_count', title='Number of Plays by Genre')
    return fig

import plotly.express as px


# Графік середньої тривалості вистав за жанром
def plot_genre_chart(df):
    """
    Побудова графіка для середньої тривалості п'єс за жанрами.
    """
    if 'genre' not in df.columns or 'avg_duration' not in df.columns:
        raise ValueError("DataFrame must contain 'genre' and 'avg_duration' columns")

    # Створення графіка за допомогою Plotly Express
    fig = px.pie(
        df,
        names='genre',  # Категорії (жанри)
        values='avg_duration',  # Значення (середня тривалість)
        title='Average Play Duration by Genre',
        template='plotly_white'
    )

    return fig

import plotly.express as px


def plot_avg_ticket_price_by_play(df):
    fig = px.pie(df, names='schedule__play__title', values='avg_price', title='Average Ticket Price by Play')
    return fig

def plot_play_count_by_year(df):
    fig = px.line(df, x='year', y='play_count', title='Number of Plays by Year', markers=True)
    return fig

def plot_total_revenue_by_play(df):
    fig = px.bar(df, x='schedule__play__title', y='total_revenue', title='Total Revenue by Play')
    return fig

def plot_seat_occupancy_per_hall(df):
    fig = px.pie(df, names='hall__name', values='seat_count', title='Seat Occupancy by Hall')
    return fig

def plot_plays_by_director(df):
    fig = px.bar(df, x='director__first_name', y='play_count', title='Number of Plays by Director')
    return fig

