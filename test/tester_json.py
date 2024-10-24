import subprocess
import color_style as cs
import json
import filecmp

# Load the test suite configuration
with open('test_suite_config.json', 'r') as file:
    config = json.load(file)

# Set folder paths
test_cases_folder = str(config['test_cases_folders'])[2:-2]
src_folder = str(config['src_folders'])[2:-2]

# Dictionaries to  store the count of the number of test cases and the count of the number of test cases that pass
test_case_count = {}
test_case_pass_count = {}
for item in config['test_suite']:
    test_case_count[str(item)] = 0
    test_case_pass_count[str(item)] = 0

# Iterate through the test cases using the test_cases_folder path
for item in config['test_suite']:
    # Get the test case details
    code_file = item['code_file']

    for test_case in item['test_cases']:
        test_case_count[str(item)] += 1
        input_file = test_case['input_file']
        output_file = test_case['output_file']

        subprocess.run(['python3',src_folder + code_file], \
                    stdin = open(test_cases_folder + input_file, 'r'), \
                        stdout = open(test_cases_folder + "temp", 'w'))

        if(filecmp.cmp(test_cases_folder + "temp", test_cases_folder + output_file)):
            test_case_pass_count[str(item)] += 1
            print(f"Test case {input_file}/{output_file} for {code_file} " + cs.format('PASS', "passed."))
        else:
            print(f"Test case {input_file}/{output_file} for {code_file} " + cs.format('FAIL', "failed."))
    
    # Print the number of test cases that passed and the total number of test cases for each code file
    print(f"{item['code_file']} : {test_case_pass_count[str(item)]}/{test_case_count[str(item)]} test cases passed.")