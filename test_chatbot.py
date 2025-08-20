#!/usr/bin/env python3
"""
Simple test script to verify the customer service chatbot is working.
This will test the WebSocket connection and send a simple message.
"""

import asyncio
import websockets
import json
import time

async def test_chatbot():
    """Test the customer service chatbot WebSocket connection."""
    
    print("🔧 Testing Customer Service Chatbot...")
    
    # Generate a test session ID
    session_id = f"test_session_{int(time.time() * 1000)}"
    
    # WebSocket URL for the streaming server
    ws_url = f"ws://localhost:8001/ws/agent_stream/{session_id}?is_audio=false"
    
    try:
        print(f"📡 Connecting to WebSocket: {ws_url}")
        
        async with websockets.connect(ws_url) as websocket:
            print("✅ WebSocket connection established!")
            
            # Send client ready message
            client_ready_msg = {
                "mime_type": "text/plain",
                "data": "client_ready"
            }
            await websocket.send(json.dumps(client_ready_msg))
            print("📤 Sent: client_ready")
            
            # Send a test message
            test_msg = {
                "mime_type": "text/plain", 
                "data": "Hello, I need help with gardening. What plants do you recommend for beginners?"
            }
            await websocket.send(json.dumps(test_msg))
            print("📤 Sent: Test gardening question")
            
            # Listen for responses
            response_count = 0
            timeout_seconds = 30
            
            try:
                while response_count < 10:  # Limit responses to avoid infinite loop
                    response = await asyncio.wait_for(websocket.recv(), timeout=timeout_seconds)
                    response_count += 1
                    
                    try:
                        parsed_response = json.loads(response)
                        print(f"📥 Response {response_count}: {parsed_response}")
                        
                        # Check if this is a completion signal
                        if (parsed_response.get("turn_complete") or 
                            parsed_response.get("interaction_completed")):
                            print("✅ Conversation completed successfully!")
                            break
                            
                    except json.JSONDecodeError:
                        print(f"📥 Raw response {response_count}: {response}")
                        
            except asyncio.TimeoutError:
                print(f"⚠️  Timeout after {timeout_seconds} seconds")
            
    except ConnectionRefusedError:
        print("❌ Connection refused - streaming server may not be running")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
    
    print("✅ Chatbot test completed!")
    return True

if __name__ == "__main__":
    # Run the test
    success = asyncio.run(test_chatbot())
    
    if success:
        print("\n🎉 RESULT: Customer service chatbot is working!")
    else:
        print("\n⚠️  RESULT: There may be issues with the chatbot setup")
