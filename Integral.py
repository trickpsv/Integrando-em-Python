from tkinter import *

def integral(f,ini,final,divisoes):
	tamanho = (final - ini) / divisoes

	integ = 0
	list = []
	for i in range(divisoes):
		integ += (f(ini + i*tamanho) + f(ini + (i+1)*tamanho))*tamanho/2
		list.append(f(ini + i*tamanho))
	list.append(f(ini + divisoes*tamanho))
	return integ,list

def onSlide(z):
	s = entfuncao.get()
	print(s)
	funcao = lambda x:eval(s)
	ini = float(entinicio.get())
	final = float(entfinal.get())
	divisoes = int(slider.get())
	integ ,lista = integral( funcao, ini  ,final  , divisoes )
	desenhar(lista,ini,final, abs(final - ini) / divisoes, quadro )
	lbintegra["text"] = "Valor da integral = " + str(integ)
	print(integ)
	
master = Tk()
master.geometry("900x600")
master.title("Integrando em Python")

lbfuncao = Label(master , text = "Funcao:")
lbfuncao.place(x=10,y=100)
entfuncao = Entry(master, width = 20)
entfuncao.place(x=60,y=100)

lbinicio = Label(master , text = "Inicio:")
lbinicio.place(x=10,y=130)
entinicio = Entry(master, width = 20)
entinicio.place(x=60,y=130)

lbfinal = Label(master , text = "Final:")
lbfinal.place(x=10,y=160)
entfinal = Entry(master, width = 20)
entfinal.place(x=60,y=160)

quadro = Canvas(master, width = 500 , height = 500)
quadro.place(x = 300 , y = 40 )
quadro.create_rectangle(0,0,500,500,fill = "white")

slider = Scale(master , from_ = 0, to = 100, orient = "horizontal" , length = 300 , command = onSlide)
slider.place(x = 430,y = 550 )


lbintegra = Label(master , text = "Valor da integral = 0")
lbintegra.place(x = 30 , y = 400)

#funcao para desenhar os retangulos e os eixos:
def desenhar(lista, ini , final , tam , quadro):
	quadro.delete("all")
	quadro.create_rectangle(0,0,500,500,fill = "white")

	maior = - 9999999
	for i in lista:
		if abs(i) > maior:
			maior = abs(i)
	tamX = 460
	tamY = 500
	margem = 20		

	ycord = lambda x: tamY - (tamY/2 + (tamY-margem)/2 * x / (maior) )
	xcord = lambda x: margem + abs(x-ini)/abs(final - ini)*tamX

	for i,j in enumerate(lista):
		if i == len(lista)-1:
			break
		quadro.create_line(xcord(ini + i*tam),ycord(0),xcord(ini + i*tam),ycord(j), width = 2)
		quadro.create_line(xcord(ini +i*tam),ycord(j),xcord(ini + (i+1)*tam),ycord(lista[i+1]), width = 2)
		quadro.create_line(xcord(ini +(i+1)*tam),ycord(lista[i+1]),xcord(ini + (i+1)*tam),ycord(0), width = 2)
		#print(xcord(i*tam),ycord(0))
	desenhaEixos(maior, ini, final , xcord , ycord , quadro , tamX , tamY)	
	
def desenhaEixos(maior, ini, final , xcord , ycord , quadro , tamX , tamY):
	if ini < 0 and final > 0:
		quadro.create_line(xcord(0),20,xcord(0),480)
	quadro.create_line(20,ycord(0),480,ycord(0))	

desenhar([5,1,3,9],1,5,1,quadro)	

master.mainloop()
