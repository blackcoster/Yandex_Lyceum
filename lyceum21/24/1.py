from turtle import Turtle, register_shape, done

crown = Turtle()
# кортеж координат новой формы
shape = ((-10,0),(-2,2),(0,10),(2,2),(10,0),(2,-2),(0,-10),(-2,-2))

# # регистрируем форму
register_shape('lotus', shape)
# # меняем форму на новую
crown.shape('lotus')
# # задаем размер
color,size = input().split()
crown.color(color)
crown.turtlesize(int(size))

places = [int(i) for i in input().split()]
# p_x = [i for i in places[::2]]
# p_y = [i for i in places[1::2]]
# for i in range(len(p_x)):
#
crown.pu()
for i in range(0,len(places),2):
    x,y = places[i:i+2]
    crown.goto(x,y)
    crown.stamp()
done()