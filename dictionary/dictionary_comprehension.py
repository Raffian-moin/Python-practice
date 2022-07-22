# dictionary comprehension is used to transform or filter items and return a new dictionary

# Transform
country_dictionary = {
    "Bangladesh": 123,
    "Thailand": 345
}

new_country_dictionary = {key: value * 2 for (key, value) in  country_dictionary.items()}

print(new_country_dictionary)

# Filter

new_filtered_dictionary = { key: value for (key, value) in country_dictionary.items() if value > 150} 

print(new_filtered_dictionary)