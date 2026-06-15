import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())

data = {
    "title": "New",
    "completed": False,
    "userId": 1

}

response = httpx.post("https://jsonplaceholder.typicode.com/todos")
print(response.status_code)
print(response.json())


headers = {"Authorization": "Secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.request.headers)
print(response.headers)
print(response.json())


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.json())
print(response.request.url, response.request.url.query)


files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.status_code)
print(response.json())

client = httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    headers={"Authorization": "Secret_token"}
)
response1 = client.get("/todos/1")
response2 = client.get("/todos/2")
print(response1.json())
print(response2.json())
