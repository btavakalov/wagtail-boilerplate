from drf_yasg.inspectors.view import SwaggerAutoSchema
from inflection import camelize


class CamelCaseOperationIDAutoSchema(SwaggerAutoSchema):
    def get_operation_id(self, operation_keys=None):
        operation_id = super(CamelCaseOperationIDAutoSchema, self).get_operation_id(operation_keys)
        return camelize(operation_id, uppercase_first_letter=False)
