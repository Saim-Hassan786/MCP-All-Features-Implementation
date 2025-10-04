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
    
    async def get_list_prompts(self) -> types.ListPromptsResult:
        prompts = await self._session.list_prompts()
        return prompts
    
    async def get_prompts(self,name:str,arguments:dict[str,str])->types.GetPromptResult:
        prompt_result = await self._session.get_prompt(
            name=name,
            arguments=arguments
        )
        return prompt_result
    
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
      prompts = await client.get_list_prompts()
      print("Prompts List:")
      print(prompts)    

      prompt_response = await client.get_prompts(
          name="Summarize Documents",
          arguments={"doc_id": "report.pdf"}
      )
      print("Prompt Response for 'Summarize Documents':")
      print(prompt_response.messages[0].content.text)

      prompt_response_2 = await client.get_prompts(
          name="Analyze Financials",
          arguments={"financials_doc_id": "financials.docx"}
      )
      print("Prompt Response for 'Analyze Financials':")
      print(prompt_response_2)

      prompt_response_3 = await client.get_prompts(
          name="Assistant AI",
          arguments={}
      )
      print("Prompt Response for 'Assistant AI':")
      print(prompt_response_3)          

if __name__ == "__main__":
    asyncio.run(main())
