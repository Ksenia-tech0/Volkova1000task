import math

G0 = 9.80665

def delta_v(i_sp: float, m_zero: float, m_one: float) -> float:
    """Формула Циолковского для характеристической скорости."""
    if i_sp <= 0 or m_zero <= 0 or m_one <= 0:
        raise ValueError("Все аргументы должны быть строго больше нуля.")
    if m_zero < m_one:
        raise ValueError("Начальная масса m_zero не может быть меньше конечной m_one.")
    
    return i_sp * G0 * math.log(m_zero / m_one)

def fuel_needed(m_dry: float, delta_v_val: float, i_sp: float) -> float:
    """Обратная задача: расчет необходимой массы топлива."""
    if m_dry <= 0 or delta_v_val < 0 or i_sp <= 0:
        raise ValueError("Массы и удельный импульс должны быть > 0, delta_v >= 0.")
    
    return m_dry * (math.exp(delta_v_val / (i_sp * G0)) - 1)

def flight_time(d: float, a: float) -> float:
    """Расчет времени перелета с постоянным ускорением/торможением по формуле из задания."""
    if d <= 0 or a <= 0:
        raise ValueError("Дистанция и ускорение должны быть строго больше нуля.")
    
    return 2 * math.sqrt((d / 2) / a)