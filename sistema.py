class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        if self.idade < 18:
            self.set_idade()

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade


    def set_idade(self):
        if self.idade < 18:
            while True:
                self.idade = int(input("Digite uma idade maior ou igual que 18: "))
                if self.idade >= 18:
                    print(f'Idade válida e alterada com sucesso: {self.idade}')
                    print(90 * '--')
                    break


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.__salario = salario

    def get_salario(self):
        return self.__salario
    
    def set_salario(self, novo_salario):
        self.__salario = novo_salario
        print(f'Novo salario alterado com sucesso')

    def calcular_salario_anual(self):
        return self.__salario * 12
    
p1 = Funcionario("Fábio", 15, 3500)
p2 = Funcionario("Diogo", 21, 2500)
p3 = Funcionario("Roebrto", 33, 4500)


class Departamento:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for pessoa in self.funcionarios:
            print(f'Nome: {pessoa.get_nome()} \nIdade: {pessoa.get_idade()} \nSalário: {pessoa.get_salario()}')
            print(90 * '--')
    
    def calcular_total_salarios_anuais(self):
        for trabalhador in self.funcionarios:
            calculando = f'{trabalhador.get_nome()}: ganha em um ano {trabalhador.calcular_salario_anual()}'
            print(90 * '--')
            print(calculando)


d1 = Departamento()
d1.adicionar_funcionarios(p1)
d1.adicionar_funcionarios(p2)
d1.adicionar_funcionarios(p3)

d1.listar_funcionarios()
d1.calcular_total_salarios_anuais()
        
