import pandas as pd
import plotly.graph_objects as go
import plotly
import json

def prepare_figures():

    #load data
    df_charging_points = pd.read_csv("../data/Ladesaeulenregister.csv", sep=";", low_memory=False)
    df_surface = pd.read_csv("../data/Gebietsfläche.csv",sep=";", low_memory=False)
    
    figures = []

    ###################prepare plot charging points per bundesland###################
    grouped_cnt = df_charging_points.groupby(["Bundesland", "Art der Ladeeinrichung"], as_index=False)["Betreiber"].count()
    grouped_cnt.sort_values(by = ["Bundesland","Art der Ladeeinrichung"], ascending=True, inplace = True)
    
    fig_land_cnt = go.Figure()

    for art in grouped_cnt["Art der Ladeeinrichung"].unique():

        fig_land_cnt.add_trace(
            go.Bar(
                y = grouped_cnt[grouped_cnt["Art der Ladeeinrichung"] == art]["Bundesland"],
                x = grouped_cnt[grouped_cnt["Art der Ladeeinrichung"] == art]["Betreiber"],
                name = art,
                orientation="h"
            )
        )
    
    fig_land_cnt.update_layout(
        barmode="stack",
        autosize=False,
        width=800,
        height=600,
        title="Count of Charging points per Bundesland (regional department)",
        legend=dict(
                orientation='h',  
                yanchor='top',    
                y=-0.2)
    )

    figures.append(dict(data=fig_land_cnt.data, layout=fig_land_cnt.layout))

    ###################prepare plot charging points per bundesland###################
    df_surface["Flaeche_qm"] = df_surface["Flaeche_qm"].apply(lambda x: x.replace(",", ".").replace(" ", ""))
    df_surface["Flaeche_qm"] = df_surface["Flaeche_qm"].astype("float")

    grouped_cnt = pd.merge(left = grouped_cnt, right = df_surface, left_on = "Bundesland", right_on = "Bundesland", how = "left")
    grouped_cnt["cnt_per_qm"] = grouped_cnt["Betreiber"]/grouped_cnt["Flaeche_qm"]

    fig_land_cnt_per_qm = go.Figure()

    for art in grouped_cnt["Art der Ladeeinrichung"].unique():

        fig_land_cnt_per_qm.add_trace(
            go.Bar(
                y = grouped_cnt[grouped_cnt["Art der Ladeeinrichung"] == art]["Bundesland"],
                x = grouped_cnt[grouped_cnt["Art der Ladeeinrichung"] == art]["cnt_per_qm"],
                name = art,
                orientation="h"
            )
        )

    fig_land_cnt_per_qm.update_layout(
        barmode="stack",
        autosize=False,
        width=800, 
        height=600,
        title="Count of Charging points per km² per Bundesland (regional department)",
        legend=dict(
                orientation='h',  
                yanchor='top',    
                y=-0.2)
    )


    figures.append(dict(data=fig_land_cnt_per_qm.data, layout=fig_land_cnt_per_qm.layout))

    ###################prepare plot charging points per city###################
    grouped_city_top_cnt = df_charging_points.groupby("Kreis/kreisfreie Stadt")["Betreiber"].count().sort_values(ascending=False).head()

    df_charging_points["Inbetriebnahmedatum"] = pd.to_datetime(df_charging_points["Inbetriebnahmedatum"], format="%d.%m.%Y")
    df_charging_points["Inbetriebnahmedatum_month"] = df_charging_points["Inbetriebnahmedatum"] + pd.offsets.YearBegin(-1)
    df_charging_points_timeline = df_charging_points.groupby(["Kreis/kreisfreie Stadt", "Inbetriebnahmedatum_month"], as_index = False)["Betreiber"].count().rename({"Betreiber": "cnt"}, axis = 1)
    df_charging_points_timeline_top5 = df_charging_points_timeline[df_charging_points_timeline["Kreis/kreisfreie Stadt"].isin(grouped_city_top_cnt.index.tolist())]
    df_charging_points_timeline_top5 = df_charging_points_timeline_top5[df_charging_points_timeline_top5["Inbetriebnahmedatum_month"].dt.year<2024]

    fig_city_cnt = go.Figure()

    for stadt in df_charging_points_timeline_top5["Kreis/kreisfreie Stadt"].unique():

        df_curr = df_charging_points_timeline_top5[df_charging_points_timeline_top5["Kreis/kreisfreie Stadt"] == stadt]

        fig_city_cnt.add_trace(
                go.Scatter(
                    x = df_curr["Inbetriebnahmedatum_month"],
                    y = df_curr["cnt"],
                    name = stadt.split(" ")[-1],
                    mode="lines+markers+text"
                )
            )

    fig_city_cnt.update_layout(
        autosize=False,
        width=1700, 
        height=500,
        title="Top 5 most advanced cities concerning charging stations",
        legend=dict(
                orientation='h',  
                yanchor='top',    
                y=-0.2)
    )

    figures.append(dict(data=fig_city_cnt.data, layout=fig_city_cnt.layout))

    ###################prepare plot charging points per betreiber###################
    grouped_betreiber_top_cnt = df_charging_points.groupby("Betreiber")["Ort"].count().sort_values(ascending=False).head(10)
    betreiber_timeline = df_charging_points.groupby(["Betreiber", "Inbetriebnahmedatum_month"], as_index = False)["Ort"].count().rename({"Ort": "cnt"}, axis = 1)
    betreiber_timeline_top10 = betreiber_timeline[betreiber_timeline["Betreiber"].isin(grouped_betreiber_top_cnt.index.tolist())]
    betreiber_timeline_top10 = betreiber_timeline_top10[betreiber_timeline_top10["Inbetriebnahmedatum_month"].dt.year<2024]

    fig_betreiber_cnt = go.Figure()

    for betreiber in betreiber_timeline_top10["Betreiber"].unique():

        df_curr = betreiber_timeline_top10[betreiber_timeline_top10["Betreiber"] == betreiber]

        fig_betreiber_cnt.add_trace(
                go.Scatter(
                    x = df_curr["Inbetriebnahmedatum_month"],
                    y = df_curr["cnt"],
                    name = betreiber,
                    mode="lines+markers+text"
                )
            )

    fig_betreiber_cnt.update_layout(
        autosize=False,
        width=1700, 
        height=500,
        title="Top 10 most advanced Betreiber (resp. company) concerning charging stations",
        legend=dict(
                orientation='h',  
                yanchor='top',    
                y=-0.2)
    )

    figures.append(dict(data=fig_betreiber_cnt.data, layout=fig_betreiber_cnt.layout))


    return figures