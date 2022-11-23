# Check https://pinout.xyz/pinout/pin12_gpio18

# Core
import RPi.GPIO as GPIO
import time

# Clases
from SensorUS import SensorUS
from RFID import RFID

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# Sensor
sensor = SensorUS(18, 24)
sensor.setup()

# RFID
lector = RFID()

# Ciclo
try:

  while True:

    # Obtener distancia
    distancia = sensor.getDistance()

    # Si la distancia es igual o menor a 5 cm
    if distancia <= 5.0:

      # Leer tarjeta
      lector.read()

    # Delay
    time.sleep(1)

except KeyboardInterrupt:

  print('Ejecucion detenida por el usuario')
  GPIO.cleanup()