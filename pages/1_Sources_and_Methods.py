import streamlit as st

st.title("📂 Sources and Methods")

st.markdown("### 📂 Data Sources & Methodology")

st.markdown(
    "**Our Philosophy: Breaking the Jurisdictional Silos**\n\n"
    "Public debt is often reported in isolated segments—federal, state, and local. This creates a \"transparency gap\" where the total burden on a single taxpayer is rarely visible. DebtAtlas integrates these disparate streams into a unified, per-capita liability metric."
)

st.markdown("### 1. Federal Layer: The Macro-Baseline")
st.markdown(
    "We pull real-time gross national debt data directly from the **Federal Reserve Bank of St. Louis (FRED) API**.\n\n"
    "* **Series:** `GFDEBTN` (Gross Federal Debt).\n"
    "* **Methodology:** We capture total outstanding gross debt to reflect the comprehensive national liability, not just debt held by the public. This total is distributed across the U.S. population to determine a baseline federal liability per resident."
)

st.markdown("### 2. State Layer: The Structural Debt")
st.markdown(
    "Data is derived from the **U.S. Census Bureau’s Annual Survey of State and Local Government Finances**.\n\n"
    "* **Metrics:** We isolate \"Full Faith and Credit\" long-term bonds.\n"
    "* **Methodology:** This represents the debt directly issued by state governments for infrastructure, public works, and budgetary operations."
)

st.markdown("### 3. Municipal/Local Layer: The Granular Burden")
st.markdown(
    "Aggregated from local government finance records, including:\n\n"
    "* **Entities:** County governments, independent school districts, and special-purpose transit/utility authorities.\n"
    "* **Methodology:** Municipal debt structures vary significantly by state law. We aggregate these liabilities within each state to calculate an \"Average Municipal Debt Per Capita,\" providing a standardized way to compare states that decentralize debt differently."
)

st.markdown("### 4. Normalization Policy")
st.markdown(
    "* **Population Lag:** All per-capita calculations utilize the latest annualized Census population estimates.\n"
    "* **Normalization:** By converting all layers to a per-capita metric, we strip away the bias caused by state population size, allowing for a direct, apples-to-apples comparison of fiscal responsibility."
)
