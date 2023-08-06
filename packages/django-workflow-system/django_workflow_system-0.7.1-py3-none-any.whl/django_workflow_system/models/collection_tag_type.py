"""Django model definition."""
import uuid

from django.db import models

from django_workflow_system.models.abstract_models import CreatedModifiedAbstractModel


class WorkflowCollectionTagType(CreatedModifiedAbstractModel):
    """Types that can be assigned to tags."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)

    class Meta:
        db_table = "workflow_system_collection_tag_type"
        verbose_name_plural = "Workflow Collection Tag Types"

    def __str__(self):
        return self.type
