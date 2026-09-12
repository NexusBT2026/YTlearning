from client import ApiClient

api = ApiClient("https://jsonplaceholder.typicode.com")

print(api.get("/posts/1"))
print(api.post("/posts", {"title": "Hello", "body": "World"}))
