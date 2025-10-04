import asyncio
from mcp import ClientSession,types
from mcp.client.streamable_http import streamablehttp_client
from typing import Optional, Any
from contextlib import AsyncExitStack

class MCPClientImplementation:
    def __init__(self,server_url:str):
        self.server_url = server_url
        self._session : Optional[ClientSession] = None
        self.async_stack :AsyncExitStack = AsyncExitStack()

    async def connect(self):
        streaming_session = await self.async_stack.enter_async_context(
            streamablehttp_client(self.server_url)
        )
        _read,_write,_session_id = streaming_session
        self._session = await self.async_stack.enter_async_context(
            ClientSession(
            read_stream=_read,
            write_stream=_write,
            )
        )
        await self._session.initialize()

    async def session(self):
        if self.session is None:
            raise ConnectionError("connect to MCP server first")
        return self.session
    
    async def list_tools(self) -> types.ListToolsResult:
        tools = await self._session.list_tools()
        return tools
    
    async def call_tool(self,tool_name:str,arguments:dict[str,Any])->types.CallToolResult:
        tool_result = await self._session.call_tool(
            name=tool_name,
            arguments=arguments
        )
        return tool_result
    
    async def list_resources(self) -> types.ListResourcesResult:
        resources = await self._session.list_resources()
        return resources
    
    async def read_resource(self,resource_uri:str)->types.ReadResourceResult:
        read_result = await self._session.read_resource(
            uri=resource_uri
        )
        return read_result
    
    async def list_templates_resources(self)->types.ListResourceTemplatesResult:
        templates = await self._session.list_resource_templates()
        return templates
    
    async def cleanup(self):
        await self.async_stack.aclose()
        self._session = None

    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        await self.cleanup()


async def main():
    async with MCPClientImplementation(server_url = "http://127.0.0.1:8000/mcp") as client:
      resources_list = await client.list_resources()
      print("Available Resources:", resources_list.resources)

      read_resource = await client.read_resource(
        resource_uri = "docs://documents/financials"
      )
      print("Read Resource Result:", read_resource) 

      read_resource_2 = await client.read_resource(
        resource_uri = "docs://documents/doc_info/outlook.pdf",
      ) 
      print("Read Resource Result 2:", read_resource_2.contents[0].text)

      templates = await client.list_templates_resources()
      print("Resource Templates:", templates)

      external_resource = await client.read_resource(
        resource_uri = "http://example.com/external_resource"
      )
      print("External Resource Result:", external_resource)           

if __name__ == "__main__":
    asyncio.run(main())
