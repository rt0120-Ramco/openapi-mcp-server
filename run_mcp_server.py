"""Unified MCP server with multiple OpenAPI specs using FastMCP mount"""
import json
from pathlib import Path
import httpx
from fastmcp import FastMCP


def create_unified_server():
    """Create a unified MCP server with tools from all OpenAPI specs"""
    
    print("=" * 70)
    print("🚀 Creating Unified API Gateway with FastMCP Mount")
    print("=" * 70)
    
    # Create the main gateway server
    gateway = FastMCP(
        name="Unified-API-Gateway",
        instructions="Unified gateway for multiple Ramco ERP and test APIs"
    )
    
    # ==================== JSONPlaceholder API ====================
    print("\n📦 Loading JSONPlaceholder API...")
    spec_path = Path(__file__).parent / "specs" / "jsonplaceholder-openapi.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://jsonplaceholder.typicode.com",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    jsonplaceholder_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="JSONPlaceholder API",
        validate_output=False
    )
    gateway.mount(jsonplaceholder_mcp, namespace="jsonplaceholder")
    print("   ✓ Mounted with namespace: jsonplaceholder")

    # ==================== AuthorizeAssets API ====================
    print("\n📦 Loading AuthorizeAssets API...")
    spec_path = Path(__file__).parent / "specs" / "authorizeassets.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/FA/ACAP_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    authorizeassets_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="AuthorizeAssets API",
        validate_output=False
    )
    gateway.mount(authorizeassets_mcp, namespace="assets")
    print("   ✓ Mounted with namespace: assets")

    # ==================== ViewPurchaseRequest API ====================
    print("\n📦 Loading ViewPurchaseRequest API...")
    spec_path = Path(__file__).parent / "specs" / "viewpurchaserequest.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/PRA/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={ 
                    "Accept": "application/json", 
                    "Content-Type": "application/json",
                    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkI0MUU2NzE0NDk3RjEyREM1RTc3MDhCQzdCMENCNjVGQjRBRERCMkJSUzI1NiIsInR5cCI6IkpXVCIsIng1dCI6InRCNW5GRWxfRXR4ZWR3aThld3kyWDdTdDJ5cyJ9.eyJuYmYiOjE3NzIxMDQ2ODcsImV4cCI6MTc3MjEwODI4NywiaXNzIjoiaHR0cHM6Ly9lcnBlbmhkZXYucmFtY291YXQuY29tL2NvcmVzZWN1cml0eW9wcyIsImF1ZCI6WyJjb20ucmFtY28udndhcGllLmFkay5hcGlzIiwiY29tLmV4dGVybmFsLmFwaXMiLCJodHRwczovL2VycGVuaGRldi5yYW1jb3VhdC5jb20vY29yZXNlY3VyaXR5b3BzL3Jlc291cmNlcyJdLCJjbGllbnRfaWQiOiJjb3JlLmluZnJhLnNydnJjbGllbnQiLCJyX3RpZCI6InJhbWNvIiwic3ViIjoiQVBOVVNFUjEiLCJhdXRoX3RpbWUiOjE3NzIxMDQ2ODcsImlkcCI6ImxvY2FsIiwianRpIjoiRjFGNEUwODIxMTAxMkUzMkQxREM1QjYxNUQ5MjZERTUiLCJpYXQiOjE3NzIxMDQ2ODcsInNjb3BlIjpbInJ2d19pbXBlcnNvbmF0ZSJdLCJhbXIiOlsiY3VzdG9tX2NsaWVudF9jcmVkZW50aWFscyJdfQ.pTx0DeHnUHCHpNdjyez3On9_zUbVhEzV2oGgTkn5X1tMIhBDzV_8dQigsATROwsdPwdZkJ5QDjzb_YStO-DzrzhMoWQjbLkk6gkiuv_Pgxr3fvFBoA6no7prqStpF4XYX8UdO-nuWA2bNLdPeZUCRX5e3QPQBy5Ch8YjjpsGgztC54m3llrixDkw_3gjKncN20h4amAfeQejZ2f-az4frI9zBzQa_hdWT9uEjHjbz55DexEeM0zEffT0x92APXF2x02w-ZnS8EoWSd2C6hXR3QqhjNC2pb_QmBnFtaFCxOM_gfqQiuW_YKqtT-TwbZt1t0wl1mbOHNlizXzIpwYboA"
                }
    )

    viewpr_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="ViewPurchaseRequest API",
        validate_output=False
    )
    gateway.mount(viewpr_mcp, namespace="purchase_request")
    print("   ✓ Mounted with namespace: purchase_request")

    # ==================== CreatePRPOConversion API ====================
    print("\n📦 Loading CreatePRPOConversion API...")
    spec_path = Path(__file__).parent / "specs" / "createPRPOConversion3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/PROConv_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    createprpo_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="CreatePRPOConversion API",
        validate_output=False
    )
    gateway.mount(createprpo_mcp, namespace="pr_po_conversion")
    print("   ✓ Mounted with namespace: pr_po_conversion")

    # ==================== GETSupplierItemAndLeadTimeDtls API ====================
    print("\n📦 Loading GETSupplierItemAndLeadTimeDtls API...")
    spec_path = Path(__file__).parent / "specs" / "GETSupplierItemAndLeadTimeDtls3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/SUPP_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    supplier_item_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="SupplierItemLeadTime API",
        validate_output=False
    )
    gateway.mount(supplier_item_mcp, namespace="supplier_item")
    print("   ✓ Mounted with namespace: supplier_item")

    # ==================== GETSupplierScoreCardDtls API ====================
    print("\n📦 Loading GETSupplierScoreCardDtls API...")
    spec_path = Path(__file__).parent / "specs" / "GETSupplierScoreCardDtls3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/SUPRAT_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    supplier_scorecard_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="SupplierScoreCard API",
        validate_output=False
    )
    gateway.mount(supplier_scorecard_mcp, namespace="supplier_scorecard")
    print("   ✓ Mounted with namespace: supplier_scorecard")

    # ==================== SearchBPO API ====================
    print("\n📦 Loading SearchBPO API...")
    spec_path = Path(__file__).parent / "specs" / "SearchBPO3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/BLPO_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    searchbpo_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="SearchBPO API",
        validate_output=False
    )
    gateway.mount(searchbpo_mcp, namespace="blanket_po")
    print("   ✓ Mounted with namespace: blanket_po")

    # ==================== ViewPO API ====================
    print("\n📦 Loading ViewPO API...")
    spec_path = Path(__file__).parent / "specs" / "ViewPO3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/PO_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    viewpo_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="ViewPO API",
        validate_output=False
    )
    gateway.mount(viewpo_mcp, namespace="purchase_order")
    print("   ✓ Mounted with namespace: purchase_order")

    # ==================== ViewReleaseSlip API ====================
    print("\n📦 Loading ViewReleaseSlip API...")
    spec_path = Path(__file__).parent / "specs" / "ViewReleaseSlip3.0.json"
    with open(spec_path) as f:
        spec = json.load(f)

    client = httpx.AsyncClient(
        base_url="https://erpenhdev.ramcouat.com/coreapiops/Purchase/PRS_SER/v1",
        verify=False,
        timeout=30.0,
        follow_redirects=True,
        headers={"Accept": "application/json", "Content-Type": "application/json"}
    )

    viewreleaseslip_mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        name="ViewReleaseSlip API",
        validate_output=False
    )
    gateway.mount(viewreleaseslip_mcp, namespace="release_slip")
    print("   ✓ Mounted with namespace: release_slip")
    
    print("\n" + "=" * 70)
    print(f"✅ Unified API Gateway Ready!")
    print(f"   9 API servers mounted with namespaced tools")
    print("=" * 70)
    print(f"🌐 Server endpoint: http://localhost:8000/mcp")
    print("=" * 70)
    
    return gateway


if __name__ == "__main__":
    mcp = create_unified_server()
    print("\n🚀 Starting server...\n")
    mcp.run(transport="http", host="localhost", port=8000)
