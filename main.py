import apt
import re
import typer

app = typer.Typer()

@app.command()
def read_file(filepath: str):
    cache = apt.Cache()
    history_file = open(filepath, "r")
    history = []

    for line in history_file:
        if line.__contains__("apt install"):
            pkg_name = re.findall(r'apt install ([\w-]+)', line)
            try:
                if cache[pkg_name[0]].is_installed:
                    history.append(pkg_name[0])
                else:
                    print("is not installed")
            except:
                print("is not installed")
    
    for item in history:
        print(item)

    history_file.close()


if __name__ == "__main__":
    app()
