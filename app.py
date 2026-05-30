import os
import runpy
from pathlib import Path

import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from dotenv import load_dotenv

# 1. SETUP
load_dotenv(dotenv_path="atlas_keys.env")
FRED_API_KEY = os.getenv("FRED_API_KEY")

st.set_page_config(layout="wide", page_title="DebtAtlas")

pages = {
    "Dashboard": None,
    "Sources & Methods": "pages/1_Sources_and_Methods.py",
    "About": "pages/2_About.py",
}

selected_page = st.sidebar.selectbox("Navigate", list(pages.keys()))

# 2. PAGE ROUTING
if pages[selected_page] is not None:
    page_path = Path(pages[selected_page])
    if page_path.exists():
        runpy.run_path(str(page_path), run_name="__main__")
    else:
        st.error(f"Page script not found: {page_path}")
    st.stop()

st.title("DebtAtlas: Unified Fiscal Liability Map")
st.write("This dashboard unifies federal, state, and municipal debts.")

# 3. DATA LOGIC
@st.cache_data(ttl=86400)
def get_live_federal_debt():
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id=GFDEBTN&api_key={FRED_API_KEY}&file_type=json"
    try:
        response = requests.get(url).json()
        latest_observation = response["observations"][-1]
        raw_debt_millions = float(latest_observation["value"])
        return raw_debt_millions * 1_000_000, None
    except:
        return 39_171_154_946_667, None

fed_total, _ = get_live_federal_debt()
state_df = pd.read_csv("state_debt_data.csv")
us_population_est = 336_000_000
fed_per_capita = fed_total / us_population_est

state_df["Federal_Debt_Per_Capita"] = fed_per_capita
state_df["Combined_Total_Debt"] = state_df["State_Debt_Per_Capita"] + state_df["Avg_Muni_Debt_Per_Capita"] + state_df["Federal_Debt_Per_Capita"]

# 3. MAP
fig = px.choropleth(
    state_df, locations="State_Code", locationmode="USA-states",
    color="Combined_Total_Debt", scope="usa", color_continuous_scale="Purples"
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# 4. DRILLDOWN
selected_state = st.selectbox("Select a State:", state_df["State_Code"])
state_row = state_df[state_df["State_Code"] == selected_state].iloc[0]
col1, col2, col3 = st.columns(3)
col1.metric("Federal Layer", f"${state_row['Federal_Debt_Per_Capita']:,.2f}")
col2.metric("State Layer", f"${state_row['State_Debt_Per_Capita']:,.2f}")
col3.metric("Muni Layer", f"${state_row['Avg_Muni_Debt_Per_Capita']:,.2f}")