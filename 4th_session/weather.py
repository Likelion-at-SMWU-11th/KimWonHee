import requests
import json

city = "Seoul"
# apikey = "********************"
apikey = "***************************"
# api = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" : 그대로 나와버림
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
# f-string을 이용했더니 city에 seoul이, apikey엔 api key 값이 들어간 채로 출력됨.
# 파이썬의 f-string을 사용하면 문자열 안에 우리가 원하는 변수를 넣을 수 있다.
# 1) f-string을 적용하고 싶은 문자열 앞에 f라고 적어주기
# 2) 변수를 넣어주고 싶은 부분에는 변수 이름을 중괄호로 묶어주기

# print(api)

result = requests.get(api)
# print(result.text) :필요없는 것들도 많으니까 필요한 것만 뽑고 싶어요
# print(type(result.text)) : class 'str' <- json이 str로 변환된 형태 => 다시 json으로 변환해서 융통하자...
data = json.loads(result.text)

# print(type(result.text)) #str형
# print(type(data))  # dict형: api 통신에 많이 쓰이는 json으로 변환했더니 str이 dict형태가 됐다.

# result.text 출력해서 dict 구조 파악 후 원하는 key값의 value만 가져옴
print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["main"], "입니다.")
# weather라는 key의 value가 list형=> list의 1번째 값인 dict에서 main이라는 key의 value가 clouds(날씨 value값)
