import os 
#Visual inspection of how questions and answers are ordered.
'''
questions = [["q11", "q12", "q13", "q14", "q15"], 
             ["q11", "q12", "q13", "q14", "q15"],
             ["q11", "q12", "q13", "q14", "q15"],
             ["q11", "q12", "q13", "q14", "q15"],
             ["q11", "q12", "q13", "q14", "q15"]]

answers = [[["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]],
          [["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"], ["c1", "in1", "in2", "in3"]]]
'''
#positions_selected = [] #Here we are going to save the positions selected by the players
#questions\\mate.txt

categories = {"M": 'mate.txt', "C": 'cultura.txt', "O": 'musica.txt'}

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

def obtain_questions(my_path) ->list:
    path_ = os.getcwd()

    file = open(os.path.join(path_,'questions' , my_path), 'r', encoding='utf-8')
    questions = []
    for row in file:
        question_aux = []
        question_aux = row.split("&") #Split separates the question and creates a list of the elements of that row
        questions.append(question_aux)
    return questions


def main():
    global categories
    global questions
    #We ask the category to the player
    choosen_category = ask_players_category(categories)

    #We open the folder of the text acording to the selected category 
    path = categories[choosen_category]
    questions = obtain_questions(path)

main()