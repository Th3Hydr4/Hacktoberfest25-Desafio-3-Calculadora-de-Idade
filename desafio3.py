from datetime import datetime

def calcular_idade(data_nasc: str):
    """Calcula idade completa em anos, meses e dias."""
    nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
    hoje = datetime.today()

    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day

    if dias < 0:
        meses -= 1
        dias += 30  # aproximação simples
    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

if __name__ == "__main__":
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    anos, meses, dias = calcular_idade(data)
    print(f"Idade atual: {anos} anos, {meses} meses e {dias} dias.")
