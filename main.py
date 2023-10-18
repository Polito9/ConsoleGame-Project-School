import os 
import random
#Global variables
continue_game = True
player1, player2 = "", ""
score_p1, score_p2 = 0, 0
questions = [] #Matrix where we are going to add the questions list[list]
answers = [] #Matrix where we are going to add the answers list[list[list]]
positions_selected = [] #Here we are going to save the positions selected by the players
#To shuffling things
questions_shuf = [] 
answers_shuf = [] 
shuffled_pos = [] 
#Dict that saves the name of the file for questions and answers 
categories = {"M": ['mate.txt','ans_mate.txt'], "C": ['cultura.txt','ans_cul.txt'], "O": ['musica.txt','ans_mus.txt']}

def ask_players_category(categories: dict) ->str:
    s_category = ""
    while True:
        print("\n\nEstas son las categorías disponibles para el juego: ")
        print("M: Matemáticas \nC: Cultura general \nO: Musica")
        s_category = input("Ingresa el código de la categoría a elegir: ")
        if (s_category in categories.keys()): #Detects if a category key is valid and if not it ask again
            break
        print("->Código no válido, intentalo nuevamente. \n\n")
    return s_category

#Using files
def obtain_questions(my_path : str) ->list: #Read the questions from the file
    path_ = os.getcwd() #Get the actual directory
    file = open(os.path.join(path_, my_path[0]), 'r', encoding='utf-8')
    questions = []
    for row in file: #Iterates each row
        question_aux = []
        question_aux = row.split("&") #Split separates the question and creates a list of the elements of that row
        question_aux[-1] = question_aux[-1][:-1]#Removes the \n
        questions.append(question_aux)
    file.close()
    return questions

def obtain_answers(my_path: str)-> list: #Read the answers from the file
    final_answers = []
    path = os.getcwd()
    file = open(os.path.join(path, my_path[1]), 'r', encoding='utf-8')
    for row in file: #We separate for each row
        answ_1aux = row.split("&")#Separate each question's anwers
        aux_row = []
        for q in answ_1aux: #Iterate in each question, q has a format of c|i|i|i
            answ_2aux = q.split("|") #Separate each element so we have each answer in a position in the list
            answ_1aux[-1] = answ_1aux[-1][:-1] #Removing the \n by slicing the last element of the list
            aux_row.append(answ_2aux) #We add the list of anwsers of each question in the row
        final_answers.append(aux_row)
    file.close()
    return final_answers

#Printing things
def print_map(questions:list, pos_s : list):
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
def ask_position(pos_selected:list)->list:#Validates if x, y is a valid position, if it is, it returns a mini_list[x, y]
    mini_list = []
    while True:
        try:
            x_t = input("\nIngresa la primera posición: ")
            y_t = input("Ingresa la segunda posición: ")
            if x_t == "end" or y_t == "end":
                return mini_list
            x = int(x_t) -1
            y = int(y_t) -1
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
def ask_print_answer(answers_shuf:list,pos_:list)->list:
    arr = ["A", "B", "C", "D"]
    answers = answers_shuf[pos_[0]][pos_[1]]
    correct = answers[0] #Saves the first position, that is always the correct one
    random.shuffle(answers)#Shuffles the new list of answers
    for i, answer in enumerate(answers):#Printing in the correct format
        print(arr[i]+")"+answer)
    while True:#Validates the answer
        user_answer = input("Respuesta: ")
        if user_answer.upper() in arr:
            if answers[arr.index(user_answer.upper())] == correct: #Validates the index of arr with the answers shuffled, and now it checks with correct
                return [True]
            else:
                return [False, correct, answers] #Returns the correct value, and the order of answers to not be shuffled when the other player anwers
        print("Respuesta no válida, intentalo nuevamente")
def ask_print_answer_noShuffle(answers: list, correct: str)->bool:
    arr = ["A", "B", "C", "D"]
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
def change_value(index:int)->int:
    if index == 0:
        return 1
    else:
        return 0

