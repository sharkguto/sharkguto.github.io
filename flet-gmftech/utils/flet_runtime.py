import asyncio
import inspect


def call_page_method(page, method_name, *args, **kwargs):
    """Call a Flet page method whether the current runtime exposes it as sync or async."""
    method = getattr(page, method_name)

    if inspect.iscoroutinefunction(method):
        run_task = getattr(page, "run_task", None)
        if callable(run_task):
            return run_task(method, *args, **kwargs)
        return _run_awaitable(method(*args, **kwargs))

    result = method(*args, **kwargs)
    if inspect.isawaitable(result):
        run_task = getattr(page, "run_task", None)
        if callable(run_task):
            async def await_result():
                return await result

            return run_task(await_result)
        return _run_awaitable(result)

    return result


def _run_awaitable(awaitable):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(awaitable)

    return loop.create_task(awaitable)
