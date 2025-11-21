from db_p.main_db import init_db, add_stuf, get_stufs, set_completed, delete_stuf
import flet as ft

def main(page: ft.Page):
    page.title = "Список покупок"
    filter_type = "all"
    stufs_column = ft.Column(spacing=5)

    def load_stufs():
        stufs_column.controls.clear()
        for stuf_id, name, completed in get_stufs(filter_type):
            checkbox = ft.Checkbox(
                label=name,
                value=bool(completed),
                on_change=lambda e, sid=stuf_id: toggle_completed(sid, e.control.value)
            )
            delete_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, sid=stuf_id: remove_stuf(sid))
            stufs_column.controls.append(
                ft.Row([checkbox, delete_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        page.update()

    def add_item(e):
        text = input_stuf.value
        if text:
            add_stuf(text)
            input_stuf.value = ""
            load_stufs()

    def remove_stuf(stuf_id):
        delete_stuf(stuf_id)
        load_stufs()

    def toggle_completed(stuf_id, value):
        set_completed(stuf_id, int(value))
        load_stufs()


    def change_filter(e):
        nonlocal filter_type
        idx = e.control.selected_index
        if idx == 0:
            filter_type = "all"
        elif idx == 1:
            filter_type = "completed"
        else:
            filter_type = "active"
        load_stufs()

    input_stuf = ft.TextField(label="Добавить товар", expand=True, on_submit=add_item)
    button_add = ft.IconButton(icon=ft.Icons.ADD, on_click=add_item)

    filter_tabs = ft.Tabs(
        selected_index=0,
        on_change=change_filter,
        tabs=[
            ft.Tab(text="Все"),
            ft.Tab(text="Купленные"),
            ft.Tab(text="Не купленные"),
        ]
    )

    page.add(ft.Row([input_stuf, button_add]), filter_tabs, stufs_column)
    load_stufs()

if __name__ == "__main__":
    init_db()
    ft.app(target=main)
