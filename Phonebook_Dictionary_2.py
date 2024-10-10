'''
* run() 함수에서 if-else 중첩문 대신 options 딕셔너리로 전화번호 관리 프로그램의 기능을 관리하는 소스코드
'''

def add_contact(phonebook):
    name = input("이름을 입력하세요: ")
    if name in phonebook:
        print("이미 전화번호부에 등록되어 있는 이름입니다!")
        print(f"{name}: {phonebook[name]}")
        print("전화번호를 수정하고 싶다면, [3. 전화번호 수정] 기능을 사용하세요.")
    else:
        phone_number = input("전화번호를 입력하세요 (예: 01011110000): ")
        if len(phone_number) == 11 and phone_number.startswith('010') and phone_number.isdigit():
            phonebook[name] = phone_number
            print(f"{name}의 전화번호가 추가되었습니다.")
        else:
            print("잘못된 전화번호 형식입니다. 다시 입력해주세요.")

def search_contact(phonebook):
    name = input("검색할 이름을 입력하세요: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("해당 이름이 없습니다.")

def modify_contact(phonebook):
    name = input("수정할 이름을 입력하세요: ")
    if name in phonebook:
        new_number = input("새 전화번호를 입력하세요 (예: 01011110000): ")
        if len(new_number) == 11 and new_number.startswith('010') and new_number.isdigit():
            phonebook[name] = new_number
            print(f"{name}의 전화번호가 수정되었습니다.")
            print(f"수정된 전화번호는 {phonebook[name]}입니다.\n")
        else:
            print("잘못된 전화번호 형식입니다.")
    else:
        print("해당 이름이 없습니다.")

def delete_contact(phonebook):
    name = input("삭제할 이름을 입력하세요: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name}의 전화번호가 삭제되었습니다.")
    else:
        print("해당 이름이 없습니다.\n")

def display_contacts(phonebook):
    print("\n저장된 전화번호 목록:")
    if phonebook:
        for user_name, number in phonebook.items():
            print(f"{user_name}: {number}")
    else:
        print("저장된 전화번호가 없습니다.\n")

def run():
    phonebook = {}

    options = {
        '1': ('전화번호 추가', add_contact),
        '2': ('전화번호 검색', search_contact),
        '3': ('전화번호 수정', modify_contact),
        '4': ('전화번호 삭제', delete_contact),
        '5': ('저장된 전화번호 확인', display_contacts),
        '6': ('전화번호부 내보내기', None)
    }

    while True:
        print("\n" + "*"*5 + "전화번호 관리 프로그램" + "*"*5)
        print("<프로그램 기능 목록>")
        for num, (description, _) in options.items():
            print(f"{num}. {description}")

        choice = input("원하는 작업의 번호만 입력한 후, 엔터하세요(1-6):")

        if choice in options:
            if choice == '6':
                print("\n프로그램을 종료합니다..")
                break
            options[choice][1](phonebook)
        else:
            print("*"*40)
            print("잘못된 입력입니다.\n원하시는 기능의 숫자를 입력해주세요.(1-6):")
            print("*"*40)


run()