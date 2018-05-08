import pandas as pd
import numpy as np

#df = pd.read_csv('E:\Google Drive\Source Code\Python\quosaexport.csv')

# Use the height and width to calculate the area
def calculate_area(row):
    return row['height'] * row['width']

df=pd.DataFrame([
    { 'Author': 'Auth AA', 'Title': 'My Title AA' },
    { 'Author': 'Auth BB', 'Title': 'My Title BB' },
])
    
df_subset=df[['Author','Title']]

# append empty column
df["D"] = np.nan
df=df.assign(E="",F=np.nan)
 
for i in df.index:
    if df.at[i,'Author']=='Auth AA':
        df.at[i, 'ifor'] = 'x'
    else:
        df.at[i, 'ifor'] = 'y'
