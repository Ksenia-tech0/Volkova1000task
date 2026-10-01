import sched, time

s = sched.scheduler(time.time, time.sleep)


def say(text):
    """Печатает сообщение с меткой времени."""
    print(f"[{time.strftime('%H:%M:%S')}] {text}")


start = time.time()
print("Старт. Отсчёт времени от t0 = 0\n")

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0 — сработает ПЕРВЫМ)",))
s.enter(1, 1, say, ("Прошла 1 секунда",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 c",))

print("Очередь до run():", len(s.queue), "задач")

print("\nСодержимое s.queue ДО запуска (отсортировано по времени):")
for i, ev in enumerate(s.queue, 1):
    print(f"  {i}. time={ev.time - start:.2f}s, priority={ev.priority}, action={ev.action.__name__}, args={ev.argument}")

print("\nrun() блокирует поток, пока все задачи не выполнятся:\n")
s.run()
print("\nГотово. Пустая очередь?", s.empty())