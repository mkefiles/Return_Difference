'''
Creator: Mike
Description: Returns the different data-points between data-sets.
Example: This returns only results between 30 miles and 55 miles.
'''

# DESC: Import
import pandas as pd

# DESC: Read CSV into DataFrame
thirty_mile_df = pd.read_csv('30-mi-radius-FIXED.csv', dtype='str')
fifty_mile_df = pd.read_csv('55-mi-radius-FIXED.csv', dtype='str')

# DESC: Return DataFrame with Difference ONLY
above_thirty_mile_df = pd.concat([thirty_mile_df, fifty_mile_df]).drop_duplicates(keep=False)

# DESC: Output to CSV
above_thirty_mile_df.to_csv("beyond-30-mi.csv")

# DESC: Output Results
print("Task completed...")