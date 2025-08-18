from django.core.exceptions import ValidationError

FIELD_TYPES = {
    'query_params': (list, type(None)),
    'url': str,
    'api_key': (str, type(None)),
}

def get_type_name(typ):
    if isinstance(typ, tuple):
        return " or ".join(t.__name__ for t in typ)
    return typ.__name__


def validate_keys_type(value:dict):
    if not isinstance(value, dict) or not value:
        raise ValidationError("API config must be a dictionary.")
    
    for field, typ in FIELD_TYPES.items():
        if field not in value:
            raise ValidationError(f"Missing field: {field}")
        
        field_value = value.get(field)
        if not isinstance(field_value, typ):
            raise ValidationError(f'{field} must be {get_type_name(typ)}.')


def validate_parameter(value):

    if not isinstance(value, dict):
        raise ValidationError('parameter must be a dictonary.')
    params_fields_types = {
        'name': str,
        'type': str
    }
    for field, typ in params_fields_types.items():
        if field not in value:
            raise ValidationError(f"Missing field: {field}")
        
        field_value = value.get(field)
        if not isinstance(field_value, typ):
            raise ValidationError(f'parameter {field} must be {get_type_name(typ)}')
        
    PARAMETER_TYPES = ['string', 'integer', 'float', 'list', 'date']
    if value['type'] not in PARAMETER_TYPES:
        raise ValidationError(f'parameter type must be one of: {", ".join(PARAMETER_TYPES)}')


def validate_parameters(value:dict):
    params = value.get('query_params')
    if params is None:
        return
    if not isinstance(params, list):
        raise ValidationError('parameters field invalid format')
    for param in params:
        validate_parameter(param)



