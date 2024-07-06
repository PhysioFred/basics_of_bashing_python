

#Numeric Comparisons
#> : Greater than
#< : Less than
#>= : Greater than or equal to
#<= : Less than or equal to
#== : Equal to
#!= : Not equal to

def number_comparisons():
    number1=16
    number2=16

    if number1 >= number2:
        print(f"{number1} is equal to or greater than {number2}")
    else:
        print(f"{number1} is not greater than {number2}")

number_comparisons()

#String Comparisons
# == : Equal to
# != : Not equal to
# > : Greater than (lexicographical order)
# < : Less than (lexicographical order)
# >= : Greater than or equal to (lexicographical order)
# <= : Less than or equal to (lexicographical order)
#Lexicographical order = alphabetical order
#It is case-sensitive and considers the ASCII values of the characters

def string_comparison():
    string1="Mr Anderson"
    string2="Agent Smith"

    if string1 > string2:
        print(f"{string1} is considered greater than {string2}")
    else:
        print(f"{string1} is less than {string2}")

string_comparison()


#File Comparisons
#os.path.exists(path) : Checks if a file or directory exists
#os.path.isfile(path) : Checks if the path is a regular file
#os.path.isdir(path) : Checks if the path is a directory
#os.access(path, os.R_OK) : Checks if the file is readable
#os.access(path, os.W_OK) : Checks if the file is writable
#os.access(path, os.X_OK) : Checks if the file is executable
#use  command `realpath <file/folder>` in linux to find the absolute file path
import os

file1="/home/fredunix/Fred/cloud_eng/python_bash/python/frodo.txt"
file2="~/Fred/cloud_eng/python_bash/python/fake_file"
directory1="/home/fredunix/Fred/cloud_eng/python_bash/python"
directory2="~/Fred/cloud_eng/python_bash/fake_path"

if os.path.exists(file1):
    print("got cha ass")
else:
    print("file not found")

if os.path.isfile(file1):
    print("it's a file")
else:
    print("it's not a file")

if os.path.isdir(directory1):
    print("it's a directory")
else:
    print("it's not a directory")