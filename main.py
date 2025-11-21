from db_p.main_db import init_db, add_shop, get_shops, set_completed, delete_shop
import flet as ft

def main(page: ft.Page):
    page.title = "Список покупок"
    filter_type = "all"
    shops_column = ft.Column(spacing=5)

    def load_shops():
        shops_column.controls.clear()
        for stuf_id, name, completed in get_shops(filter_type):
            checkbox = ft.Checkbox(
                label=name,
                value=bool(completed),
                on_change=lambda e, sid=stuf_id: toggle_completed(sid, e.control.value)
            )
            delete_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, sid=stuf_id: remove_shop(sid))
            shops_column.controls.append(
                ft.Row([checkbox, delete_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )
        page.update()

    def add_item(e):
        text = input_stuf.value
        if text:
            add_shop(text)
            input_stuf.value = ""
            load_shops()

    def remove_shop(shop_id):
        delete_shop(shop_id)
        load_shops()

    def toggle_completed(shop_id, value):
        set_completed(shop_id, int(value))
        load_shops()


    def change_filter(e):
        nonlocal filter_type
        idx = e.control.selected_index
        if idx == 0:
            filter_type = "all"
        elif idx == 1:
            filter_type = "completed"
        else:
            filter_type = "active"
        load_shops()

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

    page.add(ft.Row([input_stuf, button_add]), filter_tabs, shops_column)
    load_shops()

if __name__ == "__main__":
    init_db()
    ft.app(target=main)
