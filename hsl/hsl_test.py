import pandas as pd
from collections import defaultdict
from PIL import Image
import requests
import colorgram
import colorsys

#get HSL data for each century
def categorize_hsl(rgb):
    r, g, b = rgb

    h, s, l = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    h_segment = int(h * 360 / 60)
    s_segment = int(s * 100 / 20)  
    l_segment = int(l * 100 / 20)
    return h_segment, s_segment, l_segment

def process_csv(csv_file, century):
    df = pd.read_csv(csv_file)
    hsl_counts = defaultdict(int)
    total_pixels = 0

    for index, row in df.iterrows():
        image_url = row["Image URL"]
        image = Image.open(requests.get(image_url, stream=True).raw)
        colors = colorgram.extract(image, 5) 
        for color in colors:
            rgb = color.rgb
            hsl_segments = categorize_hsl(rgb)
            hsl_counts[hsl_segments] += 1
            total_pixels += 1


    hsl_percentages = {segment: (count / total_pixels) * 100 for segment, count in hsl_counts.items()}
    return {century: hsl_percentages}

csv_files = ["15th_color2.csv", "16th_color2.csv", "17th_color2.csv", "18th_color2.csv", "19th_color2.csv", "20th_color2.csv"]
centuries = ["15th Century", "16th Century", "17th Century", "18th Century", "19th Century", "20th Century"]

hsl_compositions = defaultdict(dict)
for csv_file, century in zip(csv_files, centuries):
    hsl_composition = process_csv(csv_file, century)
    hsl_compositions.update(hsl_composition)

csv_data = []
for century, hsl_percentages in hsl_compositions.items():
    for hsl_segment, percentage in hsl_percentages.items():
        h, s, l = hsl_segment
        csv_data.append([century, h, s, l, percentage])

output_df = pd.DataFrame(csv_data, columns=["Century", "Hue Segment", "Saturation Segment", "Lightness Segment", "Percentage"])
output_df.to_csv("hsl_composition_by_century.csv", index=False)
