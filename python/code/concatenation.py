import modu

c = modu.py_script
hello = "Hello"
world = "World"
exclamation = "!"


print(hello+world+exclamation)
print(" ".join([hello, world, exclamation]))
print(f"{hello} {world} {exclamation}")

print(c("concatenation.py"))