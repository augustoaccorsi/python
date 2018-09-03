#escreva uma função righ justify que receba um string e a ultima letra tem que ser exibina na posição 70
def right_justify(value):
    cat = value
    while len(cat) != 70:
        cat = " " + cat
    print(cat)

right_justify("guto")
