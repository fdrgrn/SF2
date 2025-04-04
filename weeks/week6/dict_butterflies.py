def new_sighting(butterfly_dict, sighting):
    butterfly_dict[sighting] = butterfly_dict.get(sighting, 0) + 1
    
butterflies = {'Monarch' = 4, 'Painted Lady' = 12}

for kind, count in butterflies.item():
    print(f'{kind}: {count}')