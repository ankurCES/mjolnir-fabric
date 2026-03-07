from qdrant_client import QdrantClient
import os

class MjolnirFabric:
    def __init__(self):
        self.host = os.getenv("QDRANT_HOST", "localhost")
        self.port = int(os.getenv("QDRANT_PORT", 6333))
        self.client = QdrantClient(host=self.host, port=self.port)

    def heartbeat(self):
        return self.client.get_collections()

if __name__ == "__main__":
    fabric = MjolnirFabric()
    print("Mjolnir-Fabric initialized. Checking Qdrant connection...")
    try:
        collections = fabric.heartbeat()
        print(f"Connected. Collections: {collections}")
    except Exception as e:
        print(f"Connection failed: {e}")
