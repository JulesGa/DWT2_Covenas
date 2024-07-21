import pyautogui as pg, time as tm

# Espera 5 segundos para darte tiempo de mover el cursor al botón
tm.sleep(5)

# Obtiene y muestra la posición actual del cursor
x, y = pg.position()
print(f"La posición actual del cursor es: ({x}, {y})")
