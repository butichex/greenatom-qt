from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from db import create_table, insert_data

transport = AIOHTTPTransport(url="https://spacex-production.up.railway.app/")

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    query ExampleQuery {
      launches {
        details
          rocket {
            rocket_name
          }
      mission_name
      mission_id
    }
  }
  """
)


def get_data():
    result = client.execute(query)
    [insert_data(r['details'], r['rocket']['rocket_name'],
     r['mission_name'], r['mission_id'][0]) for r in result['launches']]


if __name__ == '__main__':
    create_table()
    get_data()
