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
        dbc.Tab(label='Environmental', children=[
            # First row
            dbc.Row([
                # First column (slider)
                dbc.Col([
                    html.Label('Slider'),
                    dcc.RangeSlider(
                        id='slider-env',
                        min=dataset['Year'].dt.year.min(),
                        max=dataset['Year'].dt.year.max(),
                        step=1,
                        vertical=True,
                        value=[dataset['Year'].min(),dataset['Year'].dt.year.max()],
                        marks={str(year): str(year) for year in dataset['Year'].dt.year.unique()},
                    ),
                    dcc.Dropdown(
                        id='dropdown-env',
                        options=[{'label': i, 'value': i} for i in dataset['Country'].unique()],
                        value='Finland'
                    )], 
                    width=3,md=3),
                # Second column (chart-1)
                dbc.Col(
                    html.Iframe(
                        id='env-1',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'})),
                # Third column (chart-2)
                dbc.Col(
                    html.Iframe(
                        id='env-2',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}))
            ]),
        ]),# First tab close
 
        # Second tab open
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


# Define the callbacks to update the chart

@app.callback(
    Output('env-1', 'srcDoc'),
    Input('slider-env', 'value'),
    Input('dropdown-env', 'value'))
def env_1(slider_value, dropdown_value):
    #min_value = slider_value[0]
    #max_value = slider_value[1]
    years_range = range(slider_value[0], slider_value[1] + 1)
    
    # Filter the data based on the dropdown values
    filtered_country = dataset[dataset['Country']== dropdown_value]


    # Filter the data based on the slider values
    #filtered_year = filtered_country[(filtered_country['Year'] >= min_value) & (filtered_country['Year'] <= max_value)]
    filtered_year = filtered_country[filtered_country['Year'].dt.year.isin(years_range)]
    
    # Create chart
    chart = alt.Chart(filtered_year).mark_circle(opacity=0.7, size=500).encode(
        alt.X('Internet', title='Access to Internet (% of population)'),
        alt.Y('Electricity_access', scale=alt.Scale(zero=False), title='Access to electricity (% of population)'),
        color=alt.Color('Income_classification', title='Income Classification'),
        tooltip=[alt.Tooltip('Internet', title='Access to Internet(% of population)'), 
                alt.Tooltip('Electricity_access',title='Access to electricity (% of population)')]).properties(
        width=500,
        height=400,
        title='Access to Utilities, as a percentage of Population'
    ).interactive()

    return chart.to_html()

@app.callback(
    Output('env-2', 'srcDoc'),
    Input('slider-env', 'value'),
    Input('dropdown-env', 'value'))
def env_2(slider_value, dropdown_value):
    #min_value = slider_value[0]
    #max_value = slider_value[1]
    years_range = range(slider_value[0], slider_value[1] + 1)
    
    # Filter the data based on the dropdown values
    filtered_country = dataset[dataset['Country']== dropdown_value]
    
    # Filter the data based on the slider values
    filtered_year = filtered_country[filtered_country['Year'].dt.year.isin(years_range)]
    
    # create bar chart

    bar_chart = alt.Chart(filtered_year).mark_bar(color='Teal', size=10).encode(
        alt.X('Year:T',title =''),
        alt.Y('Co2_prod_tonnes:Q',title='Annual CO2 production (in tonnes)'),
        tooltip=[alt.Tooltip('Year:T', format='%Y'), alt.Tooltip('Co2_prod_tonnes:Q',title='Annual CO2 production')]
    )

    # create line chart


    line_chart = alt.Chart(filtered_year).mark_line(color='red').encode(
        alt.X('Year:T', title=''),
        alt.Y('Adj_savCO2_damage:Q', title='Adjusted Savings : CO2 Damage (% of GNI)'),
        tooltip=[alt.Tooltip('Year:T', format='%Y'), alt.Tooltip('Adj_savCO2_damage:Q',format='.2f',title='CO2 Damage (% of GNI)')]
    )
    
    # Combine line and bar chart
    
    chart = (bar_chart + line_chart).resolve_scale(
        y='independent'
    ).properties(
        width=500,
        height=400
    ).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    )
   
    return chart.to_html()

##### Social Tab #####

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
                     
                     
