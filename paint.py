import turtle
import keyboard
import time

t=turtle.Turtle()
turtle.setup(800,600)
t.pencolor('black')
janela=turtle.Screen()
t.shape('circle')
t.speed(0)
t.pensize(5)
desenhar_ativo=False
def anvançar():
    if keyboard.is_pressed('w'):
        t.forward(10)


def virar_esq():
    if keyboard.is_pressed('a'):
        t.left(15)

def virar_dire():
    if keyboard.is_pressed('d'):
        t.right(15)

def grossura():
    if keyboard.is_pressed('tab'):
        try:
            grossu=int(input('Qual a grossura '))
            t.pensize(grossu)
            t.shapesize(grossu/20)
            return
        except ValueError:
            print('use um nª inteiro')
            pass

def cor():
    try:
        if keyboard.is_pressed('shift'):
            cor=str(input('Qual a cor (escreva em inglês) '))
            t.pencolor(cor)
            t.fillcolor(cor)
    except turtle.TurtleGraphicsError:
        print('Use uma cor valida')
        segunda_tent()
        pass
def segunda_tent():
    cor()    
   
def limpar_ecra():
    if keyboard.is_pressed('c'):
        t.clear()            
def seguir_rato(evento):
    # Converte as coordenadas do rato para o ecrã do turtle
    x = evento.x - (janela.window_width() / 2)
    y = (janela.window_height() / 2) - evento.y
    t.goto(x, y)
def botao_1click(evento):
    t.pendown()
    desenhar_ativo=True
def botao_1largado(evento):
    t.penup()
    desenhar_ativo=False  
def guardar_desenho():
    if keyboard.is_pressed('F1'):
    # Extrai o ecrã do turtle e guarda o ficheiro com o nome que escolheres
        ficheiro_nome=input('qual o nome do ficheiro  ')
        janela.getcanvas().postscript(file=ficheiro_nome)
        ficheiro_bom=ficheiro_nome+'.ps'
        print("Desenho guardado com sucesso como ",ficheiro_bom)       
        
print('=====')        
print('Paint')
print('=====')
print('use "w" "a" e "d" ou arraste para desenhar\nuse tab para a grossura(use só numeros)\nuse shift para mudar a cor\nuse F1 para guardar\n use ctrl+c para parar')
try:
    try:
        janela.listen()
        janela.cv.bind("<Motion>",seguir_rato)
        janela.cv.bind("<ButtonPress-1>", botao_1click)
        janela.cv.bind("<ButtonRelease-1>", botao_1largado)
        janela.getcanvas().config(cursor="none")
        while True:
            anvançar()
            virar_esq()
            virar_dire()
            grossura()
            cor()
            limpar_ecra()
            guardar_desenho()
            turtle.Screen().update()
            time.sleep(0.05)
    except KeyboardInterrupt:
        print('Adeus')
        pass        
except turtle.TurtleGraphicsError:
    print('use um valor ou cor valida')   
    pass 