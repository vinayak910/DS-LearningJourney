import mysql.connector
class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                port=3309,
                user='root',
                password='root',
                database='flights')
            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except Exception as E:
            print("Connection Error")
            print(E)

    def fetch_city_names(self):
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flights
        UNION 
        SELECT DISTINCT(source) FROM flights
        """)
        data = self.mycursor.fetchall()
        print(data)
        city = []
        for i in data:
            city.append(i[0])
        return city

    def fetch_all_flights(self , source , destination):
        self.mycursor.execute("""
        SELECT * FROM flights
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source , destination))
        data = self.mycursor.fetchall()
        return data

    def fetch_airline_info(self):
        self.mycursor.execute("""
        SELECT Airline , COUNT(*) FROM flights
        GROUP BY Airline
        """)
        data = self.mycursor.fetchall()
        airline = []
        frequency = []
        for i in data :
            airline.append(i[0])
            frequency.append(i[1])
        return airline , frequency