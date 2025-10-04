import requests

url = "http://127.0.0.1:8000/mcp"

headers =  {"Accept": "application/json,text/event-streams"}

tool_call_payload_1 =  {
    "jsonrpc":"2.0",
    "method":"resources/read",
    "params":{
        "uri": "docs://documents/outlook.pdf"},
    "id": 1
}

tool_call_payload_2 =  {
    "jsonrpc":"2.0",
    "method":"resources/read",
    "params":{
        "uri": "docs://documents/financials"},
    "id": 2
}

tool_call_payload_3 =  {
    "jsonrpc":"2.0",
    "method":"resources/read",
    "params":{
        "uri": "http://example.com/external_resource"},
    "id": 3
}

tool_list_payload_4 =  {
    "jsonrpc":"2.0",
    "method":"resources/list",
    "params":{},
    "id":0
}

tool_list_payload_5 =  {
    "jsonrpc":"2.0",
    "method":"resources/templates/list",
    "params":{},
    "id":0
}

# For 1st Call
response = requests.post(url, json=tool_call_payload_1, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For 2nd Call
response = requests.post(url, json=tool_call_payload_2, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For 3rd Call
response = requests.post(url, json=tool_call_payload_3, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For Resource List
response = requests.post(url, json=tool_list_payload_4, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")    
print(response.status_code)
for line in response.iter_lines():
    print(line)

# For Template List
response = requests.post(url, json=tool_list_payload_5, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")
print(response.status_code)
for line in response.iter_lines():
    print(line)



