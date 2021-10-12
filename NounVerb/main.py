import click
from src.files.file import file
from src.directories.directory import directory


@click.group()
@click.pass_context
def cli(ctx):
    pass

cli.add_command(file)
cli.add_command(directory)
