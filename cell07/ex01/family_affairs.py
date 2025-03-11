def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

# Print the list of red-haired individuals
print(find_the_redheads(dupont_family))