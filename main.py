import readline
import typer

app = typer.Typer()

@app.command()
def hello():
    history_length = readline.get_history_length()
    if history_length <= 0:
        print("No history found")

    for i in range(readline.get_history_length()):
        print(readline.get_history_item(i+1))

if __name__ == "__main__":
    app()
