"""The dashboard page."""
from reflex_python.templates import template

import reflex as rx


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Alvin's website", font_size="3em"),
        rx.text("Welcome to Reflex!"),
        rx.text(
4            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
    )
