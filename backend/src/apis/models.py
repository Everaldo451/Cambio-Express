from django.db import models
from backend.core.types.apis import APIParamValueTypes

class APIConfig(models.Model):
    HTTP_METHODS = [
        ('GET', 'GET'),
        ('POST', 'POST')
    ]
    name = models.CharField(max_length=100)
    base_url = models.CharField(max_length=250)
    endpoint = models.CharField(max_length=100)
    api_key = models.CharField(max_length=150, null=True, blank=True)
    headers = models.JSONField(null=True, blank=True)
    http_method = models.CharField(choices=HTTP_METHODS, default='GET')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)


class APIParam(models.Model):
    api_config = models.ForeignKey(
        'apis.APIConfig',
        models.CASCADE,
        related_name='params'
    )
    name = models.CharField(max_length=50)
    required = models.BooleanField(default=False)
    value_type = models.CharField(
        choices=[(typ.value, typ.value.title()) for typ in APIParamValueTypes]
    )
    format = models.CharField(max_length=50, blank=True, null=True)