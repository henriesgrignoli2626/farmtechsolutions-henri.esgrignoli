"""
FarmTech Solutions - Sistema de gestao de plantio
Disciplina: Dev / Formacao Social - FIAP

Requisito (a): suporta 2 culturas -> Laranja e Cana-de-acucar
Requisito (b): calculo de area de plantio, com figura geometrica diferente por cultura
Requisito (c): calculo do manejo de insumos (produto + quantidade necessaria)
Requisito (d): dados organizados em vetor (lista de dicionarios) -> variavel `culturas`
Requisito (e): menu com entrada, saida, atualizacao, delecao de dados e opcao de sair
Requisito (f): uso de rotinas de loop (while/for) e decisao (if/elif)
"""

# Requisito (d): vetor principal. Cada posição guarda um dicionário representando uma cultura.
culturas = []


# ---------- Funções auxiliares de entrada validada ----------

def ler_float(mensagem):
    """Lê um número decimal do usuário, repetindo até ser válido (rotina de loop)."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero < 0:
                print("O valor não pode ser negativo. Tente novamente.")
                continue
            return numero
        except ValueError:
            print("Valor inválido. Digite um número (ex: 12.5).")


def ler_int(mensagem):
    """Lê um número inteiro do usuário, repetindo até ser válido (rotina de loop)."""
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def ler_opcao_cultura():
    """Pede o tipo de cultura (1 ou 2), repetindo até o usuário digitar uma opção válida."""
    while True:
        print("1 - Laranja (área em retângulo, insumo: calda bordalesa)")
        print("2 - Cana-de-açúcar (área em trapézio, insumo: inseticida)")
        opcao = input("Escolha a cultura: ").strip()
        if opcao in ("1", "2"):
            return opcao
        print("Opção inválida. Digite 1 ou 2.\n")


# ---------- Cálculos ----------

def calcular_area(cultura):
    """Requisito (b): calcula a área de plantio de acordo com a figura geométrica de cada cultura."""
    if cultura["nome"] == "Laranja":
        # retângulo: base x altura
        return cultura["base"] * cultura["altura"]
    elif cultura["nome"] == "Cana-de-acucar":
        # trapézio: ((base maior + base menor) / 2) x altura
        return ((cultura["base_maior"] + cultura["base_menor"]) / 2) * cultura["altura"]
    return 0


def calcular_insumo(cultura):
    """
    Requisito (c): calcula o total de insumo necessário, em litros.
    Segue a lógica: total de metros (ruas x comprimento de cada rua) x taxa por metro.
    """
    total_metros = cultura["numero_ruas"] * cultura["comprimento_rua"]
    total_ml = total_metros * cultura["taxa_ml_por_metro"]
    return total_ml / 1000  # converte mL para litros


# ---------- Funções do menu ----------

def cadastrar_cultura():
    """Opção 1 - Entrada de dados: cadastra uma nova cultura no vetor."""
    print("\n--- Cadastro de cultura ---")
    opcao = ler_opcao_cultura()

    if opcao == "1":
        cultura = {
            "nome": "Laranja",
            "base": ler_float("Base do retângulo (m): "),
            "altura": ler_float("Altura do retângulo (m): "),
            "insumo": "Calda bordalesa",
            "taxa_ml_por_metro": 300,
        }
    else:
        cultura = {
            "nome": "Cana-de-acucar",
            "base_maior": ler_float("Base maior do trapézio (m): "),
            "base_menor": ler_float("Base menor do trapézio (m): "),
            "altura": ler_float("Altura do trapézio (m): "),
            "insumo": "Inseticida",
            "taxa_ml_por_metro": 200,
        }

    cultura["numero_ruas"] = ler_int("Quantas ruas (linhas de plantio) a lavoura tem? ")
    cultura["comprimento_rua"] = ler_float("Comprimento de cada rua (m): ")

    cultura["area"] = calcular_area(cultura)
    cultura["total_insumo_litros"] = calcular_insumo(cultura)

    culturas.append(cultura)
    print(f"\nCultura '{cultura['nome']}' cadastrada com sucesso na posição {len(culturas) - 1}!")


def listar_culturas():
    """Opção 2 - Saída de dados: mostra todas as culturas cadastradas e um resumo geral."""
    print("\n--- Culturas cadastradas ---")
    if not culturas:
        print("Nenhuma cultura cadastrada ainda.")
        return

    area_total = 0
    insumo_total = 0

    # Requisito (f): percorre o vetor inteiro com um loop for
    for i, cultura in enumerate(culturas):
        total_metros = cultura["numero_ruas"] * cultura["comprimento_rua"]
        print(f"\nPosição {i} - {cultura['nome']}")
        print(f"  Área de plantio: {cultura['area']:.2f} m²")
        print(f"  Ruas: {cultura['numero_ruas']} x {cultura['comprimento_rua']:.2f} m = {total_metros:.2f} m totais")
        print(f"  Insumo: {cultura['insumo']} ({cultura['taxa_ml_por_metro']} mL/metro)")
        print(f"  Total de insumo necessário: {cultura['total_insumo_litros']:.2f} litros")

        area_total += cultura["area"]
        insumo_total += cultura["total_insumo_litros"]

    print("\n--- Resumo geral ---")
    print(f"Área total plantada: {area_total:.2f} m²")
    print(f"Total geral de insumo: {insumo_total:.2f} litros")


def atualizar_cultura():
    """Opção 3 - Atualização de dados numa posição qualquer do vetor (todos os campos)."""
    listar_culturas()
    if not culturas:
        return

    posicao = ler_int("\nDigite a posição da cultura que deseja atualizar: ")
    if posicao < 0 or posicao >= len(culturas):
        print("Posição inválida.")
        return

    cultura = culturas[posicao]
    print(f"Atualizando dados de '{cultura['nome']}' (posição {posicao}).")

    # Atualiza os campos de área conforme a figura geométrica da cultura
    if cultura["nome"] == "Laranja":
        cultura["base"] = ler_float("Nova base do retângulo (m): ")
        cultura["altura"] = ler_float("Nova altura do retângulo (m): ")
    else:
        cultura["base_maior"] = ler_float("Nova base maior do trapézio (m): ")
        cultura["base_menor"] = ler_float("Nova base menor do trapézio (m): ")
        cultura["altura"] = ler_float("Nova altura do trapézio (m): ")

    # Atualiza os campos de manejo de insumo
    cultura["numero_ruas"] = ler_int("Novo número de ruas: ")
    cultura["comprimento_rua"] = ler_float("Novo comprimento de cada rua (m): ")
    cultura["taxa_ml_por_metro"] = ler_float("Nova taxa de insumo (mL/metro): ")

    # Recalcula tudo com os novos valores
    cultura["area"] = calcular_area(cultura)
    cultura["total_insumo_litros"] = calcular_insumo(cultura)

    print("Cultura atualizada com sucesso!")


def deletar_cultura():
    """Opção 4 - Deleção de dados do vetor."""
    listar_culturas()
    if not culturas:
        return

    posicao = ler_int("\nDigite a posição da cultura que deseja deletar: ")
    if posicao < 0 or posicao >= len(culturas):
        print("Posição inválida.")
        return

    removida = culturas.pop(posicao)
    print(f"Cultura '{removida['nome']}' removida com sucesso!")


def menu():
    """Requisito (e) e (f): loop principal do menu, com decisão para cada opção escolhida."""
    while True:
        print("\n===== FarmTech Solutions =====")
        print("1 - Cadastrar cultura (entrada de dados)")
        print("2 - Listar culturas (saída de dados)")
        print("3 - Atualizar cultura")
        print("4 - Deletar cultura")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cultura()
        elif opcao == "2":
            listar_culturas()
        elif opcao == "3":
            atualizar_cultura()
        elif opcao == "4":
            deletar_cultura()
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
