5.4. 集合

>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> fruit = set(basket)               # create a set without duplicates
>>> fruit
set(['orange', 'pear', 'apple', 'banana'])

>>> 'orange' in fruit                 # fast membership testing
True
>>> 'crabgrass' in fruit
False




