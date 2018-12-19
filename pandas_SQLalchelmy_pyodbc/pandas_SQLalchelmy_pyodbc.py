from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mssql+pyodbc://vminformdev01/GI_VS_SC_Test?driver=SQL+Server+Native+Client+11.0')

df = pd.read_sql_query('SELECT * FROM FOO', engine)

print(df)