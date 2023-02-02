# import os
# import click


# def register(app):
#     @app.cli.group()
#     def translate():
#         """Translation and localization commands."""
#         pass

#     @translate.command()
#     @click.argument('lang')
#     def init(lang):
#         """Initialize a new language."""
#         if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
#             raise RuntimeError('extract command failed')
#         if os.system(
#                 'pybabel init -i messages.pot -d app/translations -l ' + lang):
#             raise RuntimeError('init command failed')
#         os.remove('messages.pot')

#     @translate.command()
#     def update():
#         """Update all languages."""
#         if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
#             raise RuntimeError('extract command failed')
#         if os.system('pybabel update -i messages.pot -d app/translations'):
#             raise RuntimeError('update command failed')
#         os.remove('messages.pot')

#     @translate.command()
#     def compile():
#         """Compile all languages."""
#         if os.system('pybabel compile -d app/translations'):
#             raise RuntimeError('compile command failed')


import os
import click

def register(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        run_command(f'pybabel extract -F babel.cfg -k _l -o messages.pot .', 'extract command failed')
        run_command(f'pybabel init -i messages.pot -d app/translations -l {lang}', 'init command failed')
        remove_file('messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        run_command('pybabel extract -F babel.cfg -k _l -o messages.pot .', 'extract command failed')
        run_command('pybabel update -i messages.pot -d app/translations', 'update command failed')
        remove_file('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        run_command('pybabel compile -d app/translations', 'compile command failed')

def run_command(command, error_message):
    if os.system(command):
        raise RuntimeError(error_message)

def remove_file(file):
    os.remove(file)
