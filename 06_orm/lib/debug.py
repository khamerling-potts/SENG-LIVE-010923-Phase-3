#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()

Pet.create_table()
spot = Pet("spot", "dog", "chihuahua", "feisty")
rex = Pet("rex", "dog", "boxer", "chill")
grace = Pet("grace", "cat", "siamese", "mysterious")

spot.save()
rex.save()
grace.save()

import ipdb; ipdb.set_trace()
