import pyautogui as pg
import time as tm
from datetime import datetime, timedelta

# Definir las coordenadas de los puntos
point1 = (568, 547)
point2 = (600, 600)  # Modifica estas coordenadas según tu necesidad

# Definir los tiempos para cada clic
click_time1 = "14:00"
click_time2 = "14:02"
end_time1 = "21:00"
end_time2 = "21:02"

def get_today_time(time_str):
    """Convierte una cadena de tiempo en un objeto datetime para el día de hoy."""
    now = datetime.now()
    time_obj = datetime.strptime(time_str, "%H:%M")
    return now.replace(hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0)

# Espera inicial para permitir la configuración
tm.sleep(5)

# Definir el intervalo de clics en segundos
interval_seconds_point1 = 30 * 60  # 30 minutos
interval_seconds_point2 = 60 * 60  # 1 hora

while True:
    now = datetime.now()
    time1 = get_today_time(click_time1)
    time2 = get_today_time(click_time2)
    end1 = get_today_time(end_time1)
    end2 = get_today_time(end_time2)

    # Hacer clic en el primer punto cada 30 minutos dentro del rango de tiempo
    if time1 <= now < end1:
        pg.click(*point1)
        print(f"Clic realizado en el primer punto a las {now.strftime('%H:%M:%S')}")
        tm.sleep(interval_seconds_point1)
    
    # Hacer clic en el segundo punto cada 1 hora dentro del rango de tiempo
    if time2 <= now < end2:
        pg.click(*point2)
        print(f"Clic realizado en el segundo punto a las {now.strftime('%H:%M:%S')}")
        tm.sleep(interval_seconds_point2)
    
    # Si es después del horario, esperar hasta el siguiente día a las 14:00
    if now >= end1 and now >= end2:
        next_time = (time1 + timedelta(days=1))
        time_to_wait = (next_time - now).total_seconds()
        print(f"Esperando hasta el día siguiente a las {next_time.strftime('%H:%M:%S')}")
        tm.sleep(time_to_wait)