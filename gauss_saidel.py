
def mayor (rx1,rx2,rx3):
    if rx1 > rx2 and rx1 > rx3:
        return rx1
    elif rx2 > rx1 and rx2 > rx3:
        return rx2
    else:
        return rx3









def gauss_saidel (x1,x2,x3,error):
    k = 0
    rx1 = 1
    rx2 = 1
    rx3 = 1
    rx1_anterior = 0
    rx2_anterior = 0
    rx3_anterior = 0
    while mayor(abs(rx1-rx1_anterior),abs(rx2-rx2_anterior),abs(rx3-rx3_anterior)) > error:
        rx1_anterior = rx1
        rx2_anterior = rx2
        rx3_anterior = rx3
        rx1 = x1(rx2,rx3)
        rx2 = x2(rx1,rx3)
        rx3 = x3(rx1,rx2)
        k += 1
    print(k)
        
    print(f"\nResultados:\nx1 = {rx1}\nx2 = {rx2}\nx3 = {rx3}")
x1 = lambda x2, x3 : 1/5*(5 + 3*x2 - x3)
x2 = lambda x1, x3 : 1/4*(6 - 2*x1 + x3)
x3 = lambda x1, x2 : 1/8*(4 - 2*x1 + 3*x2)
error= 0.009
gauss_saidel(x1,x2,x3,error)