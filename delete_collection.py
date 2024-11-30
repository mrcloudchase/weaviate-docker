import weaviate

# Connect to local Weaviate instance running in Docker Compose
client = weaviate.connect_to_local()

try:    
    client.collections.delete("Question")
except Exception as e:
    print(f"Error deleting collection: {e}")

# Close the client
client.close()