import pymysql as database

conn = database.connect(
  host="localhost",
  user="root",
  password="",
  database="db_pegawai"
)
print(conn,"sukses")

mycursor = conn.cursor()

# menampilkan data pegawai
mycursor.execute("SELECT * FROM pegawai")
data = mycursor.fetchall()
print(data)
