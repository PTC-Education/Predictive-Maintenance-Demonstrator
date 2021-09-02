import pandas as pd

# df => pandas DataFrame
# open csv
print("Loading csv file")
df_csv = pd.read_csv(r"ThingworxAnalyticsTimeSeriesDataset.csv")
df_csv['RUL'] = ''


numOfEntries = 0
total = 0  
cycle = 0
newCycle = True


print("Start processing loop")
for i in range(len(df_csv.index)):  # special case for last cycle
    if df_csv.loc[i, 'isDrawing'] and newCycle :  # if current is 0 ignore it for averages
        total += 1
        cycle = df_csv.loc[i, 'cycle']
        newCycle = False
    if i < len(df_csv.index) - 1 and cycle != df_csv.loc[i+1, 'cycle']:
        newCycle = True

cycle = 0
total -= 1  # last cycle is split with "isDrawing" True / False
for i in range(len(df_csv.index)):
    df_csv.loc[i, 'RUL'] = total
    if i < len(df_csv.index) - 1 and cycle != df_csv.loc[i+1, 'cycle']:
        cycle += 1
        if total > 0:
            total -= 1


print("Write to file")
df_csv.to_csv(r"output_RUL.csv", index=False)

# print(df_new)
