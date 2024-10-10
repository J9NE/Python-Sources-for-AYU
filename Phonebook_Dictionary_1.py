'''
* run() 함수가 else-if 중첩문으로 작성된 소스코드
'''

def add_contact(phonebook):
    # name: 추가하고자 하는 전화번호의 주인 이름을 저장하는 변수
    name = input("이름을 입력하세요: ")
    
    # ! [조건] 이미 전화번호부에 추가된 이름인지 확인하는 조건문
    if name in phonebook:
        print("이미 전화번호부에 등록되어 있는 이름입니다!")
        print(f"{name}: {phonebook[name]}")
        print("전화번호를 수정하고 싶다면, [3. 전화번호 수정] 기능을 사용하세요.")
    
    # 전화번호부에 추가되어있지 않은 이름일 때 새로운 번호 추가
    else:
        phone_number = input("전화번호를 입력하세요 (예: 01011110000): ")

        # ! [조건] 입력받은 전화번호 문자열 유효성 검사
        # 각각 (1) 총 11자리인지 (2) 010으로 시작하는지 (3) (int형으로 변환 가능한) 숫자로 이루어진 문자열인지 확인함
        if len(phone_number) == 11 and phone_number.startswith('010') and phone_number.isdigit():
            # 전화번호 문자열이 유효할 때, 딕셔너리에 (이름)-(전화번호) 키값쌍으로 저장
            phonebook[name] = phone_number
            print(f"{name}의 전화번호가 추가되었습니다.")
        # 전화번호 문자열이 유효하지 않을 때((1)~(3) 중 위배되는 조건이 있을 때), 딕셔너리에 저장하지 않음.
        else:
            print("잘못된 전화번호 형식입니다. 다시 입력해주세요.")

def search_contact(phonebook):
    # name: 검색하고자 하는 전화번호의 주인 이름을 저장하는 변수
    name = input("검색할 이름을 입력하세요: ")
    # ! [조건] 검색하고자 하는 이름이 phonebook 딕셔너리에 존재하는지 검사
    if name in phonebook:
        # 존재할 때, 데이터 출력
        print(f"{name}: {phonebook[name]}")
    else:
        # 존재하지 않을 때, 존재하지 않음을 알림
        print("해당 이름이 없습니다.")

def modify_contact(phonebook):
    # name: 수정하고자 하는 전화번호의 주인 이름을 저장하는 변수
    name = input("수정할 이름을 입력하세요: ")
    # ! [조건] 수정하고자 하는 이름(name)이 phonebook 딕셔너리에 존재하는지 검사
    if name in phonebook:
        # 조건을 만족할 때, 사용자로부터 new_number를 입력받고 갱신함
        new_number = input("새 전화번호를 입력하세요 (예: 01011110000): ")
        # ! [조건] 입력받은 전화번호 문자열 유효성 검사
        if len(new_number) == 11 and new_number.startswith('010') and new_number.isdigit():
            # 전화번호 문자열이 유효할 때, (이름)-(전화번호) 키값쌍의 (전화번호)를 (새로운 전화번호(new_nubmer))로 갱신
            phonebook[name] = new_number
            print(f"{name}의 전화번호가 수정되었습니다.")
            print(f"수정된 전화번호는 {phonebook[name]}입니다.\n")
        # 전화번호 문자열이 유효하지 않을 때, 새로운 전화번호로 갱신하지 않음
        else:
            print("잘못된 전화번호 형식입니다.")
    else:
        print("해당 이름이 없습니다.")

def delete_contact(phonebook):
    # name: 삭제하고자 하는 전화번호의 주인 이름을 저장하는 변수
    name = input("삭제할 이름을 입력하세요: ")
    # ! [조건] 검색하고자 하는 이름이 phonebook 딕셔너리에 존재하는지 검사
    if name in phonebook:
        # 존재할 때, del 키워드를 통해 phonebook 딕셔너리에서 {name} 키를 갖는 키값쌍 삭제
        del phonebook[name]
        print(f"{name}의 전화번호가 삭제되었습니다.")
    # 존재하지 않을 때, 존재하지 않음을 알림
    else:
        print("해당 이름이 없습니다.\n")

def display_contacts(phonebook):
    print("\n저장된 전화번호 목록:")
    print("NAME\t\tPHONE NUMBER")
    print("="*30)
    # ! [조건] phonebook이 요소(키값쌍)를 갖는지 검사
    if phonebook:
        # 존재할 때, phonebook 딕셔너리의 모든 요소를 출력
        for user_name, number in phonebook.items():
            print(f"{user_name}: {number}")
    # 존재하지 않을 때(phonebook 딕셔너리가 비어있을 때), 비어있음을 알림
    else:
        print("저장된 전화번호가 없습니다.\n")

def run():    
    phonebook = {}  # 이름-전화번호를 저장할 빈 딕셔너리 생성

    # 각 기능을 번호(1~6)로 구분
    # '6' 입력시 break로 while:True 반복문을 빠져나와 종료됨
    while True:
        print("\n" + "*"*5 + "전화번호 관리 프로그램" + "*"*5)
        print("<프로그램 기능 목록>")
        print("1. 전화번호 추가")
        print("2. 전화번호 검색")
        print("3. 전화번호 수정")
        print("4. 전화번호 삭제")
        print("5. 저장된 전화번호 확인")
        print("6. 프로그램 종료")

        # choice: 사용자가 입력한 숫자를 저장하는 변수
        choice = input("원하는 작업을 선택하세요 (1-6): ")

        # 1. 전화번호 추가 기능
        if choice == '1':
            add_contact(phonebook)
        # 2. 전화번호 검색 기능
        elif choice == '2':
            search_contact(phonebook)
        # 3. 전화번호 수정 기능
        elif choice == '3':
            modify_contact(phonebook)
        # 4. 전화번호 삭제 기능
        elif choice == '4':
            delete_contact(phonebook)
        # 5. 전체 전화번호 열람 기능
        elif choice == '5':
            display_contacts(phonebook)
        # 6. 프로그램 종료 기능
        elif choice == '6':
            print("\n프로그램을 종료합니다.")
            break
            
        # 사용자가 choice 입력 단계에서 번호(1~6) 외에 다른 문자를 입력했을 경우 
        else:
            print("=" * 50)
            print("잘못된 입력입니다.\n원하시는 기능의 숫자를 입력해주세요.(1~6).")
            print("=" * 50)

run()
