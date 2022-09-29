class Aluno:
    def __init__(self, cod, name, registration):
        self.cod = cod
        self.name = name
        self.registration = registration

    def imprimir(self):
        print(f"Código: {self.cod}\nNome: {self.name}\nMatrícula: {self.registration}")