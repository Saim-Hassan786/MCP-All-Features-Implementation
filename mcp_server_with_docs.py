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
    name = "My 1st MCP Server with Docs",
    stateless_http = True
)

# Tool N0.1
@mcp.tool(
    name="Document Retrieval Tool",
    description="A tool to retrieve documents based on their names.",
    title="Doc Retrieval Tool",
)
async def document_retrieval_tool(doc_name: str) -> str:
    return docs.get(doc_name, "Document not found.")

# Tool N0.2
@mcp.tool(
    name="List Documents Tool",
    description="A tool to list all available document names.",
    title="List Docs Tool",
)
async def list_documents_tool() -> str:
    return ", ".join(docs.keys())   

# Tool N0.3
@mcp.tool(
    name="Document Edit Tool",
    description="A tool to edit the content of a document.",
    title="Edit Doc Tool",
)
async def document_edit_tool(doc_name: str, new_content: str) -> str:
    if doc_name in docs:
        docs[doc_name] = new_content
        return f"Document '{doc_name}' updated successfully."
    else:
        raise ValueError("Document not found.")

mcp_app = mcp.streamable_http_app()