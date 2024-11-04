from . import inventory_category_api_blueprint
from fkcommerce.core.schema import CategorySchema
from apifairy import response
from core.models import Category

category_schema = CategorySchema(many=True)

@inventory_category_api_blueprint.route("/category", methods=["GET"])
@response(category_schema)
def category():
    return Category.query.all()