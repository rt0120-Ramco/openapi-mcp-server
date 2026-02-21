"""Unified MCP server with multiple OpenAPI specs using FastMCP"""
import json
from pathlib import Path
import httpx
from fastmcp import FastMCP


def add_server(main_mcp: FastMCP, sub_mcp: FastMCP, prefix: str = ""):
    """
    Custom add_server functionality to merge tools from sub_mcp into main_mcp.
    
    Args:
        main_mcp: The main MCP server to add tools to
        sub_mcp: The sub MCP server whose tools will be extracted
        prefix: Optional prefix for tool names to avoid conflicts
    """
    # Access the internal tool manager
    if hasattr(sub_mcp, '_tool_manager') and sub_mcp._tool_manager:
        tool_manager = sub_mcp._tool_manager
        
        # Get all registered tools
        if hasattr(tool_manager, '_tools'):
            for tool_name, tool_func in tool_manager._tools.items():
                # Add prefix if provided
                new_tool_name = f"{prefix}_{tool_name}" if prefix else tool_name
                
                # Register tool in main MCP
                if hasattr(main_mcp, '_tool_manager') and main_mcp._tool_manager:
                    main_mcp._tool_manager._tools[new_tool_name] = tool_func
                    print(f"  ✓ Registered tool: {new_tool_name}")
    
    # Also try to copy resources if they exist
    if hasattr(sub_mcp, '_resource_manager') and hasattr(main_mcp, '_resource_manager'):
        if hasattr(sub_mcp._resource_manager, '_resources'):
            for resource_uri, resource_func in sub_mcp._resource_manager._resources.items():
                main_mcp._resource_manager._resources[resource_uri] = resource_func
                print(f"  ✓ Registered resource: {resource_uri}")


def create_unified_server():
    """Create a unified MCP server with tools from all OpenAPI specs"""
    
    print("=" * 70)
    print("🚀 Creating Unified MCP Server")
    print("=" * 70)
    
    # Create the main unified MCP server
    main_mcp = FastMCP("Unified-API-Gateway")
    
    # ==================== JSONPlaceholder API ====================
    print("\n📦 Loading JSONPlaceholder API...")
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
    add_server(main_mcp, mcp_1, prefix="jsonplaceholder")

    # ==================== AuthorizeAssets API ====================
    print("\n📦 Loading AuthorizeAssets API...")
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
    add_server(main_mcp, mcp_2, prefix="authorizeassets")

    # ==================== ViewPurchaseRequest API ====================
    print("\n📦 Loading ViewPurchaseRequest API...")
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
    add_server(main_mcp, mcp_3, prefix="viewpurchaserequest")

    # Count total tools
    tool_count = 0
    if hasattr(main_mcp, '_tool_manager') and main_mcp._tool_manager:
        if hasattr(main_mcp._tool_manager, '_tools'):
            tool_count = len(main_mcp._tool_manager._tools)
    
    print("\n" + "=" * 70)
    print(f"✅ Unified Server Ready with {tool_count} tools total!")
    print("=" * 70)
    print(f"🌐 Server endpoint: http://localhost:8000/mcp")
    print("=" * 70)
    
    return main_mcp


if __name__ == "__main__":
    mcp = create_unified_server()
    print("\n🚀 Starting server...\n")
    mcp.run(transport="http", host="localhost", port=8000)
