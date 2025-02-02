'''
Creator: Mike
Description: Returns all accounts who were in the original data set and not the newest.
Example: If ABC Co. had Aflac (and is on the DNC list) then falls off... they are fair-game.
'''

# DESC: Import
import pandas as pd

# DESC: Read CSV into DataFrame
data_frame_original = pd.read_csv("01.04.csv", dtype="str")
data_frame_new = pd.read_csv("01.19.csv", dtype="str")

# DESC: Return DataFrame with Differences ONLY
data_frame_difference = pd.concat([data_frame_original, data_frame_new]).drop_duplicates(keep=False)

# DESC: Output DataFrame (to see unique values between dataframes)
print("========= DIFFERENCE LEADS =========")
print("==================")
print(data_frame_difference)

# DESC: Checks if unique-values are in the latest data-set (returns a Series with True or False)
data_frame_fresh_blood = data_frame_difference['name'].isin(data_frame_new['name'])

# DESC: Delete any value, in place, from DF where it is "True"
data_frame_difference.drop(data_frame_difference[data_frame_fresh_blood].index, inplace=True)

print("========= FAIR-GAME LEADS =========")
print("==================")

# DESC: Output all results
pd.set_option("display.max_rows", None)
print(data_frame_difference)

# DESC: Output to CSV
data_frame_difference.to_csv("output.csv", index=False)
