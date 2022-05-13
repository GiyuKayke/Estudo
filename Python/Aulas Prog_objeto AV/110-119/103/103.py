class A:
    vc = "base"
    def __init__(self):
        self.vc = "alterado"
a1 = A()
a2 = A()

a1.vc = "Alterado em var"

print(a1.vc)
print(a2.vc)
print(A.vc)