#PID
va = time = e_0 = e_1 = props = derivs = intes = 0
Vm = 1.850 #valor minimo (izquierda,adelante)
VM = 1.150 #valor maximo (derecha,atras)
kp = 1
ki = 0.5
kd = 0.05
t_s = 0.1
T = 1/t_s
time = 0
while(True):
    va = 0
    e_1 = e_0
    e_0 = sp - va
    props = kp * e_0
    derivs = kd * (e_0 - e_1) * T
    if ((intes < VM) and (intes > Vm)):
        intes += ki * T * e_0
    else:
        if intes >= VM:
            intes = VM #limita la señal de control
        if intes <= Vm:
            intes = Vm #limita la señal de control
    u = props + intes + derivs
    if u > VM:
        u = VM
    if u < Vm:
        u = Vm
    time += t_s
    print u


