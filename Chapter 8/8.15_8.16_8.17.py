#! python3

print("Task 8.15")

import printing_functions as pf

unprinted_designs = ['elephant', 'car', 'rifle', 'star']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

print("Task 8.16")

from making_sandwiches import make_sandwich as ms

ms.make_snadwich('large', 'pepperoni')
ms.make_snadwich('small', 'pepper', 'cheese', 'onion', 'salami')