from __future__ import annotations
import time
import os
from typing import List, Optional, TYPE_CHECKING
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.table import Table
from rich.theme import Theme
import questionary

from .. import generator, data_manager, native_dialogs
from ..formatters.txt import TxtFormatter
from ..formatters.md import MarkdownFormatter

if TYPE_CHECKING:
    from ..formatters.base import BaseFormatter
    from ..generator import PatternModel

# Custom theme for the CLI
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "bold red",
    "success": "bold green"
})

console = Console(theme=custom_theme)

def show_welcome() -> None:
    console.print(Panel.fit(
        "[bold blue]Pattern Discovery Optimization Model Generator[/bold blue]\n"
        "[italic]University AI Lab 3 - Alpha-Object Approach[/italic]",
        border_style="green",
        padding=(1, 2)
    ))

def get_user_choice() -> Optional[str]:
    return questionary.select(
        "Choose an action:",
        choices=[
            {"name": "Load Dataset (CSV)", "value": "1"},
            {"name": "Generate Synthetic Dataset (5+5)", "value": "2"},
            {"name": "Exit", "value": "exit"}
        ]
    ).ask()

def get_export_formatter() -> Optional[BaseFormatter]:
    choice = questionary.select(
        "Choose export format:",
        choices=[
            {"name": "Plain Text (.txt)", "value": "txt"},
            {"name": "Markdown with LaTeX (.md)", "value": "md"}
        ]
    ).ask()
    
    if choice == "txt": return TxtFormatter()
    if choice == "md": return MarkdownFormatter()
    return None

def show_progress(models: List[PatternModel], formatter: BaseFormatter) -> str:
    ext = formatter.get_extension().upper()
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task(f"[cyan]Generating {ext} models...", total=len(models))
        output_content = formatter.get_header()
        separator = formatter.get_separator()
        for i, model in enumerate(models):
            time.sleep(0.15) 
            output_content += formatter.format(model)
            if i < len(models) - 1:
                output_content += separator
            progress.advance(task)
    return output_content

def show_data_summary(data: List[List[float]]) -> None:
    table = Table(title="Dataset Preview", border_style="blue", header_style="bold magenta")
    table.add_column("Index", justify="right", style="cyan")
    table.add_column("X1 (Feature)", justify="right")
    table.add_column("X2 (Feature)", justify="right")
    table.add_column("Class", justify="center")

    for i, row in enumerate(data[:10]): 
        cls_style = "green" if row[2] == 1.0 else "red"
        cls_name = "POSITIVE" if row[2] == 1.0 else "NEGATIVE"
        table.add_row(str(i), f"{row[0]:.2f}", f"{row[1]:.2f}", f"[{cls_style}]{cls_name}[/]")
    
    if len(data) > 10: table.add_row("...", "...", "...", "...")
    console.print(table)
    console.print(f"Total objects processed: [bold green]{len(data)}[/bold green]")

def run() -> None:
    """Orchestrates the interactive CLI workflow."""
    show_welcome()
    choice = get_user_choice()
    if choice == "exit" or choice is None: return

    data: List[List[float]] = []
    if choice == "1":
        input_path = native_dialogs.get_open_file_path("Select Dataset CSV")
        if not input_path or not os.path.exists(input_path):
            console.print("[error]Error: No valid input file selected.[/]")
            return
        try:
            data = data_manager.load_data_from_csv(input_path)
        except Exception as e:
            console.print(f"[error]Error loading data: {e}[/]")
            return
    else:
        data = data_manager.generate_synthetic_data()
    
    show_data_summary(data)
    models = generator.generate_models(data)
    formatter = get_export_formatter()
    if not formatter: return
    
    ext = formatter.get_extension()
    filter_str = "Text Files (*.txt)|*.txt" if ext == "txt" else "Markdown Files (*.md)|*.md"
    output_path = native_dialogs.get_save_file_path(f"Save Models as {ext.upper()}", filter_str, ext)
    if not output_path: return
    
    content = show_progress(models, formatter)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        console.print(f"\n[success]Success![/] Models saved to [info]{output_path}[/]")
    except Exception as e:
        console.print(f"[error]Error saving file: {e}[/]")
