import logging

from click import Group

from litestar.plugins import CLIPlugin
from litestar import Litestar

from config import BASE_DIR


logger = logging.getLogger(__name__)




class LoadGraphDatabasePlugin(CLIPlugin):
    """ Add custom management command to the native Litestar CLI. """

    def on_cli_init(self, cli:Group) -> None:
        @cli.command(name='load-graph-db', help='Load Graph database from application.json')

        def send_db(app: Litestar)-> None:
            file_path = BASE_DIR / 'corpus' / 'final' / 'applications.json'
            import json
            with open(file_path,'rb') as f:
                data = json.load(f)
               # print(data)
                applications:dict[str,list] = {}


                for key, values in data.items():
                    print(key,'->',values)

                    for value in values:
                        app_name = value['id']
                        services_list = value['children']

                        if key not in applications:
                            applications[app_name] = []
                        for service in services_list:

                            applications[app_name].append(service)


            print(applications)

