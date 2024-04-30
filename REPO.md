4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (20%)

    - Went to .git/hooks/ in the repository
    - Ran cp pre-commit.sample pre-commit
    - Opened pre-commit
    - Edited pre-commit to run bandit and add found security weaknesses to a csv file
    
Code Changed in pre-commit file: 

<img width="465" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/cfc97710-1cc5-4335-820f-8cfcd0c1bd2a">


Terminal Output after committing a change:

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/3385b7f1-de4d-415d-b83b-0c5fda573e44">


CSV file created:

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/acd158e0-362b-4b3f-b2e0-54d7c3f93f5d">


Lessons Learned: Learned how to build a Git Hook to help automatically identify security weaknesses. Also learned about the tools that can be used to identify security weaknesses. Specifically, we are using the tool, Bandit, to identify security weaknesses since the given file contains Python scripts.



4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (20%)

## Activities Performed
### Fuzz Test Creation:
Method Selection: Identified critical methods within the project that were suitable candidates for fuzz testing based on their complexity and exposure to potential bugs.
Fuzz Test Implementation: Developed a fuzz.py script using the Hypothesis library, which is designed to automatically generate test inputs to simulate edge cases and unexpected conditions. Selected methods from different modules like py_parser.py and lint_engine were targeted.
### GitHub Actions Workflow Setup:
Automation Script: Created a YAML file for a GitHub Actions workflow named fuzzing.yml, which defines the steps to install dependencies, set the appropriate environment variables, and execute the fuzz.py script upon every push and pull request to the feature/fuzzing branch.
Environment Configuration: Configured PYTHONPATH in the GitHub Actions workflow to ensure that the testing environment correctly mirrors the local development setup, allowing imports and modules to be located without errors.
### Execution and Monitoring:
Continuous Integration: Monitored the execution of the fuzz tests through GitHub Actions, adjusting configurations as necessary to handle failures and ensure reliable execution.
Results Review: Checked logs and outcomes from the GitHub Actions runs to verify that the fuzz tests were performing as expected, catching errors, and generating reports.

4.c. Integrate forensics by modifying 5 Python methods of your choice. (20%)

4.d. Integrate continuous integration with GitHub Actions. (20%)

    - Added codacy-analysis.yaml file to the repository 

Codacy Analysis CLI:
    
<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/5b504a17-c28a-4393-a44d-cce013fb7494">


Run Codacy Analysis CLI:

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/da624da3-8155-494c-ad5a-c3ed95e18f8f">


<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/52f13b88-e51a-402c-a615-d1e0dff4fdb2">


Lessons Learned: Learned how to use the Codacy tool to integrate code changes with continuous integration and also check for quality concerns with static analysis. 


