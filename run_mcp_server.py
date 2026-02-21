"""MCP server with multiple OpenAPI specs using FastMCP"""
import json
from pathlib import Path
import httpx
import asyncio
from fastmcp import FastMCP

async def run_servers():
    """Run multiple MCP servers on different ports"""
    
    # ==================== JSONPlaceholder API (Port 8000) ====================
    spec_path_1 = Path(__file__).parent / "jsonplaceholder-openapi.json"
    with open(spec_path_1) as f:
        jsonplaceholder_spec = json.load(f)

    client_1 = httpx.AsyncClient(
        base_url="https://jsonplaceholder.typicode.com",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )

    mcp_1 = FastMCP.from_openapi(
        openapi_spec=jsonplaceholder_spec,
        client=client_1,
        name="JSONPlaceholder"
    )

    # ==================== AuthorizeAssets API (Port 8001) ====================
    spec_path_2 = Path(__file__).parent / "authorizeassets.json"
    with open(spec_path_2) as f:
        authorizeassets_spec = json.load(f)

    client_2 = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/FA/ACAP_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )

    mcp_2 = FastMCP.from_openapi(
        openapi_spec=authorizeassets_spec,
        client=client_2,
        name="AuthorizeAssets"
    )

    # ==================== ViewPurchaseRequest API (Port 8002) ====================
    spec_path_3 = Path(__file__).parent / "viewpurchaserequest.json"
    with open(spec_path_3) as f:
        viewpurchaserequest_spec = json.load(f)

    client_3 = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/Pur_Req_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
    )

    mcp_3 = FastMCP.from_openapi(
        openapi_spec=viewpurchaserequest_spec,
        client=client_3,
        name="ViewPurchaseRequest"
    )

    print("Starting Multiple MCP Servers...")
    print("=" * 60)
    print("📡 JSONPlaceholder API:        http://localhost:8000/mcp")
    print("📡 AuthorizeAssets API:        http://localhost:8001/mcp")
    print("📡 ViewPurchaseRequest API:    http://localhost:8002/mcp")
    print("=" * 60)
    print("\nServers are running. Press Ctrl+C to stop.")
    
    # Run all servers concurrently
    await asyncio.gather(
        mcp_1.run_async(transport="http", host="localhost", port=8000),
        mcp_2.run_async(transport="http", host="localhost", port=8001),
        mcp_3.run_async(transport="http", host="localhost", port=8002),
    )

if __name__ == "__main__":
    asyncio.run(run_servers())
