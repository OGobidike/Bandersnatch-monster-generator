import plotly.express as px
from pandas import DataFrame
from plotly.graph_objects import Figure

# make sure you change output to figure if your using Plotly
def chart(df, x, y, target) -> Figure:
    """
    create an interactive chart with plotly.

    Params:
        df == (DataFrame): The dataset to visualize
        x == (str): The column for the x-axis
        y == (str): The column for the y-axis
        target == (str): The column for grouping (color coding)

    returnz:
        Figure: The plotly figure object
    """
    # now! a scatterplot for the dataset!
    fig = px.scatter(
        df,  # remember, this is the DataFrame that contains our data
        x = x,
        y = y,
        color = target,
        title = f"{y} by {x} for {target}",
        hover_data = df.columns,  # include all columns
    )

    fig.update_layout(
        plot_bgcolor = "#2c2f33", # this is the background for the dark theme CSS peeps know what it is
        paper_bgcolor = "#2c2f33", # this is the background for paper color
        font = dict(color = "white"),
        title = dict(
            font_size = 18,
            x = 0.05,  # align title to the left of screen
        ),
        margin = dict(l = 50, r = 50, t = 50, b = 50),  # adjust padding for chart spacing
    )

    # customization!! customize the  axes for better visibility...
    # (Bandersnatch web page is in some type of dark theme)
    # first we remove gridlines for clearer vizz, then we color the axis titles, and ticket labels
    fig.update_xaxes(showgrid = False, title_font = dict(color = "white"), tickfont = dict(color = "white"))
    fig.update_yaxes(showgrid = False, title_font = dict(color = "white"), tickfont = dict(color = "white"))

    fig.show()
    return fig

