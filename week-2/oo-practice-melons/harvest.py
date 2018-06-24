############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedlesss = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.code = code
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types(file):
    """Returns a list of current melon types."""
    melon_file = open(file)

    all_melon_types = []

    for line in melon_file:
        melon_info = line.rstrip().split("|")
        # Name|code|first harvest|color|pairing|seedless?|bestseller?
        new_melon = MelonType(melon_info[1], int(melon_info[2]), melon_info[3],
                              melon_info[-2], melon_info[-1], melon_info[0])

        pairings = melon_info[-3]  # a string containing all pairings

        pairings = pairings.split(",")

        for item in pairings:
            new_melon.add_pairing(item)

        all_melon_types.append(new_melon)

    # Fill in the rest

    melon_file.close()

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print("{} pairs with".format(melon.name))

        for item in melon.pairings:
            print("- {}".format(item))

        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field_harvested, 
                 harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field_harvested = field_harvested
        self.harvester = harvester 

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field_harvested != 3

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(file, melon_types):
    # assume melon_types is a dictionary created from make_melon_type_lookups
    """Returns a list of Melon objects."""
    all_melons = []
    file = open(file)
    for line in file:
        melon_info = line.rstrip().split("|")
        # code|shape rating|color rating|field|harvester
        code = melon_info[0]
        melon = Melon(melon_types[code], int(melon_info[1]), int(melon_info[2]),
                      int(melon_info[3]), melon_info[4])
        all_melons.append(melon)

    return all_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellable = "Can be Sold"
        else:
            sellable = "Not Sellable"
        print("Harvested by {} from field {:d} {}".format(melon.harvester,
                                                          melon.field_harvested,
                                                          sellable))


melon_types = make_melon_types("harvest_prep.txt")
melon_type_dict = make_melon_type_lookup(melon_types)
melons = make_melons("harvest_data.txt", melon_type_dict)
get_sellability_report(melons)