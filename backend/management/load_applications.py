from click import Group

from litestar.plugins import CLIPlugin
from litestar import Litestar

from config import BASE_DIR


class LoadGraphDatabasePlugin(CLIPlugin):
    """ Add custom management command to the native Litestar CLI. """

    def on_cli_init(self, cli:Group) -> None:
        @cli.command(name='load-graph-db', help='Load Graph database from application.json')

        def send_db(app: Litestar)-> None:
            file_path = BASE_DIR / 'corpus' / 'final' / 'applications.json'
            import json
            with open(file_path,'rb') as f:
                data = json.load(f)

