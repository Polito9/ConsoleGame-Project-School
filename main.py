import os 
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

answers = [[["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]]]
'''
questions = []
answers = []
positions_selected = [] #Here we are going to save the positions selected by the players
#questions\\mate.txt

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

def obtain_questions(my_path : str) ->list:
    path_ = os.getcwd()
    file = open(os.path.join(path_,'questions' , my_path[0]), 'r', encoding='utf-8')
    questions = []
    for row in file: #Iterates each row
        question_aux = []
        question_aux = row.split("&") #Split separates the question and creates a list of the elements of that row
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
            answ_2aux = row.split("|") #Separate each element so we have each answer in a position in the list
            aux_row.append(answ_2aux) #We add the list of anwsers of each question in the row
        final_answers.append(aux_row)
    
    return final_answers
    
    

def print_map(questions, pos_s : list):
    for i, row in enumerate(questions): #Iterates in questions getting the row and the index of the row
        for j in range(len(row)): #Iterates the index of the row
            if not ([i, j] in pos_s): #Validates if that is not a selected position
                print("["+str(i+1)+", "+str(j+1)+"] ", end="") #Prints adding 1 to the row and column
            else:
                print("[ XX ] ") #The format in case the position have already been selected
        print("") #To go to the next line

def main():
    global categories
    global questions
    global positions_selected
    #We ask the category to the player
    choosen_category = ask_players_category(categories)
    #We open the folder of the text acording to the selected category 
    path = categories[choosen_category]
    #We create the questions according to the path selected, and we save it in a list
    questions = obtain_questions(path)
    answers = obtain_answers(path)
main()