def main():
    global categories
    global questions
    global positions_selected
    global questions_shuf
    global answers_shuf
    global player1
    global player2
    global continue_game

    #Giving instructions: 
    print("----------------------------------------------------------------------")
    print("Bienvenido al juego: MARATÓN")
    print("\nPara elegir una pregunta: ")
    print("    1.Selecciona una casilla")
    print("    2.Busca el primer valor que aparece en la casilla y digítalo")
    print("    3.Digita el segundo valor que aparece en la casilla")
    print("\nPara responder digita A, B, C o D en el momento en el que te lo pidan")
    print("\nSi quieres terminar el juego, digita 'end' cuando te pidan alguna posición")
    print("Diviertanse!\n")
    input("Presiona Enter para continuar")
    
    while True:
        player1 = input("Ingresa el nombre del jugador 1: ")
        player2 = input("Ingresa el nombre del jugador 2: ")
        if len(player1)>0 and len(player2)>0:
            break
        else:
            print("Los nombres de usuario deben de contener al menos un caracter")
    
    #We ask the category to the players
    choosen_category = ask_players_category(categories)
    #We open the folder of the text acording to the selected category 
    path = categories[choosen_category]
    #We create the questions according to the path selected, and we save it in a list
    questions = obtain_questions(path)
    answers = obtain_answers(path)
    
    #Shuffling questions and answers
    questions_shuf = shuffle_questions(questions)
    answers_shuf = shuffle_answers(answers)
    scores = [0, 0] #Always the first value is the score of the player who starts
    #To define which player starts
    players = [player1, player2]
    i_playerS = random.randint(0, 1) 
    while continue_game:
        print("-----------------------------------------------------------------------------------------")
        print("Es el turno de <<"+players[i_playerS]+">>")
        #Start asking the player
        print_map(questions_shuf, positions_selected)
        #
        posxy = ask_position(positions_selected)
        if len(posxy) == 0:
            print("->Has decidido terminar el juego")
            break
        #Print question acording to positions selected
        print("\n"+questions_shuf[posxy[0]][posxy[1]])
        #Print answers according to positions
        is_correct = ask_print_answer(answers_shuf, posxy)
        if is_correct[0]:
            print("\nCORRECTO! Has sumado "+str(posxy[0]+1)+" puntos")
            scores[i_playerS] += posxy[0]+1
        else:
            print("\nIncorrecto, lo siento :(")
            correct_ans = is_correct[1]
            #Change the value to start stealing points from the other player
            i_playerS = change_value(i_playerS)
            print("\nAhora es el turno de robar de <<"+players[i_playerS]+">>")
            #Print question acording to positions selected
            print("\n"+questions_shuf[posxy[0]][posxy[1]])
            #Print answers according to positions
            is_correct = ask_print_answer_noShuffle(is_correct[2], correct_ans)
            if is_correct:
                print("\nCORRECTO! Has robado "+str(posxy[0]+1)+" puntos")
                scores[i_playerS] += posxy[0]+1
            else:
                print("\nIncorrecto, tu también has fallado :(")
                print("->La respuesta correcta era: "+correct_ans)
            i_playerS = change_value(i_playerS)

        print("PUNTOS ACUMULADOS DE "+players[i_playerS]+": "+str(scores[i_playerS]))
        #At the end we need to change the value of i_playerS
        i_playerS = change_value(i_playerS)
        print("PUNTOS ACUMULADOS DE "+players[i_playerS]+": "+str(scores[i_playerS]))
        if len(positions_selected) == 25:
            print("->No quedan mas preguntas disponibles")
            break

    #Showing the result:
    print("\n\n------------------------------------------------------------------------")
    print("RESULTADOS: ")
    print(players[i_playerS]+": "+str(scores[i_playerS])+" puntos")
    i_playerS = change_value(i_playerS)
    print(players[i_playerS]+": "+str(scores[i_playerS])+" puntos")
    if (scores[0]> scores[1]):
        print("El/La ganador/a es "+players[0])
    elif (scores[0]< scores[1]):
        print("El/La ganador/a es "+players[1])
    else:
        print("\nHa habido un empate")
main()