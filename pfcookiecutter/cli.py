import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """Say hello to someone"""
    typer.echo(f"Hello {name}")

@app.command()
def goodbye(name: str):
    typer.echo(f"Goodbye {name}")


if __name__ == "__main__":
    app()