import requests

url = "http://127.0.0.1:8000/mcp"

headers =  {"Accept": "application/json,text/event-streams"}

tool_call_payload_1 =  {
    "jsonrpc":"2.0",
    "method":"prompts/get",
    "params":{
        "name": "Summarize Documents",
        "arguments" : {
            "doc_id": "report.pdf"
        }
    },
    "id": 1
}

tool_call_payload_2 =  {
    "jsonrpc":"2.0",
    "method":"prompts/get",
    "params":{
        "name": "Analyze Financials",
        "arguments" : {
            "financials_doc_id": "financials.docx"
        }
    },
    "id": 1
}

tool_call_payload_3 =  {
    "jsonrpc":"2.0",
    "method":"prompts/get",
    "params":{
        "name": "Assistant AI",
    "id": 1
}
}

tool_list_payload_4 =  {
    "jsonrpc":"2.0",
    "method":"prompts/list",
    "params":{},
    "id":0
}

# For 1st Tool Call
response = requests.post(url, json=tool_call_payload_1, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For 2nd Tool Call
response = requests.post(url, json=tool_call_payload_2, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For 3rd Tool Call
response = requests.post(url, json=tool_call_payload_3, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For Prompt List
response = requests.post(url, json=tool_list_payload_4, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")    
print(response.status_code)
for line in response.iter_lines():
    print(line)




