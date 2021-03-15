""" A script to write all the structs to the answer key. """
# For cmd line arguments
import sys
# For csv-ness
import csv
# For grabbing filenames
import re

"""
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

"""

inputfile = sys.argv[1]
# A place to store all the keys for the answer key.
bowl = []

# A function to parse all the keys from the input file.
def getKeys(inputfile):
    with open(inputfile, 'r', newline='') as csv_input:
        # create reader
        reader = csv.reader(csv_input)
        # skip the header row 'cuz we don't need it.
        csv_input.readline()
        # Columns from input should be ordered like this: class,method,path,injPoint,real
        for row in reader:
            answer_dict = {}
            answer_dict['class'] = row[0]
            answer_dict['method'] = row[1]
            answer_dict['path'] = row[2]
            answer_dict['injPoint'] = row[3]
            answer_dict['real'] = row[4]
            bowl.append(answer_dict)

# get the keys.
getKeys(inputfile)

def writeAnswerKey(bowl,inputfile):
    # Grab the package name
    package = re.search(r'([\w_\d]+)\.csv',inputfile)[1]
    # Make a file name from the input filename.
    filename = package + '.go'
    # Write the file.
    with open(filename, 'w', newline='') as output:
        # Write package name
        output.write('package ' + package + '\n\n')
        # Import-ant stuff
        output.write('import \t"github.com/whitehatsec/component-plugin-sdk-go/pkg/data"\n\n')
        # Declare the evidence struct
        output.write('type evidence struct {\n\tpath string\n\tmethod string\n\tclass string\n\tevent data.Event\n}\n\n')
        # Declare the testCase struct
        output.write('type testCase struct {\n\tclass string\n\tmethod string\n\tinjPoint string\n\treal bool\n\tdetections []evidence\n\tdetected bool\n}\n\n')
        # Open global declaration of answerKey map
        output.write('var answerKey = map[string]testCase{\n')
        # Define the answerKey struct for every testCase in the bowl list.
        for i in range(len(bowl)):
            output.write('\t"'+bowl[i]["path"]+'" : testCase{ class:"'+bowl[i]["class"]+'", method:"'+bowl[i]["method"]+'", injPoint:"'+bowl[i]["injPoint"]+'", real:'+bowl[i]["real"].lower()+', detections:[]evidence{}, detected:false},\n')
        # Close the declaration of the answer key map.
        output.write('}')
# Do the thing!
writeAnswerKey(bowl,inputfile)