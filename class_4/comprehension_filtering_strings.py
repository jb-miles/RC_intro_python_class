print("Rob".startswith("R"))
first_names = ["John", "Robin", "Emma", "Michael", "Ralph", "Sophia", "Daniel"]
r_names = [name for name in first_names if name.startswith("R")]
print(r_names)
n_enders = [name for name in first_names if name.endswith("n")]
print(n_enders)
