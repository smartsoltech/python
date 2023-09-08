
# Импорт тестовых функций из соответствующих файлов
from rectangle_test_code import run_rectangle_test
from student_test_code import run_student_test
from matrix_test_code import run_matrix_test

def main():
    while True:
        print("Select the test to run:")
        print("1: Rectangle Test")
        print("2: Student Test")
        print("3: Matrix Test")
        print("0: Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            run_rectangle_test()
        elif choice == '2':
            run_student_test()
        elif choice == '3':
            run_matrix_test()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
