from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from mcp.types import PromptMessage,TextContent

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

mcp = FastMCP(
    name="My MCP Server with Prompts",
    stateless_http=True,
)

@mcp.prompt(
    name="Summarize Documents",
    description="Summarizes the content of provided documents.",
    title="Document Summarizer",
)
async def summarize_docs(doc_id:str):
    content = docs.get(doc_id, "Document not found.")
    prompt = f"""
Read the following document carefully and provide a detailed summary that captures 
its main purpose, the key ideas and arguments it presents, and the supporting details or 
evidence used to strengthen those ideas. Explain how the document is structured and flows from 
beginning to end, highlighting how the introduction, body, and conclusion connect together. 
Finally, emphasize the most important insights, conclusions, or action points a reader should 
take away. The summary should be written in clear, concise language, long enough to cover all 
essential points but without unnecessary repetition.
Document Content:
{content}
"""
    return [base.UserMessage(content=prompt)]

@mcp.prompt(
    name="Analyze Financials", 
    description="Analyzes the financial documents provided.",
    title="Financial Document Analyzer",
)
async def analyze_financials(financials_doc_id:str):
    prompt = f"""
You are a financial analyst. Review the provided financial documents and perform a comprehensive
analysis. Identify key financial metrics, trends, and anomalies. Provide insights into the
financial health of the project, including profitability, liquidity, and risk factors.
Summarize your findings in a clear and concise report, highlighting any areas of concern or
opportunity for improvement.
Financial Documents:
{financials_doc_id}
"""
    return PromptMessage(
        role="user",
        content = TextContent(
            type="text",
            text=prompt
        )
    )
@mcp.prompt(
    name="Assistant AI",
    description="A general-purpose assistant AI prompt.",
    title="Assistant AI Prompt",
)
async def assistant_ai():
    prompt = f"""
You are an AI assistant designed to help with a wide range of tasks. You can provide information
on various topics, assist with problem-solving, and offer recommendations based on user input.
Your goal is to be as helpful and informative as possible, ensuring that users receive accurate
and relevant responses to their queries.
"""
    return [base.UserMessage(content=prompt)]


mcp_app = mcp.streamable_http_app()

