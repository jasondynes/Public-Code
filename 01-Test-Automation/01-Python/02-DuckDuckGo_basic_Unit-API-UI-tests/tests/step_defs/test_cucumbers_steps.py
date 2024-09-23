from pytest_bdd import scenarios, parsers, given, when, then

from cucumbers import ProductBasket

EXTRA_TYPES = {'Number': int, }

CONVERTERS = {'initial': int,'some': int, 'total': int, }

scenarios('../features/unittest.feature', example_converters=CONVERTERS)

@given(parsers.cfparse('the basket has "{initial:Number}" products', extra_types=EXTRA_TYPES))
@given('the basket has "<initial>" products')
def basket(initial):
    return ProductBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" products are added to the basket', extra_types=EXTRA_TYPES))
@when('"<some>" products are added to the basket')
def add_products(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" products are removed from the basket', extra_types=EXTRA_TYPES))
@when('"<some>" products are removed from the basket')
def remove_products(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" products', extra_types=EXTRA_TYPES))
@then('the basket contains "<total>" products')
def basket_has_total(basket, total):
    assert basket.count == total
