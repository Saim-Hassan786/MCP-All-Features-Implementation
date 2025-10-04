import requests

url = "http://127.0.0.1:8000/mcp"

headers =  {"Accept": "application/json,text/event-streams"}

payload =  {
    "jsonrpc":"2.0",
    "method":"tools/list",
    "params":{},
    "id":1
}


response = requests.post(url=url, json=payload, headers=headers)
print(response.status_code)
for lines in response.iter_lines():
    if lines:
        print(lines)