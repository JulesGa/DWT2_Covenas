import pyautogui as pg
import time as tm
from datetime import datetime, timedelta

# Definir las coordenadas del botón
x, y = 568, 547

# Definir el rango de tiempo (en formato de 24 horas)
start_time = "14:01"
end_time = "14:10"

# Definir el intervalo de clics en minutos
click_interval_seconds = 1 * 60  # 30 minutos en segundos

def get_today_time(time_str):
    """Convierte una cadena de tiempo en un objeto datetime para el día de hoy."""
    now = datetime.now()
    time_obj = datetime.strptime(time_str, "%H:%M")
    return now.replace(hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0)

# Espera inicial para permitir la configuración
tm.sleep(5)

while True:
    now = datetime.now()
    start_dt = get_today_time(start_time)
    end_dt = get_today_time(end_time)
    
    if start_dt <= now < end_dt:
        clicks_done = 0
        clicks_needed = (end_dt - start_dt).seconds // click_interval_seconds
        
        while clicks_done < clicks_needed and start_dt <= datetime.now() < end_dt:
            pg.click(x, y)
            clicks_done += 1
            tm.sleep(click_interval_seconds)
        
        print("Proceso completado: Se han realizado todos los clics programados para hoy.")
    else:
        # Calcular el tiempo de espera hasta el inicio del rango de tiempo del día siguiente
        if now >= end_dt:
            start_dt += timedelta(days=1)
        time_to_start = (start_dt - now).total_seconds()
        tm.sleep(time_to_start)
