from tkinter import*

#operações
def soma(a,b):
    return a+b
def subtrai(a,b):
    return a-b
def multiplica(a,b):
    return a*b
def divide(a,b):
    return a/b
def percentual(a,b):
    return a*(b/100)

#comando
#inserir número
def comando_s(x,base):
    nov=base.get()
    base.set(nov+x)
#fazer o cálculo
def comando_ci(base):
    nov=base.get()
    val1s=''
    val2s=''
    n_op=0
    test=0
    for letra in range(len(nov)):
        if nov[letra]=='+' or nov[letra]=='-' or nov[letra]=='*' or nov[letra]=='/' or nov[letra]=='%':
            n_op=letra
            test+=1
            break
    if test==1:
        for letra in range(n_op):
            val1s+=nov[letra]
            if nov[letra] == '+' or nov[letra] == '-' or nov[letra] == '*' or nov[letra] == '/' or nov[letra]=='%':
                nov='ERROR'
                break
        for letra in range(n_op+1,len(nov)):
            val2s+=nov[letra]
            if nov[letra] == '+' or nov[letra] == '-' or nov[letra] == '*' or nov[letra] == '/' or nov[letra]=='%':
                nov='ERROR'
                break
    else:
        nov='ERROR'
    if nov!='ERROR':
        val1 = float(val1s)
        val2 = float(val2s)
        if nov[n_op]=='+':
            base.set(str(round(soma(val1,val2),4)))
        elif nov[n_op]=='-':
            base.set(str(round(subtrai(val1,val2),4)))
        elif nov[n_op]=='*':
            base.set(str(round(multiplica(val1,val2),4)))
        elif nov[n_op]=='/':
            base.set(str(round(divide(val1,val2),4)))
        elif nov[n_op]=='%':
            base.set(str(round(percentual(val1,val2),4)))
        else:
            base.set("")
    else:
        base.set("")
#apagar
def comando_cd(base):
    nov=base.get()
    nov2=''
    if len(nov)>0:
        for letra in range(1,len(nov)):
            nov2+=nov[letra]
    base.set(nov2)
#salvar
def salvar(base):
    arq=open("Operações Guardadas.txt",'a')
    nov=base.get()
    if nov!="":
        arq.write(nov)
        arq.write("\n")
        arq.close()
def Apresentar(base):
    arq=open("Operações Guardadas.txt",'r')
    for linha in arq:
        base.set(linha)
    arq.close()

#criar interface
calculadora=Tk()
calculadora.title("Calculadora")
calculadora.iconbitmap("calc.ico")
calculadora.geometry("%dx%d+%d+%d"%(314,465,90,50))
calculadora['bg']='#4169E1'
operac=StringVar()
#tela
label=Label(
    calculadora,
    textvariable=operac,
    width=14,
    bg='#87CEFA',
    fg='#191970',
    font='Times 30 italic',
    relief='ridge',
    anchor=E
)
label.grid(row=0,columnspan=4)
#botões
bt1=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='7',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('7',operac)
)
bt1.grid(row=1,column=0)
bt2=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='8',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('8',operac)
)
bt2.grid(row=1,column=1)
bt3=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='9',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('9',operac)
)
bt3.grid(row=1,column=2)
bt4=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='-',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('-',operac)
)
bt4.grid(row=3,column=3)
bt5=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='4',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('4',operac)
)
bt5.grid(row=2,column=0)
bt6=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='5',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('5',operac)
)
bt6.grid(row=2,column=1)
bt7=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='6',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('6',operac)
)
bt7.grid(row=2,column=2)
bt8=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='+',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('+',operac)
)
bt8.grid(row=2,column=3)
bt9=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='1',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('1',operac)
)
bt9.grid(row=3,column=0)
bt10=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='2',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('2',operac)
)
bt10.grid(row=3,column=1)
bt11=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='3',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('3',operac)
)
bt11.grid(row=3,column=2)
bt12=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='=',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_ci(operac)
)
bt12.grid(row=5,column=3)
bt13=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='=>',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_cd(operac)
)
bt13.grid(row=1,column=3)
bt14=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='*',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('*',operac)
)
bt14.grid(row=4,column=3)
bt15=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='/',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('/',operac)
)
bt15.grid(row=4,column=2)
bt16=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='Rp',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: Apresentar(operac)
)
bt16.grid(row=5,column=2)
bt17=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='%',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('%',operac)
)
bt17.grid(row=5,column=0)
bt18=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='.',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('.',operac)
)
bt18.grid(row=4,column=0)
bt19=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='Sv',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: salvar(operac)
)
bt19.grid(row=5,column=1)
bt20=Button(
    calculadora,
    repeatdelay=10,
    width=3,
    text='0',
    bg='#008080',
    fg='#7FFFD4',
    font='Times 30 italic',
    relief='ridge',
    justify=CENTER,
    command=lambda: comando_s('0',operac)
)
bt20.grid(row=4,column=1)

calculadora.mainloop()