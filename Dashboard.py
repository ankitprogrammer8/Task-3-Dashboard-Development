"""
CODTECH IT SOLUTIONS - Data Analytics Internship
Task 3: Dashboard Development
Author: Ankit Kumar Pradhan
Description: Interactive Sales Analytics Dashboard built with Plotly Dash
"""

import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Load Data ────────────────────────────────────────────────────────────────
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.strftime("%Y-%m")
df["Month_Name"] = df["Date"].dt.strftime("%b %Y")

# ── App Initialisation ────────────────────────────────────────────────────────
app = dash.Dash(__name__, title="Sales Analytics Dashboard")

# ── Colour Palette ────────────────────────────────────────────────────────────
COLORS = {
    "bg": "#F8F9FA",
    "card": "#FFFFFF",
    "primary": "#2C3E7A",
    "accent": "#E84040",
    "success": "#27AE60",
    "warning": "#F39C12",
    "text": "#2D2D2D",
    "muted": "#7F8C8D",
}

CARD_STYLE = {
    "background": COLORS["card"],
    "borderRadius": "12px",
    "padding": "20px",
    "boxShadow": "0 2px 12px rgba(0,0,0,0.07)",
    "marginBottom": "20px",
}

# ── Layout ────────────────────────────────────────────────────────────────────
app.layout = html.Div(
    style={"background": COLORS["bg"], "minHeight": "100vh", "fontFamily": "Segoe UI, Arial, sans-serif", "padding": "0"},
    children=[

        # Header
        html.Div(
            style={"background": COLORS["primary"], "padding": "18px 32px", "display": "flex",
                   "alignItems": "center", "justifyContent": "space-between"},
            children=[
                html.Div([
                    html.H1("📊 Sales Analytics Dashboard",
                            style={"color": "#fff", "margin": 0, "fontSize": "22px", "fontWeight": "700"}),
                    html.P("CODTECH IT Solutions — Data Analytics Internship | Task 3",
                           style={"color": "#A8B8E8", "margin": "2px 0 0", "fontSize": "13px"}),
                ]),
                html.Div("2024 Annual Report", style={"color": "#A8B8E8", "fontSize": "14px"}),
            ],
        ),

        # Filters Row
        html.Div(
            style={"padding": "18px 32px 0", "display": "flex", "gap": "20px", "flexWrap": "wrap"},
            children=[
                html.Div([
                    html.Label("Category", style={"fontSize": "12px", "color": COLORS["muted"], "fontWeight": "600"}),
                    dcc.Dropdown(
                        id="filter-category",
                        options=[{"label": "All Categories", "value": "All"}] +
                                [{"label": c, "value": c} for c in sorted(df["Category"].unique())],
                        value="All",
                        clearable=False,
                        style={"width": "200px", "fontSize": "14px"},
                    ),
                ]),
                html.Div([
                    html.Label("Region", style={"fontSize": "12px", "color": COLORS["muted"], "fontWeight": "600"}),
                    dcc.Dropdown(
                        id="filter-region",
                        options=[{"label": "All Regions", "value": "All"}] +
                                [{"label": r, "value": r} for r in sorted(df["Region"].unique())],
                        value="All",
                        clearable=False,
                        style={"width": "180px", "fontSize": "14px"},
                    ),
                ]),
            ],
        ),

        # KPI Cards
        html.Div(
            id="kpi-row",
            style={"display": "flex", "gap": "16px", "padding": "18px 32px", "flexWrap": "wrap"},
        ),

        # Charts Row 1
        html.Div(
            style={"display": "flex", "gap": "20px", "padding": "0 32px", "flexWrap": "wrap"},
            children=[
                html.Div(dcc.Graph(id="chart-monthly-sales"), style={**CARD_STYLE, "flex": "2", "minWidth": "340px"}),
                html.Div(dcc.Graph(id="chart-category-pie"), style={**CARD_STYLE, "flex": "1", "minWidth": "280px"}),
            ],
        ),

        # Charts Row 2
        html.Div(
            style={"display": "flex", "gap": "20px", "padding": "0 32px", "flexWrap": "wrap"},
            children=[
                html.Div(dcc.Graph(id="chart-region-bar"), style={**CARD_STYLE, "flex": "1", "minWidth": "280px"}),
                html.Div(dcc.Graph(id="chart-profit-scatter"), style={**CARD_STYLE, "flex": "2", "minWidth": "340px"}),
            ],
        ),

        # Sub-category Bar
        html.Div(
            style={"padding": "0 32px 32px"},
            children=[html.Div(dcc.Graph(id="chart-subcategory"), style=CARD_STYLE)],
        ),

        # Footer
        html.Div(
            "Built with Plotly Dash · CODTECH IT Solutions Data Analytics Internship Task 3",
            style={"textAlign": "center", "padding": "12px", "fontSize": "12px", "color": COLORS["muted"]},
        ),
    ],
)


