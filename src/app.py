#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import altair as alt
from vega_datasets import data
import pandas as pd
import altair as alt
import socket

x = socket.gethostbyname("")


dataset = pd.read_csv('Sustainability_cleaned.csv',parse_dates=['Year'])

#dataset['Year'] = pd.to_datetime(dataset['Year'], format='%Y').dt.year

# Define the app and its layout
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([ 
    html.H1('World Sustainability Dashboard',
            style={
            'textAlign': 'center',
            'color': 'blue'
        }),
    dbc.Tabs([
        # First tab
        dbc.Tab(label='Social', children=[
            # First row
            dbc.Row([
                # First column (slider)
                dbc.Col([
                    html.Label('Slider'),
                    dcc.RangeSlider(
                        id='slider-soc',
                        min=dataset['Year'].dt.year.min(),
                        max=dataset['Year'].dt.year.max(),
                        step=1,
                        vertical=True,
                        value=[dataset['Year'].min(),dataset['Year'].dt.year.max()],
                        marks={str(year): str(year) for year in dataset['Year'].dt.year.unique()},
                    ),
                    dcc.Dropdown(
                        id='dropdown-soc',
                        options=[{'label': i, 'value': i} for i in dataset['Country'].unique()],
                        value='Finland'
                    )], 
                    width=3,md=3),
                # Second column (chart-1)
                dbc.Col(
                    html.Iframe(
                        id='social-1',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'})),
                # Third column (chart-2)
                dbc.Col(
                    html.Iframe(
                        id='social-2',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}))
            ]),
        ]),# Second tab close
    ]),# Tabs close
])# Container close


# Define the callbacks to update the charts



@app.callback(
    Output('social-1', 'srcDoc'),
    Input('slider-soc', 'value'),
    Input('dropdown-soc', 'value'))
def soc_1(slider_value, dropdown_value):
    #min_value = slider_value[0]
    #max_value = slider_value[1]
    years_range = range(slider_value[0], slider_value[1] + 1)
    
    # Filter the data based on the dropdown values
    filtered_country = dataset[dataset['Country']== dropdown_value]
    
    # Filter the data based on the slider values
    #filtered_df = my_df[my_df['year'].isin(year_range)]
    filtered_year = filtered_country[filtered_country['Year'].dt.year.isin(years_range)]
    
    # Rename columns 
    df_renamed = filtered_year.rename(columns={'Primary_school_enrol': 'Primary','Secondary_school_enrol':'Secondary'})

    # Create chart  
    chart = alt.Chart(df_renamed).mark_line(point=True).transform_fold(
        fold=['Primary', 'Secondary'],
        as_=['variable', 'value']
    ).encode(
        alt.X('Year', title = None),
        alt.Y('max(value):Q', title="Enrolment (%)", scale=alt.Scale(zero=False)),
        color=alt.Color('variable:N', legend=alt.Legend(title='School Enrolment')),
        tooltip=[alt.Tooltip('Year:T', format='%Y'), alt.Tooltip('max(value):Q')]
    ).properties(title="Literacy Level")

    return chart.to_html()

@app.callback(
    Output('social-2', 'srcDoc'),
    Input('slider-soc', 'value'),
    Input('dropdown-soc', 'value'))
def soc_2(slider_value, dropdown_value):
    #min_value = slider_value[0]
    #max_value = slider_value[1]
    years_range = range(slider_value[0], slider_value[1] + 1)
    
    # Filter the data based on the dropdown values
    filtered_country = dataset[dataset['Country']== dropdown_value]
    
    # Filter the data based on the slider values
    #filtered_year = filtered_country[(filtered_country['Year'] >= min_value) & (filtered_country['Year'] <= max_value)]
    filtered_year = filtered_country[filtered_country['Year'].dt.year.isin(years_range)]
    
    # Rename columns 
    df_renamed = filtered_year.rename(columns={'Unemployment_rate_male': 'Male','Unemployment_rate_women':'Female'})

    # Create chart  
    chart = alt.Chart(df_renamed).mark_line(point=True).transform_fold(
        fold=['Male', 'Female'],
        as_=['variable', 'value']
    ).encode(
        alt.X('Year', title =None),
        alt.Y('max(value):Q', title="Unemployment Rate(%)", scale=alt.Scale(zero=False)),
        color=alt.Color('variable:N', legend=alt.Legend(title='Gender')),
        tooltip=[alt.Tooltip('Year', format='%Y'), alt.Tooltip('max(value):Q')]   
    ).properties(title="Gender Gap in Unemployment")

    return chart.to_html()


if __name__ == '__main__':
    app.run_server(x)                  
                     
                     
