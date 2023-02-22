# WorldSustainabilityDashboard

## Project Proposal

### 1. Motivation and purpose

_Our role:_ Data scientist consultancy firm

_Target audience:_ Responsible citizen

_Goal:_ The goal of sustainability is to meet the needs of the present generation without compromising the ability of future generations to meet their own needs. In other words, it is about finding a way to achieve economic, social, and environmental progress in a way that is sustainable over the long term.


### 2. Description of the data

**The following text was copied from the data source: 
https://www.kaggle.com/datasets/truecue/worldsustainabilitydataset**

> The dataset tracks the performance of 173 countries aginst a range of sustainability metrics over a 19-year period (2000-2018).

Fields include:

* Country Name _(string)_ - Name of the country
* Year _(int)_ - Year for which metrices are collected
* Access to electricity (% of population) _(float)_ - Population proportion having access to electricity
* Individuals using the Internet (% of population) _(float)_ - Population proportion using internet facility
* Annual production-based emissions of carbon dioxide (CO2) _(float)_ - total CO2 emissions in million tonnes 
* Adjusted savings: carbon dioxide damage (% of GNI) _(float)_ - cost of environment damage due to C02 emission.
* Unemployment rate, male (%) _(float)_ - Male unemployment rate
* Unemployment rate, women (%) _(float)_ - Female unemployment rate
* Exports of goods and services (% of GDP) _(float)_ - Percentage of GDP comprising of export goods
* Imports of goods and services (% of GDP) _(float)_ - Percentage of GDP comprising of import goods
* Income Classification _(categorical)_ - Imcome group of the country for a particular year
* GDP_per_capita _(float)_ - GDP per capita of the country for a particular year
* Population _(integer)_ - Population of the particular country
* Inflation _(float)_ - Inflation percentage of the country for a particular year
* Primary_school_enrollment _(float)_ - % of students enrolled in primary education
* Secondary_school_enrollment _(float)_ - % of students enrolled in secondary education



**Data Cleaning:**

In order to facilitate visualization, a few changes will have to be made:

* Some of the contionous variables have missing values which needs to be treated with mean or some calculations based on other variables depending on the attribute.
* We might drop a very small number of countries for which geocodes are missing or cannot be found.


### 3. Research questions and usage scenarios

**Questions:**

* Which countries has the best sustainability index or living standard in the world?
* Which countries have the worst living standard (i.e. very low value of sustainability index) in the world?
* For a given country what proportion of population is using internet, given they have access to electricity?
* For a given country what is the proportion of adjusted savings: C02 damage for given CO2 emission from production annually?
* What is the literacy level of the selected country?
* Elucidate disparity between employment of male and female for a given country.
* How is the proportion of trade for a given country's Gross Domestic Product(GDP)?
* What is the distribution of income classes for a given year across the world?
* What is the relationship between Inflation and GDP per capita across all the countries in last 2 decades(2000-2018)?



**Use scenarios:**


* Country and regional benchmarking: The WSI can be used to compare the sustainability performance of different countries or regions, providing a benchmark for policymakers to assess progress and identify areas for improvement.
* Investor decision-making: Investors can use the WSI to assess the sustainability performance of companies they are considering investing in. This can help investors to identify companies that are well-managed and have a long-term sustainable business model.
* Corporate sustainability reporting: Companies can use the WSI to benchmark their sustainability performance against their peers and identify areas for improvement. This can help companies to prioritize sustainability efforts and develop a more comprehensive sustainability strategy.
* Policy development: Policymakers can use the WSI to inform the development of policies and regulations that promote sustainability. This can help to align policies with the sustainability goals of the country or region and promote sustainable economic development.
* Education and awareness-raising: The WSI can be used as an educational tool to raise awareness of sustainability challenges and promote sustainable behavior among individuals and organizations.




## App Sketch and Description

You can find this in our [README.md](./README.md) file.
