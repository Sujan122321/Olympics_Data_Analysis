import streamlit as st
import pandas as pd
from helpers import *
import matplotlib.pyplot as plt

summer,winter =data_preprocessor()
summer,winter =duplicate_rows_remover(summer,winter)

summer.dropna(subset=["region"],inplace=True)
winter.dropna(subset=["region"],inplace=True)

st.sidebar.title("Menu")
season = st.sidebar.radio("Choose Season: ",("Summer","Winter"))
options = st.sidebar.radio("Options",("Medal-Tally","Country-Wise","Year-Wise","Year-Wise Progress"))


### 1. Medal-Tally

if season =="Summer" and options == "Medal-Tally":
    st.subheader("Summer Olymmpics Medal Tally")
    medal_pivot_summer =medal_tally_calculator(summer)
    medal_pivot_summer=medal_pivot_summer.sort_values(by=["Gold","Silver","Bronze"],ascending=False)
    st.dataframe(medal_pivot_summer, width =700)
    
elif season =="Winter" and options == "Medal-Tally":
    st.subheader("Winter Olymmpics Medal Tally")
    medal_pivot_winter =medal_tally_calculator(winter)
    medal_pivot_winter=medal_pivot_winter.sort_values(by=["Gold","Silver","Bronze"],ascending=False)
    st.dataframe(medal_pivot_winter, width =700)


## 2. Country Wise

elif season =="Summer" and options == "Country-Wise":
        st.subheader("Summer Country-wise search")
        medal_pivot_summer =medal_tally_calculator(summer)
        noc = st.selectbox("Select NOC :", medal_pivot_summer.index.tolist())
        details = country_wise_search(noc,medal_pivot_summer)
        table =pd.DataFrame.from_dict(details, orient="index", columns=["Value"])
        st.dataframe(table)
    

elif season =="Winter" and options == "Country-Wise":
        st.subheader("Winter Country-wise search")
        medal_pivot_winter =medal_tally_calculator(winter)
        noc = st.selectbox("Select NOC :", medal_pivot_winter.index.tolist())
        details = country_wise_search(noc,medal_pivot_winter)
        table =pd.DataFrame.from_dict(details, orient="index", columns=["Value"])
        st.dataframe(table)

## 3. Year Wise

elif season =="Summer" and options == "Year-Wise":
    st.subheader("Summer Year-wise search")
    years = sorted(summer["Year"].unique())
    selected_year = st.selectbox("Select Years",years)
    countries = sorted(summer[summer["Year"]==selected_year]["region"].unique())
    selected_country = st.selectbox("Select Country : ",countries)
    plot_medals(selected_year,selected_country,summer)
    

elif season =="winter" and options == "Year-Wise":
    st.subheader("winter Year-wise search")
    years = sorted(winter["Year"].unique())
    selected_year = st.selectbox("Select Years",years)
    countries = sorted(winter[winter["Year"]==selected_year]["region"].unique())
    selected_country = st.selectbox("Select Country : ",countries)
    plot_medals(selected_year,selected_country,winter)
    
## 4. Year Wise Progress of a country

elif season =="Summer" and options == "Year-Wise Progress":
    st.subheader("Summer Overall analysis of a country")
    
    countries = sorted(summer["region"].unique())
    selected_country = st.selectbox("Choose Country :" , countries)
    year_analysis(selected_country,summer)

else:
    st.subheader("Winter Overall analysis of a country")
    countries = sorted(winter["region"].unique())
    selected_country = st.selectbox("Choose Country :" , countries)
    year_analysis(selected_country,winter)