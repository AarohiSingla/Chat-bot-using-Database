import sqlite3

def insert_data(travel_date, travel_period, trip_type, adults, child, budget, email, phno):
 conn = sqlite3.connect('demo.db') 
 cursor = conn.cursor()
 print("Database created and Successfully Connected to SQLite")
 
 # sql='''CREATE TABLE d2(
    # travel_date VARCHAR,
    # travel_period VARCHAR,
    # trip_type VARCHAR,
    # adults VARCHAR,
    # child VARCHAR,
    # budget VARCHAR,
    # email VARCHAR,
    # phno VARCHAR
  # )'''
 cursor.execute('''INSERT INTO d2(travel_date, travel_period, trip_type, adults, child, budget, email, phno) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (travel_date, travel_period, trip_type, adults, child, budget, email, phno))
   
	
 print("Table created successfully........")

 # Commit your changes in the database
 conn.commit()

 #Closing the connection
 conn.close()

 
#if __name__ == "__main__":
 #insert_data('12-10-2017',3, 'adventure', 2, 1, 6000, 'qwerty@gmail.com', 987654321)
 