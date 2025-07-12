def ET(vr, va):
    return abs(vr - va) 

def ER(vr, va):
    return abs((vr - va)/vr)

def ERP(vr, va):
    return abs((vr - va)/vr) * 100

va1 = 1.347
va2 = 0.745
vr = 0.831

print("error 1 -------------------------------------------------------------------------------------------------")
print("error real absoluto: ", ET(vr, va1))
print("error relativo: ",ER(vr, va1))
print("error relativo porcentual: ", ERP(vr, va1))

print("error 2 -------------------------------------------------------------------------------------------------")
print("error real absoluto: ", ET(vr, va2))
print("error relativo: ",ER(vr, va2))
print("error relativo porcentual: ", ERP(vr, va2))