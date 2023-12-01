#! /usr/bin/env python3

places = ['New Mexico', 'Illinois', 'Missouri']
places += ['test +=']
print(f"US places lived: {places}")

# but wait, I was born somewhere else, and also lived in Europe
places.insert(0,'Philippines')
places.insert(2,'Italy')
print(f"Global places I've lived: {places}")

# well that was when i was a chlid, I lived in new places as an adult
places_as_adult = ['Colorado','Florida','Georgia','Pennsylvania']
places.extend(places_as_adult)
print(f"Places lived as adult too: {places}")

# places I want to live:
want = ["Germany","Missouri","France","Mars","Australia"]
places.extend(want)
print(f"Place I also want to live too: {places}")

# but wait... nevermind mars
places.remove('Mars')
print(f"Nevermind, remove other planets: {places}")


# remove last item... to many desires
places.pop()
print(f"Remove last place, too many: {places}")

# remove duplicate, apparenlty have to convert to set and back to list
set_places = set(places)
places = list(set_places)
print(f"Remove duplicate places: {places}")

# convert list into string for ease of read
str_places = ', '. join(places)
print(f"My places: {str_places}")

# wait, I'm weird, i like the list version better...
list_places = str_places.split(', ')
print(f"I'm weird, I like the other format better... {list_places}")

# don't want to go
do_not = ['Hell','Purgatory']

# oh, and look... a list of lists
list_of_lists = [want, do_not]
print(f"List of Lists: {list_of_lists}")