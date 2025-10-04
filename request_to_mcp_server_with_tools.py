import requests

url = "http://127.0.0.1:8000/mcp"

headers =  {"Accept": "application/json,text/event-streams"}

tool_call_payload_1 =  {
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
        "name": "My First Tool",
        "arguments" : {
            "name": "Saim"
        }}, 
    "id":1
}

tool_call_payload_2 =  {
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
        "name": "My Second Tool",
        "arguments" : {
            "name": "Saim"
        }}, 
    "id":2
}

tool_call_payload_3 =  {
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
        "name":"My Third Tool",
        "arguments":{
            "name": "Saim",
            "age": 25
        }
    },
    "id":3
}

tool_list_payload =  {
    "jsonrpc":"2.0",
    "method":"tools/list",
    "params":{}, 
    "id":0
}

# For 1st Tool Call
response = requests.post(url, json=tool_call_payload_1, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")
print(response.status_code)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

# For 2nd Tool Call
response = requests.post(url, json=tool_call_payload_2, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")
print(response.status_code)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

# For 3rd Tool Call
response = requests.post(url, json=tool_call_payload_3, headers=headers, stream=True)
print("Response Coming From Server")
print("================================")
print(response.status_code)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

# For Tool List
response = requests.post(url, json=tool_list_payload, headers=headers, stream=True)
print("Response Coming From Server")    
print("================================")
print(response.status_code)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

    