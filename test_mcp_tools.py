"""Test script to list MCP tools via HTTP"""
import httpx
import json

async def test_list_tools():
    """Query MCP server to list all available tools"""
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Step 1: Initialize session
        print("🔌 Initializing MCP session...")
        init_response = await client.post(
            "http://localhost:8000/mcp",
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "test-client",
                        "version": "1.0.0"
                    }
                }
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream"
            }
        )
        
        init_result = init_response.json()
        print(f"✅ Session initialized: {json.dumps(init_result, indent=2)}\n")
        
        # Extract session ID from headers
        session_id = init_response.headers.get("x-session-id", "")
        
        # Step 2: Send initialized notification
        await client.post(
            "http://localhost:8000/mcp",
            json={
                "jsonrpc": "2.0",
                "method": "notifications/initialized"
            },
            headers={
                "Content-Type": "application/json",
                "x-session-id": session_id
            }
        )
        
        # Step 3: Request tools list
        print("📋 Requesting tools list...")
        response = await client.post(
            "http://localhost:8000/mcp",
            json={
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {}
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json, text/event-stream",
                "x-session-id": session_id
            }
        )
        
        result = response.json()
        print("=" * 70)
        print("MCP Tools List Response:")
        print("=" * 70)
        print(json.dumps(result, indent=2))
        
        if "result" in result and "tools" in result["result"]:
            tools = result["result"]["tools"]
            print(f"\n✅ Found {len(tools)} tools:")
            print("=" * 70)
            for tool in tools:
                print(f"  📦 {tool['name']}")
                if 'description' in tool:
                    print(f"     {tool['description'][:100]}")
                print()
        else:
            print("\n❌ No tools found in response")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_list_tools())
