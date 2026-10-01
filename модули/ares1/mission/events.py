import random

EVENTS_POOL = [
    ("Метеоритный микрошторм", -15, 10),
    ("Солнечная вспышка (радиация)", -10, 15),
    ("Сбой в системе жизнеобеспечения", -20, 5),
    ("Штатный полет (происшествий нет)", 0, 60),
    ("Успешная оптимизация энергосистемы", 5, 10),
]

def random_event(seed: int | None = None) -> tuple[str, int]:
    """Выбирает случайное событие с учетом весов и сида для воспроизводимости."""
    if seed is not None:
        random.seed(seed)
        
    events = [e[0] for e in EVENTS_POOL]
    weights = [e[2] for e in EVENTS_POOL]
    
    chosen_event_name = random.choices(events, weights=weights, k=1)[0]
    
    resource_change = next(e[1] for e in EVENTS_POOL if e[0] == chosen_event_name)
    
    return chosen_event_name, resource_change