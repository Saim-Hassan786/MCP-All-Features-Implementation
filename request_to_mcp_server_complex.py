import httpx
import json
import asyncio
from typing import Any

async def fetch_mcp_response(method:str,params:dict[str,Any]|None=None):
    """Fetch response from MCP server"""
    payload = {
        "jsonrpc":"2.0",
        "method":method,
        "params":params or {},
        "id":1
    }
    url = "http://127.0.0.1:8000/mcp"
    headers =  {"Accept": "application/json,text/event-streams",
                "Content-Type": "application/json"}
    try : 
        async with httpx.AsyncClient() as client , client.stream(
            method="POST",
            url=url,
            json=payload,
            headers=headers,
            timeout=10
        ) as response:
            print(f"Fetching Response From MCP SERVER for method: {method} with params: {params}")
            print(response.status_code)
            async for line in response.aiter_lines():
                if line: 
                    print(f"   <- Received raw data: {line}")
                    if line.startswith("data: "):
                        line = line[6:]
                        print(f"   <- Received data: {line}")
                        return json.loads(line)
        return f"Error: No response received from server for method: {method} with params: {params}"
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        print(f"Error details: {str(e)}")


async def main():
    print("\n[Step 1: Ask the server what it can do]")
    print("We send a 'tools/list' request to discover available tools.")
    tools_response = await fetch_mcp_response("tools/list")
    
    print("\nRESULT OF TOOLS: ", tools_response)

if __name__ == "__main__":
    asyncio.run(main())