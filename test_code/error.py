import sys

def main():
    try:
        result = 10 / 0  # 예시: 오류 발생 코드
    except Exception as e:
        error_message = str(e)
        with open("error.log", "a") as error_file:
            error_file.write("Error in python_script.py: {}\n".format(error_message))

if __name__ == "__main__":
    main()
