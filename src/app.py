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

#x = socket.gethostbyname("")


dataset = pd.read_csv('Sustainability_cleaned.csv',parse_dates=['Year'])

#dataset['Year'] = pd.to_datetime(dataset['Year'], format='%Y').dt.year

# Define the app and its layout
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#Adding server variable
server = app.server

#-------------------------------------------------
# World Map code

# Load data from CSV
df = pd.read_excel("Sustainability.xlsx")

# Create the base map chart
base_map = alt.Chart(alt.topo_feature('https://vega.github.io/vega-datasets/data/world-110m.json', 'countries')).mark_geoshape(
    stroke='white',
    strokeWidth=0.5
).properties(
    width=700,
    height=400
)

# Create the choropleth map chart
choro_map = base_map.transform_lookup(
    lookup='id',
    from_=alt.LookupData(df,'id',['WSI','Country'])
).encode(
    color=alt.Color('WSI:Q', scale=alt.Scale(scheme='greenblue')),
    tooltip=['Country:N', 'WSI:Q']
)

# Combine the two charts into one

def world_chart():
    world_chart = alt.layer(
    base_map, choro_map
).configure_view(
    stroke=None
)

    return world_chart.to_html()

# display the chart with tooltip
#world_plot.interactive()

world_plot_1 = html.Div([
    html.Iframe(
        id="world_plot_id_1",
        srcDoc=world_chart(),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}
    )
])

row1_col1_world = dbc.Row(html.Div("World Sustainability Index - 2018", style = {"font-weight": "bolder", 'text-align': "left"}))

row1_world = html.Div([dbc.Row(
    [
        dbc.Col(row1_col1_world, md=6)
    ]
    )]
)

row1_col1_world = dbc.Row(world_plot_1)

row2_world = html.Div([dbc.Row(
    [
        dbc.Col(row1_col1_world)
    ]
    )], 
    style={"padding-bottom": 0}
)

col3_world = html.Div(
    [
        row1_world,       # has titles of plots of first row
        row2_world      # has top two plots
    ],
    style={'padding-left': 0, "padding-right": 0}
    )
    
main_row_world = html.Div([
    dbc.Row([
        #dbc.Col(col1_shveta, md=1),    # slider column
        dbc.Col(col3_world, md=8),    # Cards column
    ])
],
style={'padding-top': "30px"})


########## layout ################################
tab_0 = dbc.Container([
    main_row_world
])

##main layout

app.layout = dbc.Container([ 
    html.H1('World Sustainability Dashboard',
            style={
            'textAlign': 'center',
            'color': 'blue'
        }),
    dbc.Tabs([
        dbc.Tab([tab_0], label = 'World'),
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
                        value=[2000,2018],
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
                        value=[2000,2018],
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
        
         
        # Third tab open
        dbc.Tab(label='Economic', children=[
            # First row
            dbc.Row([
                # First column (slider)
                dbc.Col([
                    html.Label('Slider'),
                    dcc.RangeSlider(
                        id='slider-eco',
                        min=dataset['Year'].dt.year.min(),
                        max=dataset['Year'].dt.year.max(),
                        step=1,
                        vertical=True,
                        value=[2000,2018],
                        marks={str(year): str(year) for year in dataset['Year'].dt.year.unique()},
                    ),
                    dcc.Dropdown(
                        id='dropdown-eco',
                        options=[{'label': i, 'value': i} for i in dataset['Country'].unique()],
                        value='Finland'
                    )], 
                    width=3,md=3),
                # Second column (chart-1)
                dbc.Col(
                    html.Iframe(
                        id='eco-1',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}))
            ]),
        ]),# Third tab close
        
        # Fourth tab open
        dbc.Tab(label='Summary', children=[
            # First row
            dbc.Row([
                # First column (slider)
                dbc.Col([
                    html.Label('Select a year'),
                    dcc.Dropdown(
                        id='year-summ',
                        options=[{'label': i, 'value': i} for i in dataset['Year'].dt.year.unique()],
                        value= 2018
                    ),
                    html.Br(),
                    html.Label('Select an Income Group'),
                    dcc.Dropdown(
                        id='income-summ',
                        options=[{'label': i, 'value': i} for i in dataset['Income_classification'].unique()],
                        value = ['High income','Low income','Upper-middle income','Lower-middle income'],
                        multi = 'True'
                    )], 
                    width=3,md=3),
                # Second column (chart-1)
                dbc.Col(
                    html.Iframe(
                        id='summ-1',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'})),
                # Third column (chart-2)
                dbc.Col(
                    html.Iframe(
                        id='summ-2',
                        style={'border-width': '0', 'width': '100%', 'height': '400px'}))
            ]),
        ]),# Fourth tab close
        
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
    )

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

@app.callback(
    Output('eco-1', 'srcDoc'),
    Input('slider-eco', 'value'),
    Input('dropdown-eco', 'value'))
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
    melted = pd.melt(filtered_year, id_vars=['Year'], value_vars=['Imports', 'Exports'], var_name='imp_exp',
                     value_name='GDP_per_capita')
    melted['Year'] = pd.DatetimeIndex(melted['Year']).year.astype(str)

    # Create chart  
    chart = alt.Chart(melted).mark_bar().encode(
        alt.X('imp_exp:N', axis=None), # remove x-axis label
        alt.Y('GDP_per_capita:Q', title="Trade(%) of GDP per capita"),
        alt.Color('imp_exp:N', legend=alt.Legend(title="Trade type", orient='bottom')),
        tooltip=[alt.Tooltip('GDP_per_capita:Q', title='GDP per capita'),alt.Tooltip('imp_exp:N', title='Trade type')]
    ).facet(
        column=alt.Column('Year:N', title=None)
    ).properties(
        title=alt.TitleParams(
            "Import and Export as % of GDP per Capita",
            anchor='middle',
            dy=-20
        )
    )      
    return chart.to_html()


@app.callback(
    Output('summ-1', 'srcDoc'),
    Input('year-summ', 'value'),
    Input('income-summ', 'value'))
def summ_1(year_value, income_value):
    
    # Filter the data based on the dropdown values
    filtered_df = dataset[dataset['Income_classification'].isin(income_value)]
    filtered_data = filtered_df[(filtered_df['Year'].dt.year == year_value)]

    # Create chart  
    
    chart = alt.Chart(filtered_data).mark_circle(opacity=0.5, size=100).encode(
    alt.X('GDP_per_capita:Q'),
    alt.Y('Inflation:Q'),
    alt.Size('Population:Q', scale=alt.Scale(range=[10, 2000]), legend=None),
    alt.Color('Country:N',legend = None),
    alt.Tooltip(['Country', 'Inflation'])
).properties(height=300, width=400)
    
    return chart.to_html()

@app.callback(
    Output('summ-2', 'srcDoc'),
    Input('year-summ', 'value'),
    Input('income-summ', 'value'))
def summ_2(year_value, income_value):
    
    # Filter the data based on the dropdown values
    filtered_df = dataset[dataset['Income_classification'].isin(income_value)]
    filtered_data = filtered_df[(filtered_df['Year'].dt.year == year_value)]

    # Create chart  
    
    chart = alt.Chart(filtered_data).mark_arc(outerRadius=80).encode(
    theta=alt.Theta('count():Q'),
    color=alt.Color('Income_classification:N'),
    tooltip=["Income_classification", "count()"])
    
    return chart.to_html()




if __name__ == '__main__':
    app.run_server(debug=True)                                                    
