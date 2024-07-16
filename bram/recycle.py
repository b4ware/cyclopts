from typing import Literal
import functools
from contextvars import ContextVar

import cyclopts

APP = ContextVar('APP', default=cyclopts.App()) # probably no better than a global

def recycle(func, app: cyclopts.App = APP.get()):
    """
    If the wrapped function is called, its arguments go through
    the Cyclopts command parser. The original function can also
    be called via the CLI -- that's just the regular ``app()``.

    https://github.com/BrianPugh/cyclopts/blob/main/cyclopts/core.py
    """
    # inspect(f"{func=}")
    app.command(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ## MAYDO: shlex.split, since/but cyclopt does that
        strargs = ' '.join(args) + ' '
        for key, value in kwargs.items():
            strargs += f"--{key}={value} "
        fake_cli_args = f"{func.__name__} {strargs}"
        # print(f"{fake_cli_args=}")
        return app(fake_cli_args)
    return wrapper




if __name__ == "__main__":
    from rich import print, inspect
    import rich.traceback
    rich.traceback.install(show_locals=True)

    @recycle
    def hi(name: str, whatever=42, nobody=False) -> str:
        return f"hello {name}!! {locals()=}"

    @recycle
    def bye(name: str, a:str=2, b=42):
        return f"bye {name}!! {locals()=}"

    app = APP.get() # can be below the above :)


    @app.command
    def native():
        return "hi world"
    
    @recycle
    def literal(value: Literal["foo", "bar", 3]):
        print(f"{value=} {type(value)=}")

    result = app()
    if result is not None:
        # inspect(result)
        print(result)