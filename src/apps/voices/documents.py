from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from apps.voices.models import Record, RecordHistory

#
# @registry.register_document
# class RecordHistoryDocument(Document):
#     class Index:
#         name = 'record_history'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
#
#     class Django:
#         model = RecordHistory
#         fields = ['id', 'record', 'user']
