# Team Name: Agile Avengers 

# Team Members: Elliott Baker, Lyna Capuano, and Jannatul Fhirdose


4.a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (20%)
    - Went to  .git/hooks/ in the repository
    - Rann cp pre-commit.sample pre-commit
    - Opened pre-commit
    - Edited pre-commit to run bandit and add found security weaknesses to a csv file

4.b. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (20%)

4.c. Integrate forensics by modifying 5 Python methods of your choice. (20%)

4.d. Integrate continuous integration with GitHub Actions. (20%)

Report your activities and lessons learned. Put the report in your repo as REPO.md (15%)
