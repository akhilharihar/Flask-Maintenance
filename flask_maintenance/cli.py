import os
import click
from flask import current_app
from flask.cli import with_appcontext


@click.group()
def maintenance():
    pass


@maintenance.command()
@with_appcontext
def enable():
    result = False
    ins_path = current_app.instance_path

    if not os.path.exists(ins_path):
        try:
            os.makedirs(ins_path)
        except Exception as e:
            click.echo(e)
            return False

    try:
        open(os.path.join(ins_path, 'under_maintenance'), 'w').close()
        result = True
    except Exception as e:
        click.echo(e)

    if result:
        click.echo('maintenance mode enabled.')
        return True

    return False


@maintenance.command()
@with_appcontext
def disable():
    ins_path = current_app.instance_path
    main_file = os.path.join(ins_path, 'under_maintenance')

    if os.path.exists(main_file) and os.path.isfile(main_file):
        try:
            os.remove(main_file)
        except Exception as e:
            click.echo(e)
            return False

    click.echo('maintenance mode disabled.')
