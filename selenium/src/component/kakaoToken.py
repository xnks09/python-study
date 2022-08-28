import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
"grant_type" : "authorization_code",
"client_id" : "5f6d9e4fee621db75d2472b9f3b1ac24",
"redirect_uri" : "https://example.com/oauth",
"code" : "yky9_mgKfBBJZMVZVQpW8hEiyguygsj1B-GI4JUbWX6NrPk449K4bqAzwoWNVE9t-308NworDNQAAAGC0DYrrg"
}

response = requests.post(url, data=data)
tokens = response.json()

# 토큰을 파일로 저장하기
if "access_token" in tokens:
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)
        print("Tokens saved successfully")
else:
    print(tokens)