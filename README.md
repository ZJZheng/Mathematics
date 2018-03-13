# Mathematics program for K-12 Education
## Goal of the Project: <br />
The project aims to create a prototype program for K-12 mathematics education. In more detail, the program is designed to help students finding out his or her weaknesses in mathematics by randomly generating quiz questions for students to answer. <br />

## Download: <br />
Download the 'Mathematics' file in this repository. <br />
Extract the download zip file and double click 'Mathematics.exe' to run the program. <br />

## How to Use: <br />
  1. User picks a type of questions and then pick the number of questions to start a quiz. There are four question types in the current prototype program. They are: “Arithmetic Questions”, “Fraction Questions”, “Derivative Questions”, and “Matrix Questions”. <br />
  2. The user needs to type in answers in the program and press “Enter” on keyboard to submit the answer. <br />
  3. If the answer is correct, the user would get 1 point. If the answer is wrong, the user gets 0 point, and the correct answer will be shown on the screen for user’s reference. <br />
  4. After the quiz, the total score and accuracy would be shown on the screen. <br />
  5. At this stage, the user can choose to leave the program or continue. If to leave, the program will be closed automatically. If to continue, the user needs to pick a question type again to start a new quiz. <br />
  6. After several quizzes are taken, the user shall get a sense of where his or her weaknesses are in mathematics. <br />
  7. The program can be used for self-learning or for in-class/take-home quizzes/exams. <br />
  8. The program does not use any database. The problems are generated randomly by the program. Thus, each time the user will meet new problems. <br />
  9. For the Matrix Inversion problems, all matrices generated are guaranteed to be invertible.  <br />

## Make a change of the program: <br />
  1. Change the codes in 'Mathematics.py' <br />
  2. Install pyinstaller, a python package to generate your new .exe file. Link: https://www.pyinstaller.org/  <br />
     In command prompt (Windows): <br />
        ```
        pip install pyinstaller
        ```
  3. In command prompt (Windows) under the directory of 'Mathematics.py', type: <br />
        ```
        pyinstaller Mathematics.py
        ```
  4. After generation, open your new program "Mathematics.exe" inside the "dist" folder. You can create a shortcut of it, so you can access the program easily in the future. <br />
