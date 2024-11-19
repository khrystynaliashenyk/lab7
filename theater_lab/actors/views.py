from django.shortcuts import render, get_object_or_404, redirect
from .forms import ActorForm, TheaterForm, DirectorForm
from NetworkHelper import NetworkHelper

def home(request):
    return render(request, 'home.html')

def actor_list(request):
    actors = NetworkHelper.get_list('actors')
    return render(request, 'actors/actor_list.html', {'actors': actors})


def actor_create_or_edit(request, pk=None):
    actor = NetworkHelper.get_item('actors', pk) if pk else None
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            actor_data = form.save(commit=False)
            if pk:
                success = NetworkHelper.update_item('actors', pk, {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
            else:
                success = NetworkHelper.create_item('actors', {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)

    return render(request, 'actors/actor_create_or_edit.html', {'form': form})


def actor_detail(request, pk):
    actor = NetworkHelper.get_item('actors', pk)  # Замініть 'actors' на правильний endpoint API
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def actor_delete(request, pk):
    # Attempt to delete the actor using the API
    success = NetworkHelper.delete_item('actors', pk)  # Replace 'actors' with the correct endpoint
    if success:
        return redirect('actor_list')
    return render(request, 'actors/', {'message': 'Failed to delete actor'})


from context import Context
context = Context()
def director_list(request):
    directors = context.directors.get_all()
    return render(request, 'directors/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = context.directors.get_by_id(pk)
    return render(request, 'directors/director_detail.html', {'director': director})

def director_create_or_edit(request, pk=None):
    director = context.directors.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director_data = form.save(commit=False)
            if pk:
                context.directors.update(director.id, director_data.first_name, director_data.last_name, director_data.date_of_birth)
            else:
                context.directors.create(director_data.first_name, director_data.last_name, director_data.date_of_birth)
            return redirect('director_list')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'directors/director_create_or_edit.html', {'form': form})

def director_delete(request, pk):
    director = context.directors.get_by_id(pk)
    if request.method == "POST":
        director.delete()
        return redirect('director_list')
    return render(request, 'directors/confirm_delete.html', {'director': director})

def theater_list(request):
    theaters = context.theaters.get_all()
    return render(request, 'theaters/theater_list.html', {'theaters': theaters})

def theater_detail(request, pk):
    theater = context.theaters.get_by_id(pk)
    return render(request, 'theaters/theater_detail.html', {'theater': theater})
def theater_create_or_edit(request, pk=None):
    theater = context.theaters.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = TheaterForm(request.POST, instance=theater)
        if form.is_valid():
            theater_data = form.save(commit=False)
            if pk:
                context.theaters.update(theater.id, theater_data.name, theater_data.address, theater_data.number_of_halls)
            else:
                context.theaters.create(theater_data.name, theater_data.address, theater_data.number_of_halls)
            return redirect('theater_list')
    else:
        form = TheaterForm(instance=theater)
    return render(request, 'theaters/theater_create_or_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .forms import ActorForm, TheaterForm, DirectorForm
from NetworkHelper import NetworkHelper

def home(request):
    return render(request, 'home.html')

def actor_list(request):
    actors = NetworkHelper.get_list('actors')
    return render(request, 'actors/actor_list.html', {'actors': actors})


def actor_create_or_edit(request, pk=None):
    actor = NetworkHelper.get_item('actors', pk) if pk else None
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            actor_data = form.save(commit=False)
            if pk:
                success = NetworkHelper.update_item('actors', pk, {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
            else:
                success = NetworkHelper.create_item('actors', {
                    'first_name': actor_data.first_name,
                    'last_name': actor_data.last_name,
                    'date_of_birth': actor_data.date_of_birth,
                })
                if success:
                    return redirect('actor_list')
    else:
        form = ActorForm(instance=actor)

    return render(request, 'actors/actor_create_or_edit.html', {'form': form})


def actor_detail(request, pk):
    actor = NetworkHelper.get_item('actors', pk)  # Замініть 'actors' на правильний endpoint API
    return render(request, 'actors/actor_detail.html', {'actor': actor})

def actor_delete(request, pk):
    # Attempt to delete the actor using the API
    success = NetworkHelper.delete_item('actors', pk)  # Replace 'actors' with the correct endpoint
    if success:
        return redirect('actor_list')
    return render(request, 'actors/', {'message': 'Failed to delete actor'})


from context import Context
context = Context()
def director_list(request):
    directors = context.directors.get_all()
    return render(request, 'directors/director_list.html', {'directors': directors})

def director_detail(request, pk):
    director = context.directors.get_by_id(pk)
    return render(request, 'directors/director_detail.html', {'director': director})

def director_create_or_edit(request, pk=None):
    director = context.directors.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            director_data = form.save(commit=False)
            if pk:
                context.directors.update(director.id, director_data.first_name, director_data.last_name, director_data.date_of_birth)
            else:
                context.directors.create(director_data.first_name, director_data.last_name, director_data.date_of_birth)
            return redirect('director_list')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'directors/director_create_or_edit.html', {'form': form})

def director_delete(request, pk):
    director = context.directors.get_by_id(pk)
    if request.method == "POST":
        director.delete()
        return redirect('director_list')
    return render(request, 'directors/confirm_delete.html', {'director': director})

def theater_list(request):
    theaters = context.theaters.get_all()
    return render(request, 'theaters/theater_list.html', {'theaters': theaters})

def theater_detail(request, pk):
    theater = context.theaters.get_by_id(pk)
    return render(request, 'theaters/theater_detail.html', {'theater': theater})
def theater_create_or_edit(request, pk=None):
    theater = context.theaters.get_by_id(pk) if pk else None
    if request.method == "POST":
        form = TheaterForm(request.POST, instance=theater)
        if form.is_valid():
            theater_data = form.save(commit=False)
            if pk:
                context.theaters.update(theater.id, theater_data.name, theater_data.address, theater_data.number_of_halls)
            else:
                context.theaters.create(theater_data.name, theater_data.address, theater_data.number_of_halls)
            return redirect('theater_list')
    else:
        form = TheaterForm(instance=theater)
    return render(request, 'theaters/theater_create_or_edit.html', {'form': form})

def theater_delete(request, pk):
    theater = context.theaters.get_by_id(pk)
    if request.method == "POST":
        theater.delete()
        return redirect('theater_list')
    return render(request, 'theaters/confirm_delete.html', {'theater': theater})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from repositories.queries import *  # Import queries
import pandas as pd
@api_view(['GET'])
def total_buyer_count(request):
    total_buyers = get_total_buyer_count()
    return Response(total_buyers)

@api_view(['GET'])
def play_count_by_genre(request):
    queryset = get_play_count_by_genre()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))


from django.shortcuts import render
from .dashboards import *
import pandas as pd
import requests


def dashboard_view(request):
    # Fetch data from the REST API endpoint
    response = requests.get('http://127.0.0.1:8000/theater/api/plays/genre-count/')

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response into a dictionary
        df = pd.DataFrame(data)  # Convert the data to a pandas DataFrame

        # Generate the Plotly chart using the data
        plot = plot_play_count_by_genre(df)
        return render(request, 'dashboard.html', {'plotly_chart': plot.to_html()})
    else:
        return render(request, 'dashboard.html', {'error': 'Failed to fetch data from API'})


@api_view(['GET'])
def avg_duration_by_genre(request):
    queryset = get_avg_duration_by_genre()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

def dashboard_view_plotly(request):
    # Запит до API для отримання даних
    response = requests.get('http://127.0.0.1:8000/theater/api/plays/avg-duration-by-genre/')

    if response.status_code == 200:
        data = response.json()  # Отримання даних у форматі JSON
        df = pd.DataFrame(data)  # Перетворення у DataFrame

        # Створення графіка за допомогою Plotly
        plot = plot_genre_chart(df)

        # Повернення результату для рендерингу Plotly графіка
        return render(request, 'plotly_dashboard.html', {'plotly_chart': plot.to_html()})
    else:
        return render(request, 'plotly_dashboard.html', {'error': 'Failed to fetch data from API'})

@api_view(['GET'])
def avg_ticket_price_by_play(request):
    queryset = get_avg_ticket_price_by_play()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def total_revenue_by_play(request):
    queryset = get_total_revenue_by_play()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def plays_by_director(request):
    queryset = get_plays_by_director()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def seat_occupancy_per_hall(request):
    queryset = get_seat_occupancy_per_hall()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))

@api_view(['GET'])
def play_count_by_year(request):
    queryset = get_play_count_by_year()
    df = pd.DataFrame(list(queryset))
    return Response(df.to_dict(orient='records'))


# views.py (updated)

import pandas as pd
import plotly.express as px
import requests


# views.py

import pandas as pd
import plotly.express as px
import requests
from django.shortcuts import render

# Example of generating a Plotly bar chart for play counts by genre
def plot_play_count_by_genre(df):
    fig = px.bar(df, x='genre', y='play_count', title='Number of Plays by Genre')
    return fig

def dashboard_view1(request):
    # Fetch data from the REST API endpoints
    response_avg_ticket_price = requests.get('http://127.0.0.1:8000/theater/api/plays/avg-ticket-price/')
    response_total_revenue = requests.get('http://127.0.0.1:8000/theater/api/plays/total-revenue/')
    response_seat_occupancy = requests.get('http://127.0.0.1:8000/theater/api/seats/occupancy/')

    if  response_avg_ticket_price.status_code == 200 and \
       response_total_revenue.status_code == 200 and  \
       response_seat_occupancy.status_code == 200 :

        # Convert API responses into DataFrames
        data_avg_ticket_price = pd.DataFrame(response_avg_ticket_price.json())
        data_total_revenue = pd.DataFrame(response_total_revenue.json())
        data_seat_occupancy = pd.DataFrame(response_seat_occupancy.json())

        # Generate different plots
        plot_avg_ticket_price = plot_avg_ticket_price_by_play(data_avg_ticket_price)
        plot_total_revenue = plot_total_revenue_by_play(data_total_revenue)
        plot_seat_occupancy = plot_seat_occupancy_per_hall(data_seat_occupancy)

        # Render dashboard with all plots
        return render(request, 'dashboard1.html', {
            'plot_avg_ticket_price': plot_avg_ticket_price.to_html(),
            'plot_total_revenue': plot_total_revenue.to_html(),
            'plot_seat_occupancy': plot_seat_occupancy.to_html(),
        })
    else:
        # If API fails, render the error page
        return render(request, 'dashboard1.html', {'error': 'Failed to fetch data from API'})





from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models import ColumnDataSource
import pandas as pd

def bokeh_play_count_by_genre(df):
    """
    Створення графіка для кількості п'єс за жанрами за допомогою Bokeh.
    """
    if 'genre' not in df.columns or 'play_count' not in df.columns:
        raise ValueError("DataFrame must contain 'genre' and 'play_count' columns")

    source = ColumnDataSource(data=df)

    # Створення графіка
    plot = figure(
        x_range=df['genre'],
        plot_height=400,
        plot_width=700,
        title="Number of Plays by Genre",
        toolbar_location=None,
        tools=""
    )
    plot.vbar(x='genre', top='play_count', width=0.8, source=source, color='navy')

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0
    plot.xaxis.axis_label = "Genre"
    plot.yaxis.axis_label = "Number of Plays"

    return plot


def bokeh_avg_ticket_price_by_play(df):
    """
    Створення графіка для середньої ціни квитка за виставами за допомогою Bokeh.
    """
    if 'schedule__play__title' not in df.columns or 'avg_price' not in df.columns:
        raise ValueError("DataFrame must contain 'schedule__play__title' and 'avg_price' columns")

    source = ColumnDataSource(data=df)

    plot = figure(
        x_range=df['schedule__play__title'],
        plot_height=400,
        plot_width=700,
        title="Average Ticket Price by Play",
        toolbar_location=None,
        tools=""
    )
    plot.vbar(x='schedule__play__title', top='avg_price', width=0.8, source=source, color='orange')

    plot.xgrid.grid_line_color = None
    plot.y_range.start = 0
    plot.xaxis.axis_label = "Play Title"
    plot.yaxis.axis_label = "Average Ticket Price"

    return plot


def dashboard_view_bokeh(request):
    # Fetch data from the REST API endpoints
    response_avg_ticket_price = requests.get('http://127.0.0.1:8000/theater/api/plays/avg-ticket-price/')
    response_play_count = requests.get('http://127.0.0.1:8000/theater/api/plays/count-by-genre/')

    if response_avg_ticket_price.status_code == 200 and response_play_count.status_code == 200:
        # Перетворення API-відповідей у DataFrame
        data_avg_ticket_price = pd.DataFrame(response_avg_ticket_price.json())
        data_play_count = pd.DataFrame(response_play_count.json())

        # Побудова графіків за допомогою Bokeh
        plot1 = bokeh_avg_ticket_price_by_play(data_avg_ticket_price)
        plot2 = bokeh_play_count_by_genre(data_play_count)

        # Отримання компонентів для вбудовування в HTML
        script1, div1 = components(plot1)
        script2, div2 = components(plot2)

        return render(request, 'dashboard_bokeh.html', {
            'bokeh_script1': script1,
            'bokeh_div1': div1,
            'bokeh_script2': script2,
            'bokeh_div2': div2,
        })
    else:
        return render(request, 'dashboard_bokeh.html', {'error': 'Failed to fetch data from API'})
