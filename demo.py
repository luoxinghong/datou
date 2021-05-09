import re
import pandas as pd


tail_dot_rgx = re.compile(r'(?:(\.)|(\.\d*?[1-9]\d*?))0+(?=\b|[^0-9])')
def remove_tail_dot_zeros(a):
    return tail_dot_rgx.sub(r'\2',a)

df1 = pd.read_excel('/Users/lxh/Downloads/2.xls',sheet_name=1)
df2 = pd.read_excel('/Users/lxh/Downloads/2.xls',sheet_name=2)
columns =df1.columns.values.tolist()
order_date_map=dict(zip(df2['Order No'],df2['hello']))
for idx, row in df1.iterrows():
    d_row = {}
    for column in columns:
        if pd.isnull(row["Invoice Date"]):
            row['Invoice Date'] = order_date_map[row["Order No"]].strftime('%Y-%m-%d')
            df1.loc[idx] = row



for index,i in enumerate(df1['Subtotal']):
    df1['Subtotal'][index] = remove_tail_dot_zeros(str(i))

df1.to_excel('666.xlsx', sheet_name='Sheet1', index=False, header=True)
