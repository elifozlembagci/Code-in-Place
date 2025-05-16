# Gen ekspresyon sözlüğü (tek bir değer/gene için örnek)
gene_expression = {
    "SYF2": 1.5,
    "FBX04": 2.1,
    "ATF2": 0.8,
    "PLK1": -1.2,
    "HUS1B": -0.5
}

# Kontrol yapıları
if "SYF2" in gene_expression and "FBX04" in gene_expression and gene_expression["SYF2"] > 0 and gene_expression["FBX04"] > 0:
    print("GO:1")
elif "ATF2" not in gene_expression or ("PLK1" in gene_expression and gene_expression["PLK1"] < 0):
    print("GO:2")
elif ("HUS1B" in gene_expression and gene_expression["HUS1B"] < 0) or "SYF2" not in gene_expression:
    print("GO:3")
else:
    print("GO:4")
# Bu kod, gen ekspresyon değerlerine göre belirli koşulları kontrol eder ve uygun GO (Gene Ontology) terimini yazdırır.



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
for emp_id, info in employees.items():
    print("Employee ID:", emp_id)
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    print("----")





gene_expression = {
    "GeneA": [2.3, 3.1, 2.8, 4.0, 3.3],
    "GeneB": [1.2, 2.5, 3.6, 2.9, 4.1],
    "GeneC": [5.0, 4.7, 3.3, 3.8, 2.5]
}
for gene, expressions in gene_expression.items():
    print("Gene:", gene)
    for i, value in enumerate(expressions):
        print(f"  Sample {i+1}: {value}")
    print("----")
