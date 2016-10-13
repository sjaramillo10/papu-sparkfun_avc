import time
import threading
import navio.pwm 

PWM_OUTPUT = 1
atras = 1.150 #ms servo min
adelante = 1.850 #ms servo max
neutral = atras+((adelante-atras)/2)

PWM = navio.pwm.PWM(PWM_OUTPUT)
PWM.set_period(50)

# Esta clase se encarga de manipular la velocidad del carrito
# Se utiliza un hilo para poder continuar con la ejecucion del programa principal
class Velocity(threading.Thread):
    # Inicializacion de la clase con hilos
    def __init__(self):        
        threading.Thread.__init__(self)
        self.velocidad = neutral
        self.aceleracion = 0.0
        self.velocidad_deseada = neutral
    
    # Este metodo provoca que el metodo setVelocity este siempre corriendo
    def run(self):
        PWM.set_duty_cycle(neutral)
        time.sleep(4)
        while True:
            self.setVelocity()

    # Se modifica la velicidad paulatinamente para alcanzar la velocidad deseada
    def setVelocity(self):
        if self.velocidad_deseada > self.velocidad:
            self.velocidad = min(self.velocidad_deseada, self.velocidad + self.aceleracion)
        elif self.velocidad_deseada < self.velocidad:
            self.velocidad = max(self.velocidad_deseada, self.velocidad + self.aceleracion)
        PWM.set_duty_cycle(self.velocidad)
        print self.velocidad
        # Para esperar al menos dos ciclos del pwm usar 0.04
        time.sleep(0.04)

    # Se cambian los parametros de aceleracion y velocidad deseada para acelerar al maximo
    # esta configuracion sera usada en rectas
    def accelerate(self):
        self.aceleracion = 0.01
        self.velocidad_deseada = adelante

    # Se cambian los parametros de aceleracion y velocidad deseada para una aceleracion media
    # y asi poder dar vuelta en las curvas mas facilmente
    def decelerate(self):
        self.aceleracion = -0.01
        self.velocidad_deseada = (neutral+adelante)/2

    # Se cambian los parametros de aceleracion y velocidad deseada para frenar rapidamente
    # Este metodo debera usarse al llegar a la meta, o si algo sale mal
    def stop(self):
        self.aceleracion = -0.1
        self.velocidad_deseada = neutral
