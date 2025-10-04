import requests
from mcp.server.fastmcp import FastMCP

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

mcp = FastMCP(
    name="My MCP Server with Resources",
    stateless_http=True,
)

# Resource No.1
@mcp.resource(
    uri="docs://documents",
    name="Document Resource",
    description="A resource containing various documents.",
    title="Docs Resource",
    mime_type="application/json"
)
async def list_resource_keys():
    doc = list(docs.keys())
    return doc

# Resource No.2
@mcp.resource(
    uri="docs://documents/financials",
    name="Financials Resource",
    description="A resource containing financial documents.",
    title="Financials Resource",
    mime_type="application/json"
)
async def read_financials_resource():
    financial_docs = {k: v for k, v in docs.items() if "financial" in k}
    return financial_docs

# Resource No.3
@mcp.resource(
    uri="docs://documents/doc_info/{doc_id}",
    name="Template Resource",
    description="A resource containing project plans.",
    title="Plans Resource",
    mime_type="application/json"
)
async def read_resource(doc_id: str):
    if doc_id in docs:
        return {doc_id: docs[doc_id]}
    else:
        raise ValueError("Document not found.")
    
# Resource No.4
@mcp.resource(
    uri="docs://documents/{doc_id}",
    name="Template Resource 2",
    description="A resource containing technical specifications.",
    title="Specifications Resource",
    mime_type="application/json"
)
async def read_resource_2(doc_id: str):
    if doc_id in docs:
        return f"Here is it is {docs[doc_id]}"
    else:
        raise ValueError("Document not found.")
    
# Resource No.5
@mcp.resource(
    uri="http://example.com/external_resource",
    name="External Resource",
    description="A resource that simulates fetching data from an external source.",
    title="External Resource",
    mime_type="application/json"
)
async def external_resource():
    result = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    result.raise_for_status()
    return result.json()

mcp_app = mcp.streamable_http_app()