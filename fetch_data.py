from pymongo import MongoClient

def extract_data_from_mongo(connection_string, database_name, collection_name, query=None, projection=None):
    """
    Extract data from a MongoDB collection.
    
    :param connection_string: MongoDB connection string
    :param database_name: Name of the database
    :param collection_name: Name of the collection
    :param query: Optional query to filter the results
    :param projection: Optional projection to specify which fields to include or exclude
    :return: List of documents
    """
    # Connect to MongoDB
    client = MongoClient(connection_string)
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Perform the query
    if query is None:
        query = {}
    if projection is None:
        cursor = collection.find(query)
    else:
        cursor = collection.find(query, projection)
    
    # Convert cursor to list of documents
    documents = list(cursor)
    
    # Close the connection
    client.close()
    
    return documents

# Example usage:
connection_string = "mongodb+srv://sanchitbhalla15:nosoysauce123@dev-10.ycmrtf8.mongodb.net/auth?retryWrites=true&w=majority&appName=dev-10"
database_name = "auth"
collection_name = "resources"
# query = {"status": "active"}
# projection = {"_id": 0, "name": 1, "email": 1}

result = extract_data_from_mongo(connection_string, database_name, collection_name)
for doc in result:
    print(doc)