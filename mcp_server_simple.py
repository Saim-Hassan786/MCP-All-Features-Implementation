from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name = "My 1st MCP Server",
    stateless_http = True
)


mcp_app = mcp.streamable_http_app()