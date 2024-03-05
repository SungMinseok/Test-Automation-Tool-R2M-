import sys

def main():
    try:
        # 여기에 파이썬 코드를 작성하세요.
        result = 10 / 0  # 예시: 오류 발생 코드
    except Exception as e:
        error_message = str(e)
        with open("error.log", "a") as error_file:
            error_file.write("Error in python_script.py: {}\n".format(error_message))

if __name__ == "__main__":
    main()
