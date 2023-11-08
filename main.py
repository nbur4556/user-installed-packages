import typer

app = typer.Typer()

@app.command()
def read_file(filepath: str):
    history_file = open(filepath)
    print(history_file.read())


if __name__ == "__main__":
    app()
