import pyautogui as pg
import time as tm
from datetime import datetime, timedelta

# Definir las coordenadas del botón
x, y = 568, 547

# Definir el rango de tiempo
start_time = datetime.strptime("13:30", "%H:%M")  # 1:30 PM
end_time = datetime.strptime("13:40", "%H:%M")    # 1:45 PM

# Definir el intervalo de clics en minutos
click_interval_seconds = 2 * 60  # 2 minutos en segundos

# Espera inicial para permitir la configuración
tm.sleep(5)

# Obtener la hora actual
now = datetime.now()

# Ajustar el rango de tiempo para el día actual
start_time = start_time.replace(year=now.year, month=now.month, day=now.day)
end_time = end_time.replace(year=now.year, month=now.month, day=now.day)

# Realizar los clics necesarios dentro del rango de tiempo
while datetime.now() < start_time:
    # Esperar hasta la hora de inicio si aún no es la hora
    tm.sleep((start_time - datetime.now()).total_seconds())

while datetime.now() < end_time:
    pg.click(x, y)
    tm.sleep(click_interval_seconds)

print("Proceso completado: Se han realizado todos los clics programados.")
