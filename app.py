import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Aggregate sales by date
sales_by_date = (
    df.groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)