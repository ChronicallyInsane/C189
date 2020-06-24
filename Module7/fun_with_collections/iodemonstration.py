"""
Author : Evan
Date: 6/22
Purpose: fileio

"""
import os as os


def main():
    get_student_info(name="Johnathan", course="memes")
    get_student_info(name="Tricia")
    get_student_info(name="Wololo")
    get_student_info(name="Stallman")
    for i in range(0, 5):
        get_student_info(name=input("enter name"))
        if input("Press Enter to continue else press 'n' to stop") == 'n':
            exit(0)
    read_from_file()


def write_to_file(*args, **kwargs):
    f = open('student_info.txt', 'w')
    for i in range(0, len(args)):
        f.write(str(args[i]))
        f.write("\t")
    for key, value in kwargs.items():
        f.write("{0} = {1}".format(key, value))
        f.write("\n")

    f.close()


def get_student_info(**kwargs):
    print("Enter scores as required, n to stop")
    scores =[]
    joined = []
    token='y'
    while token != 'n':
        token = input("Score?")
        scores.append(token)
    for key, value in kwargs.items():
        joined.append(("{0} = {1}".format(key, value)))
    for i in range(0, len(scores)):
        joined.append(scores[i])
    if input("Write to file? y/n") == 'y':
        write_to_file(joined)
    return joined


def read_from_file():
    file_name = "student_info.txt"
    file_name = input("file name?")
    file_dir = os.path.dirname(__file__)
    with open(os.path.join(file_dir, file_name), "r") as f:
        line = f.readlines()
        print(line)


if __name__ == '__main__':
    main()
