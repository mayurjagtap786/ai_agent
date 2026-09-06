import logging
import json
import sqlite3
from click import Group
from litestar.plugins import CLIPlugin
from litestar import Litestar
from config import BASE_DIR


logger = logging.getLogger(__name__)

def flatten_components(components):
        nodes = []
        edges = []

        def process(items, parent_id=None):

            for component in items:

                component_id = component["id"]

                # Remove children from node properties
                properties = {
                    key: value
                    for key, value in component.items()
                    if key != "children"
                }

                nodes.append(
                    (component_id, json.dumps(properties))
                )

                # Create edge from parent -> child
                if parent_id:
                    edges.append(
                        (
                            parent_id,
                            component_id,
                            "HAS_CHILD",
                            None
                        )
                    )
                # Process children
                children = component.get("children", [])
                if children:
                    process(children, component_id)
        process(components)

        return nodes, edges
def save_to_database(nodes,edges):
        connection = sqlite3.connect(BASE_DIR /'backend'/ "database.db")

        try:
            cursor = connection.cursor()

            cursor.execute("PRAGMA foreign_keys = ON")

            cursor.executemany(
                """
                INSERT INTO nodes (id, properties)
                VALUES (?, ?)
                """,
                nodes
            )

            cursor.executemany(
                """
                INSERT INTO edges (
                    from_node,
                    to_node,
                    rel_type,
                    properties
                )
                VALUES (?, ?, ?, ?)
                """,
                edges
            )

            connection.commit()

            logger.info(
                "Graph database loaded: %d nodes, %d edges",
                len(nodes),
                len(edges)
            )

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()

class LoadGraphDatabasePlugin(CLIPlugin):
    """ Add custom management command to the native Litestar CLI. """

    
    
        

    def on_cli_init(self, cli:Group) -> None:
        @cli.command(name='load-graph-db', help='Load Graph database from application.json')

        def send_db(app: Litestar)-> None:
            file_path = BASE_DIR / 'corpus' / 'final' / 'applications.json'
            import json
            with open(file_path,'rb') as f:
                data = json.load(f)
                #print(data)
                results = []
            nodes,edges = flatten_components(data["components"])
            save_to_database(nodes,edges)
            # for node in nodes:
            #     print(node)
            # print("========================================")
            # for edge in edges:
            #     print(edge)
                # for key, values in data.items():
                #     print(key,'->',values)
    


       
                    

            

