from datetime import datetime

def calcular_idade(data_nasc: str):
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = datetime.today()
    anos = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        anos -= 1
    return anos

if __name__ == "__main__":
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    print(f"Idade atual: {calcular_idade(data)} anos")
