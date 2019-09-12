import requests

context = {
	"username":"shradha",
	"email":"s@gmail.com",
	"password":"r@s@123"
}
url = 'http://localhost:8000/api/register'
response = requests.post(url,context)
print(response.json())

context = {
	'username':'shradha',
	'password': 'r@s@123'
}
url = 'http://localhost:8000/api/login'
response = requests.post(url,context)
print(response.json())

header = {
	'Authorization': 'Token '+str(response.json()['token'])
}
url = 'http://localhost:8000/api/test'
response = requests.get(url,headers=header)
print(response.json())
