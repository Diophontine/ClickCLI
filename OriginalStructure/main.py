
# top level added in main
import os
import shutil
import click
from pathlib import Path

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.group()
@click.pass_context
def create(ctx):
    pass

# top level added in main
@cli.group()
@click.pass_context
def delete(ctx):
    pass

# top level added in main
@cli.group()
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

@create.command("directory")
@click.pass_context
@click.argument('directory_name')
@click.option('-f', '--force',is_flag=True, help="Force creation even if directory exists")
def create_directory(ctx,directory_name,force):
    """Create directory"""
    os.makedirs(directory_name,exist_ok=force)

@delete.command("directory")
@click.pass_context
@click.argument('directory_name')
@click.option('-f', '--force',is_flag=True, help="Force deletion even if there are errors")
def delete_directory(ctx,directory_name,force):
    """Delete directory"""
    shutil.rmtree(directory_name, ignore_errors=force)


@get.command("directory")
@click.pass_context
@click.argument('directory_name')
def get_directory(ctx,directory_name):
    """List directory contents"""
    cwd = os.getcwd()
    for x in os.listdir(os.path.join(cwd,directory_name)):
        print(x)

if __name__ == '__main__':
    cli()