# ── Helper: filter dataframe ──────────────────────────────────────────────────
def filter_df(category, region):
    filtered = df.copy()
    if category != "All":
        filtered = filtered[filtered["Category"] == category]
    if region != "All":
        filtered = filtered[filtered["Region"] == region]
    return filtered


# ── Callbacks ─────────────────────────────────────────────────────────────────

@app.callback(
    Output("kpi-row", "children"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def update_kpis(category, region):
    d = filter_df(category, region)
    metrics = [
        ("💰 Total Sales", f"${d['Sales'].sum():,.0f}", COLORS["primary"]),
        ("📦 Total Orders", f"{len(d):,}", COLORS["accent"]),
        ("📈 Total Profit", f"${d['Profit'].sum():,.0f}", COLORS["success"]),
        ("🔢 Avg Order Value", f"${d['Sales'].mean():,.0f}", COLORS["warning"]),
    ]
    cards = []
    for title, value, color in metrics:
        cards.append(
            html.Div(
                style={**CARD_STYLE, "flex": "1", "minWidth": "150px", "borderTop": f"4px solid {color}", "marginBottom": "0"},
                children=[
                    html.P(title, style={"fontSize": "12px", "color": COLORS["muted"], "margin": "0 0 6px", "fontWeight": "600"}),
                    html.H2(value, style={"fontSize": "26px", "fontWeight": "800", "color": color, "margin": 0}),
                ],
            )
        )
    return cards


@app.callback(
    Output("chart-monthly-sales", "figure"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def monthly_sales(category, region):
    d = filter_df(category, region).groupby("Month")[["Sales", "Profit"]].sum().reset_index()
    fig = go.Figure()
    fig.add_trace(go.Bar(x=d["Month"], y=d["Sales"], name="Sales", marker_color=COLORS["primary"]))
    fig.add_trace(go.Scatter(x=d["Month"], y=d["Profit"], name="Profit", mode="lines+markers",
                             line=dict(color=COLORS["success"], width=2.5), marker=dict(size=6)))
    fig.update_layout(title="Monthly Sales & Profit Trend", plot_bgcolor="white", paper_bgcolor="white",
                      legend=dict(orientation="h", y=1.1), margin=dict(t=50, b=30, l=20, r=20),
                      xaxis=dict(tickangle=-45), hovermode="x unified")
    return fig


@app.callback(
    Output("chart-category-pie", "figure"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def category_pie(category, region):
    d = filter_df(category, region).groupby("Category")["Sales"].sum().reset_index()
    fig = px.pie(d, names="Category", values="Sales", hole=0.45,
                 color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(title="Sales by Category", paper_bgcolor="white",
                      margin=dict(t=50, b=10, l=10, r=10))
    fig.update_traces(textposition="outside", textinfo="percent+label")
    return fig


@app.callback(
    Output("chart-region-bar", "figure"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def region_bar(category, region):
    d = filter_df(category, region).groupby("Region")[["Sales", "Profit"]].sum().reset_index()
    fig = px.bar(d, x="Region", y=["Sales", "Profit"], barmode="group",
                 color_discrete_map={"Sales": COLORS["primary"], "Profit": COLORS["success"]})
    fig.update_layout(title="Sales & Profit by Region", plot_bgcolor="white", paper_bgcolor="white",
                      legend=dict(orientation="h", y=1.1), margin=dict(t=50, b=20, l=20, r=20))
    return fig


@app.callback(
    Output("chart-profit-scatter", "figure"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def profit_scatter(category, region):
    d = filter_df(category, region)
    fig = px.scatter(d, x="Sales", y="Profit", color="Category", size="Quantity",
                     hover_data=["Product", "Region", "Discount"],
                     color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(title="Sales vs Profit (bubble = Quantity)", plot_bgcolor="white",
                      paper_bgcolor="white", margin=dict(t=50, b=20, l=20, r=20))
    return fig


@app.callback(
    Output("chart-subcategory", "figure"),
    Input("filter-category", "value"),
    Input("filter-region", "value"),
)
def subcategory_bar(category, region):
    d = filter_df(category, region).groupby("Sub-Category")["Sales"].sum().reset_index().sort_values("Sales", ascending=True)
    fig = px.bar(d, x="Sales", y="Sub-Category", orientation="h",
                 color="Sales", color_continuous_scale="Blues")
    fig.update_layout(title="Sales by Sub-Category", plot_bgcolor="white", paper_bgcolor="white",
                      margin=dict(t=50, b=20, l=20, r=20), coloraxis_showscale=False)
    return fig


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
