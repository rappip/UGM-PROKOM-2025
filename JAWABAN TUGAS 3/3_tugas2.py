# Contoh data
data = ["Python", 42, 3.14, True, "123"]

# Fungsi untuk menentukan tipe literal
def determine_literal_type(value):
    if isinstance(value, bool):
        return "Boolean"
    elif isinstance(value, (int, float)):
        return "Numeric"
    elif isinstance(value, str):
        return "String"
    else:
        return "Unknown"

# Menampilkan tipe dari masing-masing data
for item in data:
    print(f"{item}: {determine_literal_type(item)}")