import pandas as pd

df = pd.read_excel(
    r"C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Python Testing\Cotton.xlsx")

df.to_csv(r'C:\Users\WKYTUK0\OneDrive-Deere&Co\OneDrive - Deere & Co\Documents\EDP Rotation 1\Excel Documents\Python Testing\Cotton2.csv',
          index = False)

'''This also works (just flip direction of slashes) the 'r' converts a normal string to a raw string which is what we want'''

# df = pd.read_excel(
#    "C:/Users/WKYTUK0/OneDrive-Deere&Co/OneDrive - Deere & Co/Documents/EDP Rotation 1/Excel Documents/Python Testing/Cotton.xlsx")