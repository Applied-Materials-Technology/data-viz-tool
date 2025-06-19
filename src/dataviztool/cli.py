import typer
import os

app = typer.Typer()

@app.command()
def showdir():
    print(os.getcwd())

@app.command()
def repeat(repeat: str):
    print(f"repeating: {repeat}")

if __name__ == "__main__":
    app()