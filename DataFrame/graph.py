import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
from PIL import Image


pivot_table = pd.read_excel('sales_pivot_table.xlsx', sheet_name='Pivot Table', index_col=0)


pivot_table = pivot_table.drop(index="Total", errors='ignore')


top_categories = pivot_table.sum(axis=1).nlargest(3).index


top_data = pivot_table.loc[top_categories]

# Побудова графіка
plt.figure(figsize=(10, 6))
for category in top_data.index:
    plt.plot(top_data.columns, top_data.loc[category], marker='o', label=category)


plt.title("Тренд продажів по місяцях для топ-3 категорій", fontsize=14)
plt.xlabel("Місяці", fontsize=12)
plt.ylabel("Сума продажів", fontsize=12)
plt.legend(title="Категорії", fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)


output_file = 'sales_trends_chart.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    pivot_table.to_excel(writer, sheet_name='Pivot Table')
    wb = writer.book
    chart_sheet = wb.create_sheet(title="Sales Trends Chart")

    # Збереження графіка на окремий лист Excel
    fig = plt.gcf()
    imgdata = BytesIO()
    fig.savefig(imgdata, format="png")
    imgdata.seek(0)    
    img = Image.open(imgdata)
    img.save('sales_trends_chart.png')

output_file
