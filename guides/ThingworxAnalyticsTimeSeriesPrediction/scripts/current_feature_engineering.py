import pandas as pd

# df => pandas DataFrame
# open csv
print("Loading csv file")
df_csv = pd.read_csv(r"ThingworxAnalyticsTimeSeriesDataset.csv")
df_csv['AVG'] = ''

df_new = pd.DataFrame(columns=df_csv.columns)

# print(len(df_csv.index))
numOfEntries = 0
total = 0  # sum is a function
count = 0

print("Start processing loop")
for i in range(len(df_csv.index)):  # special case for last cycle
    if df_csv.loc[i, 'smartServo1Current'] == 0:  # if current is 0 ignore it for averages
        pass
    elif df_csv.loc[
        i - 1, 'smartServo1Current'] == 0:  # if current before was 0 ignore it for averages, bcs of spike at the start
        pass
    else:
        total += df_csv.loc[i, 'smartServo1Current']  # sum the current values
        count += 1  # increment the count for calculating the averarge current value


    if i >= len(df_csv.index) - 2 and i < len(df_csv.index) - 1:
        pass
    elif i == len(df_csv.index) - 1:
        avg = total / count
        df_new.loc[numOfEntries] = df_csv.loc[i]
        df_new.loc[numOfEntries, 'AVG'] = avg
    elif df_csv.loc[i + 1, 'smartServo1Current'] == 0 and df_csv.loc[i + 2, 'smartServo1Current'] != 0:
        avg = total / count
        total = 0
        count = 0
        df_new.loc[numOfEntries] = df_csv.loc[i]
        df_new.loc[numOfEntries, 'AVG'] = avg
        numOfEntries += 1

print("Write to averages.csv")
# writing into the file
df_new.to_csv("averages.csv", index=False)

# print(df_new)
