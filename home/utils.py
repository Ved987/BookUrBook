from pymongo import MongoClient

def get_db_handle():
    client = MongoClient('mongodb+srv://vedan987:Vedanshu1502@cluster-books.jailwop.mongodb.net/?retryWrites=true&w=majority')
    db_handle = client['Books-Data']
    return db_handle, client


def get_collection_handle(db_handle,collection_name):
    return db_handle[collection_name]



