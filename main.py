import typer

app = typer.Typer()

@app.command()
def read_file(filepath: str):
    history_file = open(filepath, "r")
    history = []

    for line in history_file:
        if line.__contains__("apt install"):
            print(line)
            history.append(line)

    history_file.close()


if __name__ == "__main__":
    app()
