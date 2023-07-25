from collections import defaultdict

# factory function


def default_factory():
    return "This is not defined."


d = defaultdict(default_factory)
d["a"] = 1
d["b"] = 2

print(d["a"], d["b"], d["c"])  # 1 2 This is not defined.


Harry = defaultdict(lambda: "Wrong key!!")
Harry["name"] = "Harry Potter"
Harry["age"] = 16

print(Harry["name"], Harry["age"], Harry["family"])
# Harry Potter 16 Wrong key!!
