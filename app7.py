import turtle
import colorsys

# Ekranni sozlash
screen = turtle.Screen()
screen.bgcolor("black")  # Fon qora rangda
t = turtle.Turtle()
t.speed(0)               # Eng tez chizish tartibi
t.width(2)

# Rangli spiral chizish
h = 0
for i in range(200):
    # Ranglarni kamalakdek o'zgartirish
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 0.005
    
    # Harakat va burilish
    t.forward(i * 1.5)
    t.left(59)          # 59 darajaga burilish (shaklni yaratuvchi asos)

# Chizish tugagach oynani yopmaslik
turtle.done()