import apt
import typer

app = typer.Typer()

@app.command()
def read_file(filepath: str):
    cache = apt.Cache()
    history_file = open(filepath, "r")
    history = []

    for line in history_file:
        #TODO: line needs to be cleaned
        if line.__contains__("apt install"):
            print(line)
            if cache[line].is_installed():
                print("is installed")
                history.append(line)

    history_file.close()


if __name__ == "__main__":
    app()
