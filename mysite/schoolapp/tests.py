from django.test import TestCase

# Create your tests here. 
from autobahn.asyncio.wamp import connect
import asyncio

async def test_ws_server(uri):
    async def onopen(session):
        print("Successfully connected to WebSocket server!")
        await session.close()

    try:
        await connect(onopen, uri)
    except Exception as e:
        print(f"Error connecting: {e}")

# Replace with your actual server address and port
uri = "ws://localhost:9000/ws/your_path/"  # Replace with your path

asyncio.run(test_ws_server(uri))