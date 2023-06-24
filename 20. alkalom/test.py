import os
file_path = r"C:\WORK\2023_aprilis_python\20. alkalom\employees.csv"
with open(file_path, 'r', encoding="utf-8") as f:
    data = f.read().split('\n')
    data.pop()

cols = data.pop(0).split(',')
print(cols)
# print(data)

temp = []

for item in data:
    row = item.split(',')
    # print(row)
    m_dict = {}
    for idx,i in enumerate(cols):
        m_dict[i] = row[idx]
    temp.append(m_dict)

print(temp)