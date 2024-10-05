class PhonebookManager:

    def make_phonebook_dict(self):
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

    def __init__(self, filename):
        self.filename = filename
        self.phonebook = {}
        self.phonebook = self.make_phonebook_dict()

    # 전화번호부 관리 프로그램의 기능을 수행하는 메소드
    # 1. 전화번호 추가
    def add_phone_number(self):
        input_name = input("이름을 입력하세요: ")
        if input_name in self.phonebook:
            print("이미 전화번호부에 등록되어 있는 이름입니다!")
            print(f"{input_name}: {self.phonebook[input_name]}")
            print("전화번호를 수정하고 싶다면, [3. 전화번호 수정] 기능을 사용하세요.")
        else:
            phone_number = input("전화번호를 입력하세요 (예: 01011110000): ")
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
            print(f"{input_name}: {self.phonebook[input_name]}")
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
        print("\n저장된 전화번호 목록:")
        if self.phonebook:  # self.phonebook가 비어있지 않은 경우
            for name, phone_number in self.phonebook.items():
                print(f"{name}: {phone_number}")
        else:
            print("저장된 전화번호가 없습니다.\n")

    # 6. 형성한 파일 추출 기능
    def export_phonebook(self):
        # 추출할 파일 이름
        export_filename = input("저장할 파일의 이름을 작성하세요. (예: classA_export):")
        try:
            with open(export_filename, "w", encoding='utf-8') as export_file:
                export_file.write("NAME\t\tPHONE NUMBER\n")
                export_file.write("=" * 30 + "\n")
                for name, phone_number in self.phonebook.items():
                    export_file.write(f"{name}\t\t{phone_number}\n")
            print(f"전화번호부가 \'{export_filename}.txt\'로 내보내졌습니다.\n")
        except Exception as e:
            print(f"파일 추출 중 오류 발생: {e}")

    def run(self):
        while True:
            print("\n전화번호 관리 프로그램")
            print("원하는 기능의 번호를 선택하세요.")
            print("1. 전화번호 추가")
            print("2. 전화번호 검색")
            print("3. 전화번호 수정")
            print("4. 전화번호 삭제")
            print("5. 저장된 전화번호 확인")
            print("6. 전화번호부 내보내기")
            print("7. 프로그램 종료")

            choice = input("원하는 작업을 선택하세요 (1-7): ")

            if choice == '1':
                self.add_phone_number()
            elif choice == '2':
                self.search_phone_number()
            elif choice == '3':
                self.modify_phone_number()
            elif choice == '4':
                self.delete_phone_number()
            elif choice == '5':
                self.display_phonebook()
            elif choice == '6':
                self.export_phonebook()
            elif choice == '7':
                print("\n프로그램을 종료합니다.")
                break
            else:
                print("=" * 50)
                print("잘못된 입력입니다.\n원하시는 기능의 숫자를 입력해주세요.(1~6).")
                print("=" * 50)


# 프로그램 실행

fileList = ["PhoneNumbers.txt",]
A = PhonebookManager(fileList[0])
A.run()