"""MCP server created from OpenAPI spec using FastMCP"""
import json
from pathlib import Path
import httpx
from fastmcp import FastMCP

# Load OpenAPI spec - using JSONPlaceholder (reliable test API)
spec_path = Path(__file__).parent / "jsonplaceholder-openapi.json"
with open(spec_path) as f:
    openapi_spec = json.load(f)

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Create an HTTP client for the API
client = httpx.AsyncClient(
    base_url=BASE_URL,
    verify=False,  # Disable SSL verification
    timeout=30.0,
    follow_redirects=True,
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
)

# Create the MCP server from OpenAPI spec
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="JSONPlaceholder API"
)

if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)
