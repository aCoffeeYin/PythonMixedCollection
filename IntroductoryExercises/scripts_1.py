# 七段数码管绘制即时系统日期

import turtle, time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):     #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(digit):       #根据数字绘制七段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(18)
def drawDate(date):     #获得要输出的数字, date格式为‘%Y-%m=%d+’
    turtle.pencolor("purple")
    for i in date:
        if i == '-':
            turtle.pencolor("black")
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("purple")
            turtle.fd(40)
        elif i == '=':
            turtle.pencolor("black")
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("purple")
            turtle.fd(40)
        elif i == '+':
            turtle.pencolor("black")
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))      #通过函数将数字变为整数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()















    
