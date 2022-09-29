import pandas as pd
import pyperclip

df = pd.read_csv('data.csv')

codes = df["code"].to_list()

sql_set = "(" + ", ".join(codes) + ")"

print(sql_set)



pyperclip.copy(sql_set)
spam = pyperclip.paste()