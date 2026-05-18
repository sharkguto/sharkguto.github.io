import flet as ft


def walk_controls(control):
    """Yield a Flet control and every nested child control."""
    if control is None:
        return

    yield control

    content = getattr(control, "content", None)
    if isinstance(content, ft.Control):
        yield from walk_controls(content)

    controls = getattr(control, "controls", None)
    if controls:
        for child in controls:
            if isinstance(child, ft.Control):
                yield from walk_controls(child)


def find_controls(control, control_type):
    return [item for item in walk_controls(control) if isinstance(item, control_type)]


def find_text_values(control):
    return [item.value for item in find_controls(control, ft.Text) if getattr(item, "value", None)]


def text_exists(control, expected):
    return any(expected in value for value in find_text_values(control))
