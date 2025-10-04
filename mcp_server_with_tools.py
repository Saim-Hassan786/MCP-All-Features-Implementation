from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name = "My 1st MCP Server with Tools",
    stateless_http = True
)

# Tool N0.1
@mcp.tool(
    name="My First Tool",
    description="A simple tool that returns a greeting message.",
    title="Hello Tool",
)
async def hello_tool(name: str) -> str:
    return f"Hello, {name}!"

# Tool N0.2
@mcp.tool(
    name="My Second Tool",
    description="A simple tool that returns a farewell message.",
    title="Goodbye Tool",
)
async def goodbye_tool(name: str) -> str:
    return f"Goodbye, {name}!"

# Tool N0.3
@mcp.tool(
    name="My Third Tool",
    description="A simple tool that returns bio data of student.",
    title="Bio data Tool",
)
async def bio_data_tool(name: str,age:int) -> str:
    return f"Name: {name}, Age: {age}"


mcp_app = mcp.streamable_http_app()
