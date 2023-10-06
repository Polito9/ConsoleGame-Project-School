import os 
import random
#Visual inspection of how questions and answers are ordered.
'''
list = range(0,5)
hacer shuffle a list
[2, 4, 1, 0, 3]

para imprimir-> Vas acceder al valor de la posición, es decir 0
para comprobar respuestas -> Acceder al mismo valor, es decir (2) el cuál sigue ordenado.

questions = [["q11", "q12", "q13", "q14", "q15"], 
             ["q21", "q12", "q13", "q14", "q15"],
             ["q31", "q12", "q13", "q14", "q15"],
             ["q41", "q12", "q13", "q14", "q15"],
             ["q51", "q12", "q13", "q14", "q15"]]

            [1, 1] [1, 2] [1, 3] [1, 4] [1, 5]
            [2, 1] [2, 2] [2, 3] [2, 4] [2, 5]
            [3, 1] [3, 2] [3, 3] [3, 4] [3, 5]
            [4, 1] [4, 2] [4, 3] [4, 4] [4, 5]
            [5, 1] [5, 2] [5, 3] [5, 4] [5, 5]

answers = [[["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]]]
'''
player1, player2 = "p1", "p2"
questions = []
answers = []
positions_selected = [] #Here we are going to save the positions selected by the players
questions_shuf = []
answers_shuf = []
shuffled_pos = []
categories = {"M": ['mate.txt','ans_mate.txt'], "C": ['cultura.txt','ans_cul.txt'], "O": ['musica.txt','ans_mus.txt']}

def ask_players_category(categories: dict) ->str:
    s_category = ""
    while True:
        print("Estas son las categorías disponibles para el juego: ")
        print("M: Matemáticas \nC: Cultura general \nO: Musica")
        s_category = input("Ingresa el código de la categoría a elegir: ")
        if (s_category in categories.keys()):
            break
        print("->Código no válido, intentalo nuevamente. \n\n")
    return s_category

#Using files
def obtain_questions(my_path : str) ->list:
    path_ = os.getcwd()
    file = open(os.path.join(path_,'questions' , my_path[0]), 'r', encoding='utf-8')
    questions = []
    for row in file: #Iterates each row
        question_aux = []
        question_aux = row.split("&") #Split separates the question and creates a list of the elements of that row
        question_aux[-1] = question_aux[-1][:-1]#Removes the \n
        questions.append(question_aux)
    file.close()
    return questions

def obtain_answers(my_path: str)-> list:
    final_answers = []
    path = os.getcwd()
    file = open(os.path.join(path,'questions' , my_path[1]), 'r', encoding='utf-8')
    for row in file: #We separate for each row
        answ_1aux = row.split("&")#Separate each question's anwers
        aux_row = []
        for q in answ_1aux: #Iterate in each question, q has a format of c|i|i|i
            answ_2aux = q.split("|") #Separate each element so we have each answer in a position in the list
            answ_1aux[-1] = answ_1aux[-1][:-1] #Removing the \n
            aux_row.append(answ_2aux) #We add the list of anwsers of each question in the row
        final_answers.append(aux_row)
    
    return final_answers
#Printing things
def print_map(questions, pos_s : list):
    for i, row in enumerate(questions): #Iterates in questions getting the row and the index of the row
        for j in range(len(row)): #Iterates the index of the row
            if not ([i, j] in pos_s): #Validates if that is not a selected position
                print("["+str(i+1)+", "+str(j+1)+"] ", end="") #Prints adding 1 to the row and column
            else:
                print("[ XX ] ",end="") #The format in case the position have already been selected
        print("") #To go to the next line

#Shuffling things
def shuffle_questions(questions):
    for col in range(len(questions)):
        random_numbers = random.sample(range(5), 5)
        renglon = []
        for pos in random_numbers:
            renglon.append(questions[col][pos])
        questions_shuf.append(renglon)
        shuffled_pos.append(random_numbers)
    return(questions_shuf)

def shuffle_answers(answers):
    for col in range(len(answers)):
        random_numbers = shuffled_pos[col]
        renglon = []
        for pos in random_numbers:
            renglon.append(answers[col][pos])
        answers_shuf.append(renglon)
    return(answers_shuf)

#Ask position to the player
def ask_position(pos_selected:list)->list:
    mini_list = []
    while True:
        try:
            x = int(input("\nIngresa la posición x de la pregunta: ")) - 1
            y = int(input("Ingresa la posición y de la pregunta: ")) - 1
            mini_list = [x, y]
            if mini_list in pos_selected:
                print("Pregunta ya elegida, intentalo nuevamente\n")
            elif (x>=0 and x<5) and (y>=0 and y<5):#The condition is correct and we can return
                pos_selected.append(mini_list)
                break
            else:
                print("La pregunta no existe, intentalo nuevamente\n")
        except:
            print("Valor ingresado incorrectamente, intentalo nuevamente\n")
    return mini_list
#Show position accoring to the specified
def ask_print_answer(answers_shuf:list,pos_:list)->bool:
    arr = ["A", "B", "C", "D"]

    answers = answers_shuf[pos_[0]][pos_[1]]
    correct = answers[0]
    random.shuffle(answers)
    for i, answer in enumerate(answers):
        print(arr[i]+")"+answer)
    while True:
        user_answer = input("Respuesta: ")
        if user_answer.upper() in arr:
            if answers[arr.index(user_answer.upper())] == correct:
                return True
            else:
                return False
        print("Respuesta no válida, intentalo nuevamente")

def main():
    global categories
    global questions
    global positions_selected
    global questions_shuf
    global answers_shuf

    #We ask the category to the player
    choosen_category = ask_players_category(categories)
    #We open the folder of the text acording to the selected category 
    path = categories[choosen_category]
    #We create the questions according to the path selected, and we save it in a list
    questions = obtain_questions(path)
    answers = obtain_answers(path)
    
    #Shuffling questions and answers
    questions_shuf = shuffle_questions(questions)
    answers_shuf = shuffle_answers(answers)

    #Start asking the player
    print_map(questions_shuf, positions_selected)
    posxy = ask_position(positions_selected)
    #Print question acording to positions selected
    print("-----------------------------------QUESTION TIME-----------------------------------")
    print(questions_shuf[posxy[0]][posxy[1]])
    #Print answers according to positions
    is_correct = ask_print_answer(answers_shuf, posxy)
    print(is_correct)
main()