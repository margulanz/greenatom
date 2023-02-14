def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda step = step : callback(step))# Переменные в лямбда-функциях должны быть предоставлены
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()

