ELASTIC_USERNAME = "<your_elastic_username>"
ELASTIC_PASSWORD = "<your_elastic_password>"
CLOUD_ID = "<your_elastic_cloud_id>"
INDEX_NAME = "<elastic_index_for_search>"


try:
    from local_settings import *
except ImportError as e:
    print(e)
    