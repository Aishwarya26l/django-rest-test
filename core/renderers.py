import json

from rest_framework.renderers import JSONRenderer


class JSONRenderer(JSONRenderer):
    charset = 'utf-8'
    
    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error (such as the user can't be authenticated
        # or something similar), `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        if isinstance(data, dict) is True:
            errors = data.get('errors', None)

            # If we receive a `token` key in the response, it will be a
            # byte object. Byte objects don't serializer well, so we need to
            # decode it before rendering the User object.
            token = data.get('token', None)

            if errors is not None:
                if ('exception_class' in data and data['exception_class'] == 'ValidationError'):
                    error_message = {
                        'errors': data['errors']
                    }
                else:
                    error_message = {
                        'errors': {
                            'message': data['errors']['detail'] if 'detail' in data['errors'] else data['errors']
                        }
                    }

                # As mentioned above, we will let the default JSONRenderer handle
                # rendering errors.
                return super(JSONRenderer, self).render(error_message)
            
            if token is not None and isinstance(token, bytes):
                # We will decode `token` if it is of type
                # bytes.
                data['token'] = token.decode('utf-8')
                
        # Finally, we can render our data under the "user" namespace.
        return json.dumps({
            'data': data
        })