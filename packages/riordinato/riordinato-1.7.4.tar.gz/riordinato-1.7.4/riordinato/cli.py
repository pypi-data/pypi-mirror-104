"""Cli app for riordinato"""
# Riordinato utils
from .cli_utils import get_prefixes_file, get_data, create_file, show_common_files
from riordinato import Riordinato
from riordinato import Prefix
# Exceptions
from riordinato.exceptions import InvalidPrefixError
from shutil import SameFileError

from pathlib import Path
from typing import List
from typing import Optional
import json

import typer


app = typer.Typer(help="Organize your files by prefixes.")


@app.command()
def init():
    """
    Create prefixes.json file in current directory.
    """
    file = Path.cwd() / "prefixes.json"
    if file.exists():
        typer.echo("The file already exists")
    else:
        create_file(str(file))
        typer.secho("The prefixes.json file was created.",
                    fg=typer.colors.GREEN)


@app.command()
def organize(
    ignore: bool = typer.Option(
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
    specific: Optional[List[str]] = typer.Option(
        None,
        help="Only move files containing these prefixes."
    ),
    exclude: Optional[List[str]] = typer.Option(
        None,
        help="Ignore all files with these prefixes."
    ),
):
    """
    Organize files that have prefixes.
    """
    try:
        file = get_prefixes_file(ignore)
        data = get_data(file)
        riordinato = Riordinato(Path.cwd())

        # get the amount of files in current directory
        # to later calculate the number of files that were organized
        get_amount_files = lambda: len(
            [f for f in Path.cwd().iterdir() if f.is_file()])
        amount_files_before = get_amount_files()

        for prefix, destination in data.items():
            riordinato.prefixes[prefix] = destination
            # Check that there are no files with the same name
            riordinato.check_files(Path(destination))
        riordinato.movefiles(specific=specific, ignore=exclude)
        
        # Calculate files that were organized
        amount_files_after = get_amount_files()
        typer.echo(f"{amount_files_before - amount_files_after} files were organized")
        
    # If the folder does not exist show this message
    except FileNotFoundError:
        typer.echo(f"The directory '{destination}' does not exist.")
        typer.echo("If you want to delete it put the following command:")
        typer.secho(f"riordinato remove {prefix}", bold=True)
        raise typer.Exit(code=1)
    # One file has the same name as another
    except SameFileError:
        show_common_files(Path.cwd(), Path(destination))
        raise typer.Exit(code=1)


@app.command(name='add')
def add_prefix(
    prefix: str = typer.Argument(
        ...,
        help="The prefix that the file names should have."
    ),
    destination: Path = typer.Argument(
        ...,
        exists=True,
        help="The directory where the files with the prefix will be moved."
    ),
    ignore: bool = typer.Option(
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
):
    """
    Add a new prefix to the json file.
    """
    try:
        file = get_prefixes_file(ignore)
        data = get_data(file)
        Prefix()[prefix] = destination  # check that the prefix is valid

        with open(file, 'w+') as jfile:
            # Add a prefix with an absolute path
            data[prefix] = str(destination.absolute())
            # update the prefixes.json files
            jfile.write(json.dumps(data, ensure_ascii=False, indent=4))

        typer.echo(f"{prefix}:{destination} was added.")
    except InvalidPrefixError:
        # if the prefix is "." or "prefixes" show this message
        prefix_style = typer.style(f"{prefix}", underline=True)
        typer.echo(prefix_style + " is an invalid prefix")
        raise typer.Exit(code=1)


@app.command(name='remove')
def remove_prefix(
    prefixes: List[str] = typer.Argument(
        ...,
        help="The prefixes to be removed from the database."
    ),
    ignore: bool = typer.Option(
        False,
        show_default=False,
        help="Ignore the prefixes.json file inside the directory."
    ),
):
    """
    Remove prefixes.
    """
    file = get_prefixes_file(ignore)
    data = get_data(file)

    with open(file, 'w+') as jfile:
        # Remove the prefixes
        if prefixes[0] == '.':  # "." to remove all prefixes
            data = {}
        else:
            for prefix in prefixes:
                del data[prefix]
        # update the prefixes.json files
        jfile.write(json.dumps(data, ensure_ascii=False, indent=4))


def main():
    app()
