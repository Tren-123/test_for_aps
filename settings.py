ELASTIC_USERNAME = "<your_username>"
ELASTIC_PASSWORD = "<your_password>"
CLOUD_ID = "<your_cloud_id>"
INDEX_NAME = "<index_for_search>"


try:
    from local_settings import *
except ImportError as e:
    print(e)

print(ELASTIC_USERNAME)