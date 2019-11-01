import requests
import time

# x = requests.get("http://www.parsiankhazar.ir", timeout=10)
# # print(x.status_code)
# # print(x.url)
# # for key,values  in x.headers.items():
# #     print(key +" = "+ values)
# # print(x.text)
# # print(x.content)
# print(x.cookies)


# y = requests.put("http://parsiankhazar.com/get")
# y = requests.options("http://parsiankhazar.com/get")
# print(id(y))
# # for key, values in y.headers.items():
# #     print(key + " " +  values)
# # print(y.cookies)
# print(y.headers)



# params
# paylod={"key":"value","key2":"value2"}
# x = requests.get("http://parsiankhazar.com", params = paylod)
# print(x.url)


# paylod= {'key1': 'value1', 'key2': ['value2', 'value3']}
# x = requests.get("http://parsiankhazar.com/get", params = paylod)
# print(x.url)
# print(x.encoding)
# x.encoding='ISO-8859-1'
# print(x.encoding)
# y = x.headers

# print(y)


# r = requests.get('https://api.github.com/events', stream=True)
# print(r.row)


data = {"email":"test@gmail.com",
        "password":"12345"}
s = requests.post("http://shalishomal.ir", params=data)
print(s.status_code)





