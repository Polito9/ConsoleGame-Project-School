#Provitional creation of questions an answers, we're gonna actually create them by reading files
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

#positions_selected = [] #Here we are going to save the positions selected by the players

categories = {"M": "'questions\\mate.txt'", "C": "'questions\\cultura.txt'", "O": "'questions\\otra.txt'"}

def ask_players_category(categories: dict) ->str:
    s_category = ""
    while True:
        print("Estas son las categorías disponibles para el juego: ")
        print("M: Matemáticas \nC: Cultura general \nO: Otro")
        s_category = input("Ingresa el código de la categoría a elegir: ")
        if (s_category in categories.keys()):
            break
        print("->Código no válido, intentalo nuevamente. \n\n")
    return s_category

def obtain_questions(path: str) ->list:
    file = open(path, 'r')
    questions = []
    for row in file:
        question_aux = []
        question_aux = row.split("&") #Split separates the question and creates a list of the elements of that row
        questions.append(question_aux)
    
    return questions


def main():
    global categories
    #We ask the category to the player
    choosen_category = ask_players_category(categories)

    #We open the folder of the text acording to the selected category 
    path = categories[choosen_category]
    

main()