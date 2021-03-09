import altair as alt
import numpy as np
import pandas as pd
insurance = pd.read_csv("/desktop/insurance.csv")
insurance.head()
(alt.
  Chart(insurance).
  mark_circle(size=40).
  encode(x='charges', y='bmi').
  properties(height=400, width=500))