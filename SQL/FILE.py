import sqlite3

 
X = sqlite3.connect('SalesDB.db')
 
Y = X.cursor()

 
Y.execute("SELECT * FROM Supermarket_sales ")

print(Y.fetchall())

        
X.commit()

Y.close()