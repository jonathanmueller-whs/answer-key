Usage:

Copy the script to the folder containing your csv with test cases for the answer key you wish to create, 
or pass the full paths to the writeAnswerKey script and csv file respectivley.

THIS:

    $ python writeAnswerKey.py <test_case_file_name>.csv

OR THIS:

    $ python /path/to/writeAnswerKey.py /path/to/<test_case_file_name>.csv

The writeAnswerKey script is designed to take the second argument from the command line as an input file, parse 
the content of the input file, and output a Go file that contains a map with all the test cases.
The exepcted input type is a csv with the following columns for each test case that the answer key will contain:

    • class
    • method
    • path
    • injPoint
    • real

The script will iterate through each row of the csv, parsing the values of the columns from left to right. 
The columns in the csv, therefore, must be ordered from left to right like this:

    class,method,path,injPoint,real