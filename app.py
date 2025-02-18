import asyncio
import flet as ft


async def main(page: ft.Page):
    await asyncio.sleep(1)
    page.add(ft.Text("Hello, async world!"))


ft.app(main)
