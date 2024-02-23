import requests
#
# response = requests.post(
#     "http://127.0.0.1:5000/user",
#     json={"username": "user_1", "password": "ffdsgfsewdtgyet3wet"},
# )
# print(response.status_code)
# print(response.text)



# response = requests.patch("http://127.0.0.1:5000/users/3", json={"usernam": "qwee", "password": "qwqqwqw"})
# print(response.status_code)
# print(response.text)

# response = requests.delete(
#     "http://127.0.0.1:5000/users/1",
# )
# print(response.status_code)
# print(response.text)
#
#
response = requests.get(
    "http://127.0.0.1:5000/user/1",
)
print(response.status_code)
print(response.text)
