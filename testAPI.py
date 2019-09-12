import requests

context = {
	"username":"salilModak",
	"email":"salil.modak@gmail.com",
	"password":"salil@roshan@123"
}
url = 'http://localhost:8000/api/register'
response = requests.post(url,context)
print(response.json())

context = {
	'username':'salilModak',
	'password': 'salil@roshan@123'
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
