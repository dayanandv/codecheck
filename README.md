CodeCheck is a testing framework tailored for undergraduate programming students. It allows users to run test cases against their Python code submissions, providing immediate feedback on correctness. With support for input-output pairs and various configuration options, CodeCheck helps students validate their solutions and improve their coding skills.

File Structure:

    ./src/                  # Source code files
        ├── list_access.py
        ├── list_changing_value.py
        └── list_slicing_iterating.py
    
    ./test/                 # Test files
        ├── __pycache__/    # Compiled Python files
        ├── color_style.py   # Optional styling for test output
        ├── test_cases/      # Input and output test cases
        │   ├── TC_1.in
        │   ├── TC_1.1.out
        │   ├── TC_1.2.out
        │   ├── TC_1.3.out
        │   ├── TC_2.in
        │   └── TC_2.1.out
        ├── tester.py        # Main testing script
        ├── tester_json.py    # JSON-based testing script
        └── test_suite_config.*  # Configuration files

Usage:

 1. Clone the repository:

        git clone https://github.com/dayanandv/code_check.git

 2. Place your source code files in the src folder.
 3. Define your test cases in the test/test_cases directory, using .in files for inputs and .out files for expected outputs.
 4. Run the testing script:

        python test/tester.py
 5. Review the output for pass/fail results and feedback.
