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

4.c. Integrate forensics by modifying 5 Python methods of your choice. (20%)

4.d. Integrate continuous integration with GitHub Actions. (20%)

    - Added codacy-analysis.yaml file to the repository 
    
<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/5b504a17-c28a-4393-a44d-cce013fb7494">

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/da624da3-8155-494c-ad5a-c3ed95e18f8f">

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/52f13b88-e51a-402c-a615-d1e0dff4fdb2">


