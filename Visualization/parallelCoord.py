#!/usr/bin/env python3

import plotly.graph_objects as go
import pandas as pd

_dataset = '../dataset/athlete_events.csv'

def main():
    df = pd.read_csv(_dataset)
    fig = go.Figure(data=
        go.Parcoords(
            line = dict(color = df['Year'],
                    colorscale = 'Electric',
                    showscale = True,
                    cmin = 1900,
                    cmax = 2020),
            dimensions = list([
                dict(label = 'Medal', values = df['Medal'])
                dict(label = "Country", values = df['Team']),
                dict(label = 'Sport', values = df['Sport']),
                dict(label = 'Year', values = df['Year']),
            ])
        )
    )
    fig.show()


if __name__ == "__main__":
    main()