import mysql.connector as connection
mydb = connection.connect(host="127.0.0.1", user="root", password="", database="mydatabase")

import random
import time
mycursor = mydb.cursor()

class Exam:
    def __init__(self):
        self.questions = ["What is today's date", "Who is sodeeq", "president of naija", "Head of SQI", "Who is Loki"]
        self.options = ["A: Tuesday B: Monday", "A: Man B: Python Student", "A: Peter Obi B: Tinubu", "A: Aderinto B: Wunmi", "A: Thor's brother B: He who remains"]
        self.answers = ["b", "b", "b", "a", "a"]
        self.score = 0
        self.cbt()
        mydb.commit()

    def cbt(self):
        action = input("""
              Welcome to the SCHOOL
              ENTER 1 to login
              ENTER 2 to register 
              """)
        if action == "1": 
            self.login()
        elif action == "2":
            self.register()
        else: 
            print("Wrong Input, try again")
            time.sleep(3)
            self.cbt()
        

    def test(self): 
        for i in self.questions:
            index = self.questions.index(i)
            print(self.questions[index])
            print(self.options[index])
            user_ans = input("choose the correct answer ")
            answer = self.answers[index]
            if user_ans == answer:
                print("Correct")
                self.score += 20
            else:
                print("Wrong")
                self.score += 0
        
        time.sleep(2)
        print(f"Your score is {self.score}")
        upd = f"update student set score = {self.score} where matric = {self.mat}"
        dex = f"update student set exam_done = 'YES' where matric = {self.mat}"
        mycursor.execute(upd)
        mycursor.execute(dex)
        mydb.commit()
        self.grade()

        
    def register(self):
        query = "insert into student(fname, lname, matric, password, address, gender, score, state_of_origin, course, duration, admission_status, exam_done) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        gen = random.randint(11111,55555)
        fname = input("What is the first name: ")
        lname = input("what is the last name: ")
        matric = gen
        password = input("Set your password: ")
        address = input("what is your address: ")
        gender = input("what is your gender: ")
        score = 0
        origin = input("what is your state of origin: ")
        course = input("what course would you like to study: ")
        info = (fname, lname, matric, password, address, gender, score, origin, course, '4years', 'NO', 'NO')
        mycursor.execute(query, info) 
        mydb.commit()
        print(f"Welcome {fname} {lname}, you have successfully registered & your matric number is {matric}.")
        time.sleep(2)
        self.login()

    def login(self):
        self.mat = input("Enter your matric number: ")
        self.acts = f"select * from student where matric = {self.mat}"
        mycursor.execute(self.acts)
        self.user = mycursor.fetchone()
        # print(self.user)
        if self.user is None:
            print("Invalid Matric Number, try again")
            self.login()
        self.passw = input("Enter your password: ")
        if self.passw in self.user[4]:
            print("Login Successful")
            self.checkTest()
        else:
            print("Incorrect Password, please try again")
            time.sleep(2)
            self.login()

    def checkTest(self):
        if self.user[12] == 'NO':
            self.test()
        elif self.user[12] == "YES":
            print("\nYou have taken the test, this is your letter")
            time.sleep(2)
            self.letter()

    def grade(self):
        if self.score >= 60:
            print("Good job, you are admitted. Hold on for your admission letter")
            drp = f"update student set admission_status = 'YES' where matric = {self.mat}"
            mycursor.execute(drp)
            mydb.commit()
            time.sleep(3)
            self.letter()
        elif self.score < 60:
            print("U no sabi o, Hold on for your rejection letter")
            time.sleep(3)
            self.letter()

    def letter(self):
        self.acts = f"select * from student where matric = {self.mat}"
        mycursor.execute(self.acts)
        self.user = mycursor.fetchone()
        mydb.commit()
        # print(self.user[11])
        # print(self.user[7])
        if self.user[7] >= 60:
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'w')
            myfile.write(f"""
                        
                Dear Mr/Mrs {self.user[1]} {self.user[2]}

                                    ADMISSION LETTER
                Wow! Your performance blew us away. We're over the moon to offer you admission. 
                Your dedication and talent shone throughout the test. 
                We're excited to see you grow and achieve even more in our community. 
                Welcome aboard! This is just the beginning of your amazing journey.

                The details of your admission is as follows:
                Name is {self.user[1]} {self.user[2]}, you live at {self.user[5]} and you are from {self.user[8]}.
                Your course of study is {self.user[9]} which would span for {self.user[10]} and your matric number is {self.user[3]}.


                                                                                        Yours Sincerely,
                                                                                        Ogunmepon Razaq.
                                                                                        Registrar, UI.
                """)
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
            print(myfile.read())
            myfile.close()
        elif self.user[7] < 60:
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'w')
            myfile.write(f"""
                        
                Dear Mr/Mrs {self.user[1]} {self.user[2]}

                                    ADMISSION LETTER
                Wow! Your performance blew us away. We're over the moon to see you fail. 
                Your dedication and talent did not show throughout the test. 
                We're excited not to see you grow and not achieve even more in our community. 
                Bye bye! This is just the beginning of your PREDICAMENT.

                The details of your REJECTED admission is as follows:
                Name is {self.user[1]} {self.user[2]}, you live at {self.user[5]} and you are from {self.user[8]}.


                                                                                        Yours Sincerely,
                                                                                        Ogunmepon Razaq.
                                                                                        Registrar, UI.
                """)
            myfile = open('/Users/sokebiz/Desktop/Python/Class/letter.txt', 'r')
            print(myfile.read())
            myfile.close()
        exit()

Exam()
