import RPi.GPIO as GPIO
import MFRC522

# signal

class RFID:
  """
  Clase utilizada para representar un lector RFID

  Atributos
    reader (MFRC522): Objeto utilizado para realizar la lectura
  """


  def __init__(self):
    """
    Constructor por default
    """
    self.__reader = MFRC522.MFRC522()

  def uidToString(uid):

    stringUID = ""

    for i in uid:
      stringUID = format(i, '02X') + stringUID

    return stringUID

  # Check - Solo es un objeto para las dos RFID