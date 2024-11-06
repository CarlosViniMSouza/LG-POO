import functools

def log_activity(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # Formata os argumentos posicionalmente
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # Formata os argumentos nomeados
        signature = ", ".join(args_repr + kwargs_repr)  # Junta tudo em uma única string
        
        print(f"Executing {func.__name__} with arguments: {signature}")
        
        result = func(*args, **kwargs)
        
        print(f"{func.__name__} retorned: {result!r}")
        
        return result
    
    return wrapper
