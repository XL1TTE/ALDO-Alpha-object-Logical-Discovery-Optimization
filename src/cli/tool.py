from __future__ import annotations
import typer
from typing import Optional
from pathlib import Path
from .. import generator, data_manager
from ..formatters.txt import TxtFormatter
from ..formatters.md import MarkdownFormatter

app = typer.Typer(help="Optimization model generator for pattern discovery - Command Line Tool")

@app.command()
def generate(
    input_csv: Path = typer.Option(..., "--csv", "-i", help="Path to input CSV dataset", exists=True, file_okay=True, dir_okay=False, readable=True),
    output: Path = typer.Option(..., "--output", "-o", help="Path to save generated models"),
    format: str = typer.Option("txt", "--format", "-f", help="Output format (txt or md)")
) -> None:
    """
    Generate optimization models from a CSV dataset.
    """
    try:
        # 1. Load Data
        data = data_manager.load_data_from_csv(str(input_csv))
        
        # 2. Generate Models
        models = generator.generate_models(data)
        
        # 3. Select Formatter
        formatter = MarkdownFormatter() if format.lower() == "md" else TxtFormatter()
        
        # 4. Format Content
        content = formatter.get_header()
        separator = formatter.get_separator()
        for i, model in enumerate(models):
            content += formatter.format(model)
            if i < len(models) - 1:
                content += separator
                
        # 5. Save
        with open(output, "w", encoding="utf-8") as f:
            f.write(content)
            
        typer.echo(f"Successfully generated {len(models)} models to {output}")
        
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
