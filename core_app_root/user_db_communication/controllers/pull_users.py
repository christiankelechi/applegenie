from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb+srv://devapplematch:APPLEmatch24!@test-cluster.shwxefk.mongodb.net/?retryWrites=true&w=majority&appName=test-cluster")  # Replace with your MongoDB URI

# Select the database
db = client['applematch']  # Replace with your database name

# Select the collection
collection = db['users']  # Replace with your collection name

def fetch_all_users():
    """
    Fetches all users from the MongoDB collection.
    
    Returns:
        list: A list of dictionaries, each representing a user.
    """
    try:
        users = list(collection.find())
        return users
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def fetch_user(user_id):
 
    try:
        user = collection.find_one({"id": user_id})
        return user
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
all_users = fetch_all_users()
print(all_users)

# single_user = fetch_user("some_user_id")
# print(single_user)