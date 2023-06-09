# 1
print("============================")
print("회원가입")
print("============================")

register = False

while not register:
    print("회원가입을 진행하시겠습니까?")
    print("y:진행              N:취소")
    answer = input(">> ")
    answer = answer.lower()

    if answer == "y":
        register = True
        print("============================")
        print("회원가입이 진행됩니다.")
        print("============================")

    elif answer == "n":
        print("============================")
        print("회원가입이 취소됩니다.")
        print("============================")
    else:
        print("입력 값을 확인해주세요.")


# 2
users = []  # users 리스트: 유저 정보를 저장

while True:
    user = {}  # user 딕셔너리: key-value 정보들을 딕셔너리 객체 하나로 저장, 비밀번호, 이름, 생년월일, 이메일을 입력받음
    username = input("ID: ")
    while True:
        pwd = input("PWD: ")
        pwd2 = input("PWD 확인: ")
        if pwd == pwd2:
            break
        else:
            print("패스워드가 일치하지 않습니다.")
    name = input("이름: ")
    while True:
        birth = input("생년월일(6자리): ")
        if len(birth) == 6:
            break
        else:
            print("생년월일 입력값이 올바르지 않습니다.")
    email = input("이메일: ")

    # 3
    # 입력받은 value 값을 key에 저장
    user["username"] = username
    user["password"] = pwd
    user["name"] = name
    user["birth"] = birth
    user["email"] = email

    users.append(user)  # 왜 딕셔너리를 리스트에 저장하는거지?  => 회원 여러 명 : 딕셔너리 여러 개 저장!
    print(users)
    # [{'username': 'y', 'password': 'y', 'name': 'y', 'birth': 'yyyyyy', 'email': 'y'}]

    print("============================")
    print(user["name"], "님 가입을 환영합니다!")
    print("============================")

    print("회원가입을 추가로 진행하시겠습니까?")
    print("y:진행              N:취소")
    answer = input(">> ")
    answer = answer.lower()

    if answer == "y":
        pass
    elif answer == "n":
        exit()
    else:
        exit()
