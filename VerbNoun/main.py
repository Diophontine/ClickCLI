import click
from click import CommandCollection
from src.directories import directory
from src.files import file


@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.group()
@click.pass_context
def create(ctx):
    pass

@cli.group()
@click.pass_context
def delete(ctx):
    pass

@cli.group()
@click.pass_context
def get(ctx):
    pass



# add to main parent from sub modules
create_collection =  CommandCollection(sources=[file.create, directory.create])
get_collection  = CommandCollection(sources=[file.get, directory.get])
delete_collection  = CommandCollection(sources=[file.delete, directory.delete])

def merge_commands(group, command_collection:CommandCollection):
    """ """
    new_commands = {}
    command_sources = command_collection.sources
    for group in command_sources:
        for command_name,command in group.commands.items():
            new_commands[command_name] = command

    group.commands = new_commands
    return group


cli.commands["create"] = merge_commands(cli.commands["create"], create_collection)
cli.commands["delete"] = merge_commands(cli.commands["delete"], delete_collection)
cli.commands["get"] = merge_commands(cli.commands["get"], get_collection)

if __name__ == '__main__':
    cli()