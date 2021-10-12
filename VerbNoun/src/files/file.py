
# top level added in main
import os
import shutil
import click
from pathlib import Path


@click.group()
@click.pass_context
def create(ctx):
    pass

# top level added in main
@click.group()
@click.pass_context
def delete(ctx):
    pass

# top level added in main
@click.group()
@click.pass_context
def get(ctx):
    pass

@create.command("file")
@click.pass_context
@click.argument('file_name')
@click.option('-f', '--force',is_flag=True, help="Force creation even if file exists")
def create_file(ctx,file_name,force):
    """Create file"""
    Path(file_name).touch()

@delete.command("file")
@click.pass_context
@click.argument('file_name')
@click.option('-f', '--force',is_flag=True, help="Force deletion even if there are errors")
def delete_file(ctx,file_name,force):
    """Delete file"""
    cwd = os.getcwd()
    os.remove(file_name)


@get.command("file")
@click.pass_context
@click.argument('file_name')
def get_file(ctx,file_name):
    """List file contents"""
    f = open(file_name, "r")
    print(f.read())
