
import json
import requests

def getPhoneNumbers(country, phoneNumber):
    API_HOST = "https://jsonmock.hackerrank.com/api/countries?name="
    url = API_HOST + country

    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

    response = requests.get(url, headers=headers)
    jsonObject = json.loads(response.text)

    answer = "+"

    if jsonObject.get("data"):
        answer += jsonObject.get("data")[0].get("callingCodes")[-1]
        answer += " "
        answer += phoneNumber
    else:
        answer = "-1"

    return answer

print(getPhoneNumbers("Afghanistan", "656445445"))
print(getPhoneNumbers("Puerto Rico", "564593986"))
print(getPhoneNumbers("Oceania", "987574876"))

