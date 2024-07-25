# python

# test.csv

# sắp xếp lại theo cột đầu tiên

# pip install pandas
import pandas as pd

# Đọc file CSV
df = pd.read_csv('test.csv')

# Sắp xếp theo cột đầu tiên
df_sorted = df.sort_values(by=df.columns[0])

# Lưu lại file CSV đã sắp xếp
df_sorted.to_csv('test_sorted.csv', index=False)

print("File CSV đã được sắp xếp và lưu thành 'test_sorted.csv'")
