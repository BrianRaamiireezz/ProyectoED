# Check https://pinout.xyz/pinout/pin12_gpio18

# Core
import RPi.GPIO as GPIO
import time

# Clases
from SensorUS import SensorUS
from RFID import RFID

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Sensores - # Dar nombres entrada/salida
sensor1 = SensorUS(18, 24)
sensor1.setup()

sensor2 = SensorUS() # Check valores de pines
# sensor2.setup() # Setup no acepta valores de pines por default

# RFID
lector = RFID()

# Ciclo
try:

  while True:

    # Obtener distancias
    distancia1 = sensor1.getDistance()
    print ("Distancia 1 = %.1f cm" % distancia1)
    distancia2 = sensor2.getDistance()
    print ("Distancia 2 = %.1f cm" % distancia2)

    # Para sensor 1
    if distancia1 <= 5.0:

      # Leer tarjeta
      lector.read()

      # Reset distancia 2
      distancia2 = 100.0

    # Para sensor 2
    if distancia2 <= 5.0:

      # Leer tarjeta
      lector.read()

    # Delay
    time.sleep(1)

except KeyboardInterrupt:

  print('Ejecucion detenida por el usuario')
  GPIO.cleanup()