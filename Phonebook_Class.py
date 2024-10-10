# 전역변수
name_header = "이름"
phone_number_header = "전화번호"
name_header_width = 20

class PhonebookManager:
    def make_phonebook_dict(self):
        self.phonebook = {}
        try:
            with open(self.filename, 'r', encoding='utf-8') as inputFile:
                for line in inputFile:
                    name, phone_number = line.split(',')
                    self.phonebook[name] = phone_number.strip()
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.\n새 전화번호부를 생성합니다.\n")
        except Exception as e:
            print(f"객체를 생성하는 과정에서 오류가 발생했습니다: {e}\n")
        return self.phonebook

    def __init__(self, filename=""):
        self.filename = filename
        self.phonebook = self.make_phonebook_dict()

    # 전화번호부 관리 프로그램의 기능을 수행하는 메소드
    # 1. 전화번호 추가
    def add_phone_number(self):
        input_name = input("이름을 입력하세요: ")
        if input_name in self.phonebook:
            print("이미 전화번호부에 등록되어 있는 이름입니다!")
            print(f"{input_name:<{name_header_width}}: {self.phonebook[input_name]}")
            print("전화번호를 수정하고 싶다면, [3. 전화번호 수정] 기능을 사용하세요.")
        else:
            phone_number = input("전화번호를 입력하세요 (예: 01011110000):")
            # 전화번호 유효성 검사
            if len(phone_number) == 11 and phone_number.startswith('010') and phone_number.isdigit():
                self.phonebook[input_name] = phone_number
                print(f"{input_name}의 전화번호가 추가되었습니다.")
            else:
                print("잘못된 전화번호 형식입니다. 다시 입력해주세요.")

    #2. 전화번호 검색
    def search_phone_number(self):
        input_name = input("검색할 이름을 입력하세요: ")
        if input_name in self.phonebook:
            print("검색 결과는 다음과 같습니다.\n"+"-"*40)
            print(f"{name_header:<{name_header_width}}{phone_number_header}\n"+"-"*40)
            print(f"{input_name:<{name_header_width}}: {self.phonebook[input_name]}")
        else:
            print("해당 이름이 없습니다.\n")

    # 3. 전화번호 수정
    def modify_phone_number(self):
        input_name = input("수정할 이름을 입력하세요: ")
        # 이름이 목록에 있는지 확인
        if input_name in self.phonebook:
            new_number = input("새 전화번호를 입력하세요 (예: 01011110000): ")
            # 전화번호 유효성 검사
            if len(new_number) == 11 and new_number.startswith('010') and new_number.isdigit():
                self.phonebook[input_name] = new_number
                print(f"{input_name}의 전화번호가 수정되었습니다.\n")
                print(f"수정된 전화번호는 {self.phonebook[input_name]}입니다.\n")
            # 전화번호가 잘못된 경우
            else:
                print("잘못된 전화번호 형식입니다.\n")
        else:
            print("해당 이름이 없습니다.\n")

    # 4. 전화번호 삭제
    def delete_phone_number(self):
        input_name = input("삭제할 이름을 입력하세요: ")
        if input_name in self.phonebook:
            del self.phonebook[input_name]
            print(f"{input_name}의 전화번호가 삭제되었습니다.\n")
        else:
            print("해당 이름이 없습니다.\n")

    # 5. 저장된 전화번호부 목록 확인
    def display_phonebook(self):
        print("전화번호부에 저장된 내용입니다.\n"+"-"*40)
        if self.phonebook:  # self.phonebook가 비어있지 않은 경우
            print(f"{name_header:<{name_header_width}}{phone_number_header}\n"+"-"*40)
            for name, phone_number in self.phonebook.items():
                print(f"{name:<{name_header_width}}: {self.phonebook[name]}")
        else:
            print("저장된 전화번호가 없습니다.\n")

    # 6. 형성한 파일 추출 기능
    def export_phonebook(self):
        # 추출할 파일 이름
        export_filename = input("저장할 파일의 이름을 작성하세요. (예: classA_export):") + ".txt"
        try:
            with open(export_filename, "w", encoding='utf-8') as export_file:
                export_file.write(f"{name_header:<{name_header_width}}{phone_number_header}\n"+"="*30+"\n")
                for name, phone_number in self.phonebook.items():
                    export_file.write(f"{name:<{name_header_width}}{phone_number}\n")
            print(f"전화번호부가 \'{export_filename}\'로 내보내졌습니다.\n")
        except Exception as e:
            print(f"파일 추출 중 오류 발생: {e}")

    def run(self):
        options = {
            '1': ('전화번호 추가', self.add_phone_number),
            '2': ('전화번호 검색', self.search_phone_number),
            '3': ('전화번호 수정', self.modify_phone_number),
            '4': ('전화번호 삭제', self.delete_phone_number),
            '5': ('저장된 전화번호 확인', self.display_phonebook),
            '6': ('전화번호부 내보내기', self.export_phonebook),
            '7': ('프로그램 종료', None)
        }
        
        while True:
            print("\n***** 전화번호부 관리 프로그램 *****")
            print("<Functions>")
            for num, (description, _) in options.items():
                print(f"{num}. {description}")

            user_choice = input("원하는 기능의 번호를 입력하세요(1-7): ")
            if user_choice in options:
                if user_choice == '7':
                    print("\n프로그램을 종료합니다.")
                    break
                print("~"*40)
                options[user_choice][1]()
                print("~"*40)
            else:
                print("*"*40)
                print("잘못된 입력입니다. (1-7) 사이 숫자를 입력해주세요.")
                print("*"*40)

# 프로그램 실행 
A = PhonebookManager("PhoneNumbers.txt")
A.run()
