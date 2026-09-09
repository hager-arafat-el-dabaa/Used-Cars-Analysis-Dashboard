import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="Used Cars Dashboard",
    page_icon="🚗",
    layout="wide"
)


# ==================================================
# Custom Dark Theme
# ==================================================

st.markdown("""
<style>

.stApp {
    background-color: #121212;
    color: #F5F5F5;
}

section[data-testid="stSidebar"] {
    background-color: #1E1E1E;
}

h1 {
    color: #FF5722;
    font-weight: 700;
}

h2, h3 {
    color: #F5F5F5;
}

p {
    color: #B0B0B0;
}

/* KPI Cards */
div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 12px;
    padding: 15px;
}

div[data-testid="metric-container"] label {
    color: #B0B0B0;
}

div[data-testid="metric-container"] div {
    color: #FF5722;
}

/* Sidebar */
.stSelectbox label {
    color: #E0E0E0;
}

/* Divider */
hr {
    border-color: #333333;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# Load Data
# ==================================================

df = pd.read_csv("cleaned_car_data.csv")


# ==================================================
# Title
# ==================================================

st.title("🚗 Used Cars Analysis Dashboard")

st.write(
    "Explore used car listings, prices, mileage, brands, "
    "fuel types, and transmission."
)

st.divider()


# ==================================================
# Sidebar Filters
# ==================================================

st.sidebar.title("🔎 Filters")

fuel_options = ["All"] + sorted(
    df["fuel"].dropna().unique().tolist()
)

selected_fuel = st.sidebar.selectbox(
    "Fuel Type",
    fuel_options
)

transmission_options = ["All"] + sorted(
    df["transmission"].dropna().unique().tolist()
)

selected_transmission = st.sidebar.selectbox(
    "Transmission",
    transmission_options
)


# ==================================================
# Apply Filters
# ==================================================

filtered_df = df.copy()

if selected_fuel != "All":
    filtered_df = filtered_df[
        filtered_df["fuel"] == selected_fuel
    ]

if selected_transmission != "All":
    filtered_df = filtered_df[
        filtered_df["transmission"] == selected_transmission
    ]


# ==================================================
# KPI Section
# ==================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Cars",
    f"{len(filtered_df):,}"
)

col2.metric(
    "Average Price",
    f"{filtered_df['selling_price'].mean():,.0f}"
)

col3.metric(
    "Average KM Driven",
    f"{filtered_df['km_driven'].mean():,.0f}"
)

if not filtered_df.empty:
    top_brand = filtered_df["brand"].mode()[0]
else:
    top_brand = "N/A"

col4.metric(
    "Top Brand",
    top_brand
)


st.divider()


# ==================================================
# Selling Price Distribution
# ==================================================

st.subheader("💰 Selling Price Distribution")

fig, ax = plt.subplots(figsize=(12, 4))

fig.patch.set_facecolor("#1E1E1E")
ax.set_facecolor("#1E1E1E")

sns.histplot(
    filtered_df["selling_price"].dropna(),
    bins=40,
    kde=True,
    color="#FF5722",
    ax=ax
)

ax.set_xlabel("Selling Price", color="#E0E0E0")
ax.set_ylabel("Count", color="#E0E0E0")

ax.tick_params(colors="#B0B0B0")

for spine in ax.spines.values():
    spine.set_color("#333333")

st.pyplot(fig)


# ==================================================
# Brands + Fuel
# ==================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("🏷️ Top 10 Car Brands")

    brand_counts = (
        filtered_df["brand"]
        .value_counts()
        .head(10)
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    fig.patch.set_facecolor("#1E1E1E")
    ax.set_facecolor("#1E1E1E")

    brand_counts.plot(
        kind="barh",
        color="#FF5722",
        ax=ax
    )

    ax.set_xlabel("Count", color="#E0E0E0")
    ax.set_ylabel("Brand", color="#E0E0E0")

    ax.tick_params(colors="#B0B0B0")

    for spine in ax.spines.values():
        spine.set_color("#333333")

    st.pyplot(fig)


with col2:

    st.subheader("⛽ Fuel Types")

    fuel_counts = filtered_df["fuel"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))

    fig.patch.set_facecolor("#1E1E1E")
    ax.set_facecolor("#1E1E1E")

    fuel_counts.plot(
        kind="bar",
        color="#FF8A65",
        ax=ax
    )

    ax.set_xlabel("Fuel Type", color="#E0E0E0")
    ax.set_ylabel("Count", color="#E0E0E0")

    ax.tick_params(colors="#B0B0B0")

    for spine in ax.spines.values():
        spine.set_color("#333333")

    st.pyplot(fig)


# ==================================================
# Transmission + Owner
# ==================================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("⚙️ Transmission Types")

    transmission_counts = (
        filtered_df["transmission"]
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    fig.patch.set_facecolor("#1E1E1E")
    ax.set_facecolor("#1E1E1E")

    transmission_counts.plot(
        kind="bar",
        color="#FF5722",
        ax=ax
    )

    ax.set_xlabel("Transmission", color="#E0E0E0")
    ax.set_ylabel("Count", color="#E0E0E0")

    ax.tick_params(colors="#B0B0B0")

    for spine in ax.spines.values():
        spine.set_color("#333333")

    st.pyplot(fig)


with col2:

    st.subheader("👤 Owner Distribution")

    owner_counts = filtered_df["owner"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 5))

    fig.patch.set_facecolor("#1E1E1E")
    ax.set_facecolor("#1E1E1E")

    owner_counts.plot(
        kind="bar",
        color="#FF8A65",
        ax=ax
    )

    ax.set_xlabel("Owner Type", color="#E0E0E0")
    ax.set_ylabel("Count", color="#E0E0E0")

    ax.tick_params(colors="#B0B0B0")

    for spine in ax.spines.values():
        spine.set_color("#333333")

    st.pyplot(fig)


# ==================================================
# Price vs Car Age
# ==================================================

st.subheader("📈 Selling Price vs Car Age")

plot_df = filtered_df.dropna(
    subset=["car_age", "selling_price", "transmission"]
)

fig, ax = plt.subplots(figsize=(12, 5))

fig.patch.set_facecolor("#1E1E1E")
ax.set_facecolor("#1E1E1E")

sns.scatterplot(
    data=plot_df,
    x="car_age",
    y="selling_price",
    hue="transmission",
    palette={
        "Manual": "#FF5722",
        "Automatic": "#FF8A65",
        "Unknown": "#B0B0B0"
    },
    alpha=0.7,
    ax=ax
)

ax.set_xlabel("Car Age", color="#E0E0E0")
ax.set_ylabel("Selling Price", color="#E0E0E0")

ax.tick_params(colors="#B0B0B0")

for spine in ax.spines.values():
    spine.set_color("#333333")

legend = ax.legend(
    facecolor="#1E1E1E",
    labelcolor="#F5F5F5"
)

st.pyplot(fig)


# ==================================================
# Data Preview
# ==================================================

st.subheader("📋 Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)