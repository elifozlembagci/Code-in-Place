# Personel sözlüğü
employees = {
    "E001": {
        "name": "Alice Smith",
        "address": "123 Main Street, Springfield",
        "DOB": "1990-05-12"
    },
    "E002": {
        "name": "Bob Johnson",
        "address": "456 Elm Street, Metropolis",
        "DOB": "1985-09-30"
    }
}

# İkinci çalışanın adresi (E002)
second_employee_address = employees["E002"]["address"]
print("2. çalışan adresi:", second_employee_address)



# Gen ekspresyonu sözlüğü
gene_expression = {
    "GeneA": [2.3, 3.1, 2.8, 4.0, 3.3],
    "GeneB": [1.2, 2.5, 3.6, 2.9, 4.1],
    "GeneC": [5.0, 4.7, 3.3, 3.8, 2.5]
}

# 2. gen: GeneB, 4. örnek: index 3
expression_value = gene_expression["GeneB"][3]
print("2. genin 4. örnekteki ekspresyonu:", expression_value)
