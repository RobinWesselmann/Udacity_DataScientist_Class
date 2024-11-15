import pandas as pd
import plotly.graph_objects as go
import plotly
import json

def prepare_figures(df):

    figures = []

    #distribution genres
    fig_genre_cnts = go.Figure()

    genre_counts = df.groupby('genre', as_index = False)['message'].count()

    fig_genre_cnts.add_trace(
            go.Bar(
                x = genre_counts["genre"],
                y = genre_counts["message"],
                name = "Distribution of genre"
            )
        )

    fig_genre_cnts.update_layout(
        barmode="group",
        autosize=False,
        width=600, 
        height=400,
        title="Distribution of genre"
    )
 
    figures.append(dict(data=fig_genre_cnts.data, layout=fig_genre_cnts.layout))

    #distribution genre / message category
    pvt = pd.pivot_table(
        data = df,
        values = df.columns[4:].tolist(),
        columns = "genre",
        aggfunc="sum"
    )

    fig_msg_cat_heatmap = go.Figure(data=go.Heatmap(
                    y = pvt.index,
                    x = pvt.columns,
                    z=pvt,
                    colorscale='Viridis',
                    xgap = 1,
                    ygap = 1,
                    text=pvt.values,
                    texttemplate="%{text}",
                    textfont={"size":10}
                    ))

    fig_msg_cat_heatmap.update_layout(
            autosize=True,
            width=600, 
            height=800,
            title="Distribution of genre dependant on message category",
            xaxis=dict(showgrid=True),
            yaxis=dict(showgrid=True)
        )

    figures.append(dict(data = fig_msg_cat_heatmap.data, layout = fig_msg_cat_heatmap.layout))


    return figures