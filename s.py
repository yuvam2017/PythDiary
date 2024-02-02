from pymongo import MongoClient

class Mongobhai :
    def __init__(self):
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        self.CONNECTION_STRING = "mongodb+srv://admin_diary:Xoromate324@cluster0.tytbfze.mongodb.net/?retryWrites=true&w=majority"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        self.client = MongoClient(self.CONNECTION_STRING)

        try:
            self.client.admin.command('ping')
            print("Database Live",end='\r')
        except Exception as e:
            print(e)

    def get_database(self,db):
        return self.client[db]
    
    def write(self,db_name,coll_name,data):
        db = self.get_database(db)
        print(db)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__": 
    aps = Mongobhai()  
    
    dbname = aps.get_database('s')
    print(dbname)
   