# import numpy as np 


# # fx = lambda x,y : (6*(x**2)) * y
# fx = lambda x,y: 5/((x**2) +1)


# def euler(fx, x0, y0, h, n):
#     for i in range(n+1):
#         y = y0 + fx(x0, y0) * h
#         print(f"x{i} = {x0} y{i} = {y0}  |  y{i+1}= {y} ")
#         # print(i)
#         x0 += h
#         y0 = y 
        
#     return y



# def heun(fx,x0,y0,h,n):
#     for i in range(n+1):
#         y1 = y0 + ((fx(x0,y0) + fx(x0+h,euler(fx,x0,y0,h,i))/2) * h)
#         print(f"x{i} = {x0}    y{i} = {y1} ")
#         print(i)
#         x0 += h
#         y0 = y1
#     return y1



# # y0 = 0
# # x0 = 0
# # max = 4 
# # h = 0.25
# # n = int((max - x0)/h)


# y0 = 0
# x0 = 0
# max = 1 
# h = 0.2
# n = int((max - x0)/h)

# #n valor que quieres sacar numero de iteracion iteracion final 
# print(euler(fx, x0, y0, h, n))
# # print(heun(fx, x0, y0, h, n))



import numpy as np 





# fx = lambda x,y: 5/((x**2) +1)





fx = lambda x ,y : 6*(x**2)*y
def heun(fx, x0, y0, h, n):
    for i in range(n+1):
        y_pred = y0 + h * fx(x0, y0)
        y1 = y0 + h * (fx(x0, y0) + fx(x0 + h, y_pred))/2
        print(f"x{i} = {x0:.4f}    y{i} = {y0:.6f}    y{i+1} = {y1:.6f}")
        x0 += h
        y0 = y1
    return y1
x0 = 2
y0 = 0
maximo = 4
h = 0.25
n = int((maximo - x0)/h)
print("\nMétodo de Heun:")
resultado = heun(fx, x0, y0, h, n)
print(f"\nResultado final: {resultado:.6f}")




