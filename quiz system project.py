import time
allquestions={"python":{
    1: {'question': 'What is python?','option1': 'dynamically typed','option2': 'interpreted','option3': 'compiler','option4': '1&2','answer': '4'},
    2: {'question': "What is the output of print(3 * '7')",'option1': '21','option2': '777','option3': '73','option4': 'error','answer': '2'}},
              "mysql":{1: {'question': 'What does SQL stand for?','option1': 'Structured Question Language','option2': 'Structured Query Language','option3': 'Simple Query Language','option4': 'Standard Query Language','answer': '2'},
                       2: {'question': 'Which keyword is used to remove a table from a database?','option1': 'REMOVE','option2': 'DELETE','option3': 'DROP','option4': 'ERASE','answer': '3'}}}
userdetails={"python":{},"mysql":{}}
adminid="sowmya"
adminpassword="123"
while True:
    print("1.Admin login")
    print("2.User login")
    print("3.Exit")
    choose=input("Enter your choice:")
    if choose=="1":
        admin_id=input("Enter admin id:")
        admin_password=input("Enter admin password:")
        if admin_id==adminid and admin_password==adminpassword:
            print("Admin login succesfully")
            print()
            while True:
                print("-----Admin menu-----")
                print("1.add question")
                print("2.modify question")
                print("3.delete question")
                print("4.view all questions")
                print("5.view all users")
                print("6.view top 3 scores")
                print("7.logout")
                admin=input("choose one:")
                if admin=="1":
                    print("1.python")
                    print("2.mysql")
                    language=input("which language do you want:")
                    if language=="1":
                        technology=allquestions["python"]
                    elif language=="2":
                        technology=allquestions["mysql"]
                    else:
                        print("Invalid language")
                        break 
                    question=input("enter a question:")
                    option1=input("enter option1:")
                    option2=input("enter option2:")
                    option3=input("enter option3:")
                    option4=input("enter option4:")
                    answer=input("enter correct option:")
                    a=len(technology)
                    if a==0:
                        technology[1]={"question":question,"option1":option1,"option2":option2,"option3":option3,"option4":option4,"answer":answer}
                        print("Question added sucessfully") 
                    else:
                        technology[len(technology)+1]={"question":question,"option1":option1,"option2":option2,"option3":option3,"option4":option4,"answer":answer}
                        print("Question added sucessfully")
                        print()
                elif admin == "2":
                    print("1.python")
                    print("2.mysql")
                    language = input("Enter a language: ")

                    if language == "1":
                        technology = allquestions["python"]
                    elif language == "2":
                        technology = allquestions["mysql"]
                    else:
                        print("Invalid language")
                        break  

                    modify_question = int(input("Enter a question number to modify: "))

                    if modify_question in technology:
                        q = technology[modify_question]
                        print(f"Current Question {modify_question}:")
                        print(f"Question: {q['question']}")
                        print(f"Option1: {q['option1']}")
                        print(f"Option2: {q['option2']}")
                        print(f"Option3: {q['option3']}")
                        print(f"Option4: {q['option4']}")
                        print(f"Answer: {q['answer']}")
                        

                        print("Enter new one:")

                        new_question = input("Enter question: ") or q['question']
                        new_option1 = input("Enter option1: ") or q['option1']
                        new_option2 = input("Enter option2: ") or q['option2']
                        new_option3 = input("Enter option3: ") or q['option3']
                        new_option4 = input("Enter option4: ") or q['option4']
                        new_answer = input("Enter answer: ") or q['answer']

                        technology[modify_question] = {"question": new_question,"option1": new_option1,"option2": new_option2,"option3": new_option3,"option4": new_option4,"answer": new_answer}

                        print("Question modified successfully.")
                    else:
                        print("Question number not found in selected language.")
                        print()


                   
                elif admin=="3":
                    delete_question=int(input("enter a question to delete:"))
                    print("1.python")
                    print("2.mysql")
                    language=input("enter a language:")
                    if language=="1":
                        allquestions["python"].pop(delete_question)
                        print("question deleted sucessfully")
                    elif language=="2":
                        allquestions["mysql"].pop(delete_question)
                        print("question deleted sucessfully")
                    else:
                        print("please choose correct one")
                        print()
                elif admin == "4":
                    print("All Questions:")
                    for language, questions in allquestions.items():
                        print(f"Language: {language.upper()}")
                        for qid, qdata in questions.items():
                            print(f"Q{qid}: {qdata['question']}")
                            print(f"Option1: {qdata['option1']}")
                            print(f"Option2: {qdata['option2']}")
                            print(f"Option3: {qdata['option3']}")
                            print(f"Option4: {qdata['option4']}")
                            print(f"Answer : {qdata['answer']}")
                           

                elif admin == "5":
                    print("All Users and Their Quiz Results:")
                    for lang, users in userdetails.items():
                        print(f"Language: {lang.upper()}")
                        for uid, records in users.items():
                            print(f"  User ID: {uid}, mobile No:{user_mobile_no}")
                            for rec in records:
                                print(f"    Score: {rec['score']}, Time Taken: {round(rec['time_taken'], 2)}s")
                                print()
                elif admin == "6":
                    print("Top 3 Scores:")
                    for lang in userdetails:
                        print(f"{lang.upper()}:")
                        all_scores = []
                        for uid in userdetails[lang]:
                            for record in userdetails[lang][uid]:
                                all_scores.append({
                                    "user_id": record["user_id"],
                                    "user_mobile_no": record["user_mobile_no"],
                                    "score": record["score"],
                                    "time_taken": record["time_taken"]
                                })

                        if not all_scores:
                            print(" No records found.")
                            continue

                        top_scores = sorted(all_scores, key=lambda x: (-x["score"], x["time_taken"]))[:3]

                        i = 1  
                        for rec in top_scores:
                            print(f"  {i}. User: {rec['user_id']}, mobile no: {rec['user_mobile_no']}, Score: {rec['score']}, Time: {round(rec['time_taken'], 2)}s")
                            i += 1
                        print()

                elif admin=="7":
                    break
            else:
                print("Invalid")
   
    elif choose=="2":
            print("-----User menu-----")
            user_id=input("enter user_id: ")
            while True:
                s=["9","8","7","6"]
                user_mobile_no=input("enter user_mobile_no: ")
                if len(user_mobile_no)==10 and user_mobile_no.isdigit() and user_mobile_no[0] in s:
                    print("User login sucessfull")
                    break
                else:
                    print("enter correct mobile_no")
                    continue
                    print()
            user_choice=input("Do you want to take the quiz(yes/no):")
            if user_choice=="yes":
                print("1.python")
                print("2.mysql")
                language=input("select language")
                if language == "1":
                    selected_questions = allquestions["python"]
                elif language == "2":
                    selected_questions = allquestions["mysql"]
                else:
                    print("Invalid language")
                    continue
                score = 0
                question_number = 1
                correct_answer=0
                start=time.time()
                for qid in selected_questions:
                    q = selected_questions[qid]
                    print(f"Q{question_number}:{q['question']}")
                    print(f"1.{q['option1']}")
                    print(f"2.{q['option2']}")
                    print(f"3.{q['option3']}")
                    print(f"4.{q['option4']}")
                    user_answer = input("Enter the correct option: ")
                    if user_answer == q['answer']:
                        print("Correct")
                        score += 5
                        correct_answer+=1
                    else:
                        print("Incorrect.")
                        score-=2
                    question_number += 1

                end=time.time()
                print(f"Your total score: {score}")
                print("total number of questions:",len(selected_questions))
                print(f"Number of correct answers: {correct_answer}")
                print("Time taken to complete quiz is:",end-start)
                print()
                language_key = "python" if language == "1" else "mysql"
                quiz_result = {"user_id": user_id,"user_mobile_no": user_mobile_no,"score": score,"time_taken": end - start}
                if user_id not in userdetails[language_key]:
                    userdetails[language_key][user_id] = []
                userdetails[language_key][user_id].append(quiz_result)
            elif user_choice=="no":
                continue
            else:
                print("please choose the correct option")
    elif choose=="3":
        print("Thank you for participating in the quiz!")
        break
    else:
        print("please choose the correct option")
