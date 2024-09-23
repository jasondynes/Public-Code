Feature: Product Basket (JIRA: JD-1234)
  As a gardener,
  I want to carry products in a basket,
  So that I don't drop them all.


  Scenario Outline: Add products to a basket
    Given the basket has "<initial>" products
    When "<some>" products are added to the basket
    Then the basket contains "<total>" products

    Examples:
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |

  Scenario Outline: Remove products from the basket
    Given the basket has "<initial>" products
    When "<some>" products are removed from the basket
    Then the basket contains "<total>" products

    Examples:
      | initial | some | total |
      | 8       | 3    | 5     |
      | 10      | 4    | 6     |
      | 7       | 0    | 7     |

