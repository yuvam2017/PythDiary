from pymongo import MongoClient

class Database :
    def __init__(self):
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        self.CONNECTION_STRING = "mongodb+srv://admin:Xoromate324@cluster0.jvf8go4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        self.client = MongoClient(self.CONNECTION_STRING)

        try:
            self.client.admin.command('ping')
            print("Database Live",end='\r')
        except Exception as e:
            print(e)

    def get_database(self,db):
        return self.client[db]
    
    def write_one(self,db_name,coll_name,data):
        db = self.get_database(db_name)
        collection = db[coll_name]
        result = collection.insert_one(data)
        return result.acknowledged

    def write_many(self,db_name,coll_name,data):
        db = self.get_database(db_name)
        collection = db[coll_name]
        result = collection.insert_many(data)
        return result.acknowledged

    def user_exists(self,db_name,coll_name):
        db = self.get_database(db_name)
        collection = db[coll_name]
        result = collection.find_one({'_id':0})
        if result is not None:
            if result['_id'] == 0:
                return True
            else : 
                return False
        else : 
            return False

    def read(self,db_name,coll_name,data):
        db = self.get_database(db_name)
        collection = db[coll_name]
        result = collection.find_one({'_id':0})



    # def update(self,db_name,coll_name,query_match,)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__": 
    aps = Mongobhai()  
    
    write_status = aps.write('Hello','sad',{"age":21})
    print(write_status)   