'''
Imagine the first day of university for a freshman named Alex.
Alex is excited but also overwhelmed by the vast campus, numerous courses,
and the sea of new faces. To aid new students like Alex, the university's IT
department has developed a personalised chatbot. This chatbot, named
"UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and
age. Based on this input, UniBuddy offers a personalised greeting.
The chatbot also offers a feature where Alex can input specific queries and
UniBuddy responds with relevant information, all while adhering to a friendly tone,
using string transformation methods to ensure the responses feel personalised
and engaging
'''

# initialise message for first time start
print('''
Welcome to UniBuddy! 

I'm your all-in-one app, here to make your freshman journey a bit easier to navigate.

Please enter your credentials below to help us get started.
''')

while True:
    user_name = input("Please enter your first name: ").capitalize()
    user_age = input("Please enter your age: ")
    fav_colour = input("Please enter your favourite colour: ").capitalize()

    # check that user_name contains only letters, if it doesn't, provide a warning and go back to the questions.
    if not user_name.isalpha():
        print("You must only enter characters for your name, please re-enter your credentials below.")

    # check that user_age contains only numbers, if it doesn't, provide a warning and go back to the questions.
    if not user_age.isnumeric():
        print("You must only enter numbers for your age, please re-enter your credentials below.")

    # check that fav_colour contains only letters, if it doesn't provide a warning and go back to the questions.
    if not fav_colour.isalpha():
        print("You must only enter characters for your favourite colour, please re-enter your credentials below.")

    # check that fav_colour is one of the colours there are recommendations on. If not, provide a warning and go back to questions.
    if (fav_colour != "Blue"
            and fav_colour != "Red"
            and fav_colour != "Purple"
            and fav_colour != "Pink"
            and fav_colour != "Green"
            and fav_colour != "Black"
            and fav_colour != "Yellow"
            and fav_colour != "Orange"):
        print("""
            Unfortunately I don't recognise your favourite colour in order to give you some recommendations.
            You have either spelt it incorrectly or you it isn't one of the primary colours! 
            Please enter your details in again if you would like some recommendations.
            """)

    # if user_name, user_age and fav_colour are all in the correct format, print personalised welcome message
    if user_name.isalpha() and user_age.isnumeric() and fav_colour.isalpha():
        print(f"""
        Welcome {user_name}! I hope you're enjoying your university experience so far.
        Based on your age ({user_age} years old) and your favourite colour ({fav_colour}), 
        I'm going to suggest some activities!
        """)
        break

# provide university recommendations based on the student's fav_colour
if fav_colour == "Blue":
    print("""
          I see you like the colour Blue. You could try out these activities at the university:
          1. Our swimming club
          2. Our mountaineering club
          3. Our bird-watching society
          All clubs and societies will be meeting on Saturday at 5pm.
          """)

elif fav_colour == "Red":
    print("""
              I see you like the colour Red. You could try out these activities at the university:
              1. Our football club
              2. Our clubbing society
              3. Our speed-racing society
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Purple":
    print("""
              I see you like the colour Purple. You could try out these activities at the university:
              1. Our drawing society
              2. Our historical research society
              3. Our hot air balloon club
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Pink":
    print("""
              I see you like the colour Pink. You could try out these activities at the university:
              1. Our cocktail-making society
              2. Our crafting society
              3. Our dancing club
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Green":
    print("""
              I see you like the colour Blue. You could try out these activities at the university:
              1. Our gardening society
              2. Our hiking club
              3. Our panto society
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Black":
    print("""
              I see you like the colour Blue. You could try out these activities at the university:
              1. Our vampire-lovers club
              2. Our historical church visiting society
              3. Our DnB society
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Yellow":
    print("""
              I see you like the colour Blue. You could try out these activities at the university:
              1. Our lacrosse club
              2. Our sponge-bob square pants society
              3. Our art appreciation society
              All clubs and societies will be meeting on Saturday at 5pm.
              """)
elif fav_colour == "Orange":
    print("""
              I see you like the colour Blue. You could try out these activities at the university:
              1. Our sunset chasers society
              2. Our rugby club
              3. Our decoding society
              All clubs and societies will be meeting on Saturday at 5pm.
              """)

# provide freshers' week information based on the user_age
user_age = int(user_age)
if user_age < 18:
    print("""
    There is also an underage freshers event happening Friday evening in the Junior Common Room at 8pm. 
    See you there :)
    """)

elif user_age >= 18 and user_age<= 30:
    print("""
    There is also a freshers event happening Friday evening at the University Bar at 8pm.
    See you there :)
    """)

elif user_age > 30:
    print("""
    There is also a freshers event for mature students this Friday evening at the Jolly Sportsman at 8pm.
    See you there :)
    """)

# list frequently asked questions and matching answers
faq_questions = [
    "when will my lectures be starting",
    "where is the student information office",
    "where is the fees office",
    "what are the opening times of the university bar",
    "when is the first freshers event",
    "who is my student mentor",
    "where is the student counselor located"
    "where can i find more information about my course"
]

faq_answers = [
    "All lectures will be starting on Monday 15th September. For more information go to the Uni gateway and click on your subject.",
    "The student information office is located by reception. Please click here to see the university map...",
    "The fees office is located in the Finance building. Please click here to see the university map...",
    "The university bar is open from 1pm to 2am, 7 days a week. Enjoy!",
    "The first freshers event is taking place this Friday. For more information go to the Uni gateway and click on 'Freshers Week'.",
    "Your student mentor will be emailing you this week. If you don't receive anything, please go to your subject office.",
    "The student counselor is located in the Wellbeing Office. Please click here to see the university map...",
    "You can find more information about your course by going to the Uni gateway and clicking on your subject."
]

# create a loop that keeps looping while the user wants to ask a question.
while True:
    ask_question = input("Would you like to ask a question? (Y/N) ").upper()
    if ask_question != "Y" and ask_question != "N":
        print("You haven't entered Y or N, please try again.")
    elif ask_question == "N":
        print("OK, nice to meet you, have a great freshers' week!")
        break
    # if the user wants to ask a question, ask them to enter it and check this in the faq_questions
    elif ask_question == "Y":
        question = input("Great, I'm happy to answer your question! Ask away: ").lower()
        question = question.strip("?")
        question = question.strip()
        # if the question appears in the faq_questions, print the matching faq_answers
        if question in faq_questions:
            question_index = faq_questions.index(question)
            print(faq_answers[question_index])
        else:
            print('''
            I'm sorry, your question doesn't appear in our frequently asked questions.
            Please go the Student Information Office located behind the student bar.
            Click here to see the University Map...
            ''')


