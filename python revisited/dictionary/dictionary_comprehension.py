products = {
    'bottle': 15,
    'pen': 20
}

new_dictionary = {key: value*2 for key, value in products.items()}

print(new_dictionary)


filtered_dictionary = {key: value for key, value in products.items() if value>15}

print(filtered_dictionary)