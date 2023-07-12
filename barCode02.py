import mysql.connector as sqlc
from barcode import EAN13
from barcode.writer import ImageWriter
mydb= sqlc.connect(
    host='localhost',
    user='root',
    passwd='rashi123',
    database='pythondb'
)
mycursor= mydb.cursor()


mydb.commit()

mycursor.execute("select age from Employee")
myresult= [mycursor.fetchall()]
for x in myresult:
    for n in range(0, len(x)):
        my_code = EAN13(age[n], writer=ImageWriter())
        my_code.save(f"myBarCode_{n}.png")
        