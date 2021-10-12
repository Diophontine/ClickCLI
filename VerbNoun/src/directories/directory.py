
# top level added in main
import os
import shutil
import click


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
