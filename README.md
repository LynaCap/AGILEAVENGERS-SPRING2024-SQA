# Team Name: Agile Avengers 

# Team Members: Elliott Baker, Lyna Capuano, and Jannatul Fhirdose


4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (20%)

    - Went to  .git/hooks/ in the repository
    - Rann cp pre-commit.sample pre-commit
    - Opened pre-commit
    - Edited pre-commit to run bandit and add found security weaknesses to a csv file
    
Code Changed in pre-commit file: 

<img width="465" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/cfc97710-1cc5-4335-820f-8cfcd0c1bd2a">


Terminal Output after committing a change:

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/3385b7f1-de4d-415d-b83b-0c5fda573e44">


CSV file created:

<img width="468" alt="image" src="https://github.com/LynaCap/AGILEAVENGERS-SPRING2024-SQA/assets/125221326/acd158e0-362b-4b3f-b2e0-54d7c3f93f5d">



4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (20%)

4.c. Integrate forensics by modifying 5 Python methods of your choice. (20%)

4.d. Integrate continuous integration with GitHub Actions. (20%)

Report your activities and lessons learned. Put the report in your repo as REPO.md (15%)
