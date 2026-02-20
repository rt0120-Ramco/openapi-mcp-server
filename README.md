# Petstore MCP Server

A Model Context Protocol (MCP) server for the Swagger Petstore API, providing tools to interact with the Pet Store endpoints.

## Features

The MCP server provides the following tools:
- `get_pet_by_id` - Find pet by ID
- `add_pet` - Add a new pet to the store
- `update_pet` - Update an existing pet
- `delete_pet` - Delete a pet
- `get_inventory` - Returns pet inventories by status

## Setup

### Prerequisites
- Python 3.13+ installed
- Required packages: `fastmcp`, `httpx`

### Installation

1. Install dependencies:
```powershell
pip install fastmcp httpx
```

2. Run the MCP server:
```powershell
python run_mcp_server.py
```

## Configuration for MCP Clients

### For Insomnia

Add this configuration to your MCP client settings:

```json
{
  "mcpServers": {
    "petstore-api": {
      "disabled": false,
      "timeout": 60,
      "type": "stdio",
      "command": "C:/Users/Sara70&D61/AppData/Local/Programs/Python/Python313/python.exe",
      "args": [
        "c:/github/rapis-mcp-server/run_mcp_server.py"
      ]
    }
  }
}
```

### For Other MCP Clients

Use the following configuration pattern:
- **Transport**: stdio
- **Command**: Path to Python executable
- **Args**: Path to `run_mcp_server.py`

## Files

- `run_mcp_server.py` - Custom MCP server implementation using FastMCP
- `petstore-openapi.json` - OpenAPI specification for the Petstore API

## API Endpoints

Base URL: `https://petstore3.swagger.io/api/v3`

The server wraps the following Petstore API operations:
- GET `/pet/{petId}` - Get pet by ID
- POST `/pet` - Add new pet
- PUT `/pet` - Update existing pet
- DELETE `/pet/{petId}` - Delete pet
- GET `/store/inventory` - Get inventory

## Testing

Once the server is running, you can connect to it from:
- Insomnia (with MCP support)
- Claude Desktop
- Any other MCP-compatible client

The server will expose the tools listed above for interaction with the Petstore API.