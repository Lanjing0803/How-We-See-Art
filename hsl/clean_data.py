import pandas as pd

filename = 'hsl_composition_by_century.csv'
df = pd.read_csv(filename)

sorted_df = df.sort_values(by=['Century', 'Hue Segment', 'Saturation Segment','Lightness Segment'], ascending=[True, False, False,False])

sorted_df.to_csv(filename, index=False)
