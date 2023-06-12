from elasticsearch import Elasticsearch
from elastic_search.core.config import SETTINGS


ELASTIC_CLIENT = Elasticsearch(hosts=f"{SETTINGS.ELASTIC_HOST}:{SETTINGS.ELASTIC_PORT}")