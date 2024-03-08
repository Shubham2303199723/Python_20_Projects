# A dictionary store all Questions and Answer
# will have a variable which tracks all score of player questions  
# loop through the dictionary using key value pairs
# display each question on display to allow them to answer
# tell them if they are right or wrong
# show final result in final 

Quiz = {"Questions1":{'question' : 'Where do you live?',
                      'answer': 'Indore'},
        "Questions2":{'question' : 'what are your skills',
                      'answer':'Python'},
        "Questions3":{'question' : 'Are you doing JOB?',
                      'answer' : 'Yes'}
        }

score = 0
for key, value in Quiz.items():
    print(value['question'])
    user_input = str(input("Write Your Answer here :- "))
    if user_input.lower() == value['answer'].lower():
        score = score + 1
    else:
        print("wrong Answer")
print("Your Score Is :- ", score)



