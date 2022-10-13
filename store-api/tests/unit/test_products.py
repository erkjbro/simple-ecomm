import json

from app.products.src.handler import lambda_handle


def test_products(load_json):
    """
    Test the product handler
    :param load_json:
    :return:
    """
    event, context = {}, {}
    lambda_handle(event, context)

    product = load_json('sample.json')

    print(json.dumps(product, indent=True))

    # assert 1 == 2
