import turtle,datetime
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDight(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor('red')
    for i in date:
        if i=='+':
            turtle.write('年',font=('楷体',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i=='-':
            turtle.write('月',font=('楷体',18,'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i=='*':
            turtle.write('日',font=('楷体',18,'normal'))
            turtle.pencolor('purple')
            turtle.fd(40)
        elif i=='=':
            turtle.write('时',font=('楷体',18,'normal'))
            turtle.pencolor('yellow')
            turtle.fd(40)
        elif i=='#':
            turtle.write('分',font=('楷体',18,'normal'))
            turtle.pencolor('black')
            turtle.fd(40)
        elif i=='$':
            turtle.write('秒',font=('楷体',18,'normal'))
        else:
            drawDight(eval(i))
def main():
    turtle.setup(1500,600)
    turtle.speed(10)
    turtle.penup()
    turtle.fd(-550)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y+%m-%d*%H=%M#%S$'))
    turtle.hideturtle()
    turtle.done()
main()


            
