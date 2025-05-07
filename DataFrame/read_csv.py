import pandas as pd

data = pd.read_csv("sales_data.csv")
 

data["total_amount"] = data["quantity"] * data["price"]


data["month"] = pd.to_datetime(data["date"]).dt.to_period("M")
# print(data)

grouped_data = data.groupby(['month', 'category']).agg(total_sales=('total_amount', 'sum')).reset_index()
# print(grouped_data)

grouped_data['rank'] = grouped_data.groupby('month')['total_sales'].rank(method='dense', ascending=False)
top_categories = grouped_data[grouped_data['rank'] <= 3].sort_values(by=['month', 'rank'])

result = top_categories[['month', 'category', 'total_sales', 'rank']]
result.head()
print(result)

res = pd.DataFrame(result)
res.to_csv("sales_data1.csv", index= False)