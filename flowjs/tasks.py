from __future__ import absolute_import
from celery import shared_task
from .models import FlowFile


@shared_task
def join_chunks_task(flow_file_identifier):
    print('starting join task'),
    flow_file = FlowFile.objects.get(identifier=flow_file_identifier)
    return flow_file._join_chunks()


@shared_task
def delete_chunks_task(flow_file_identifier):
    print('starting delete task'),
    flow_file = FlowFile.objects.get(identifier=flow_file_identifier)
    return flow_file._delete_chunks()
