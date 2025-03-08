import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///movies.db', echo = True)

metadata = sqlalchemy.MetaData()
movies_table =  sqlalchemy.Table ("Movies", matadata)



# conn = engine.connect()
# result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))

# with engine.connect() as conn:
#   result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
#   for row in result:
#     print(row)
