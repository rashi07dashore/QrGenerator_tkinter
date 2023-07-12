import mysql.connector as sqlc
import qrcode
mydb= sqlc.connect(
    host='localhost',
    user='root',
    passwd='rashi123',
    database='pythondb'
)
mycursor= mydb.cursor()
mycursor.execute("select * from Employee")
myresult= [mycursor.fetchall()]

for x in myresult:
    for n in range(0, len(x)):
        img = qrcode.make(x[n])
        img.save(f'myQR_{n}.png')
        
        
    