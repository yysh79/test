from model import ButtonModel
import flet as ft
from controller import on_button_click


def main(page: ft.Page):
    model = ButtonModel()
    button = ft.ElevatedButton("click", bgcolor=model.colors[model.current_index], on_click= lambda e: on_button_click(e, model, button) )
    page.add(button)