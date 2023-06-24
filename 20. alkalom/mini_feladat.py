"""
Javaslatok:

Megoldás menete:
create scriptek - ezek már megvannak


"""

import pandas as pd
from sqlalchemy import create_engine, text

file_path = r"C:\WORK\2023_aprilis_python\20. alkalom\employees.csv"
df = pd.read_csv(file_path)
final_data = df.to_dict(orient="records")

engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

insert_statetment = "ide kell az insert utasítás"

with engine.connect() as conn:
    conn.execute(text(insert_statetment))