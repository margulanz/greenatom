def create_handlers(callback):
    handlers = []
    for step in range(5):
        handlers.append(lambda step = step : callback(step)) # Variables in lambda functions should be provided
    return handlers


def execute_handlers(handlers):
    for handler in handlers:
        handler()

