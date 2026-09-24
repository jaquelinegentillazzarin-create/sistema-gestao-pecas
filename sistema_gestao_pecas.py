# ============================================================
# Sistema de Gestão de Peças, Qualidade e Armazenamento
# Desafio de Automação Digital - Algoritmos e Lógica de Programação
# ============================================================

# Listas principais do sistema
pecas = []                  # Lista de todas as peças cadastradas (dicts)
caixas_fechadas = []        # Lista de caixas já fechadas (cada caixa = lista de IDs)
caixa_atual = []            # Caixa aberta no momento (lista de IDs)
CAPACIDADE_CAIXA = 10       # Capacidade máxima de cada caixa


def validar_peca(peso, cor, comprimento):
    """
    Avalia se a peça atende aos critérios de qualidade.
    Retorna: (aprovada: bool, motivos: list)
    """
    motivos = []

    if not (95 <= peso <= 105):
        motivos.append("Peso fora do intervalo permitido (95g - 105g)")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida (deve ser azul ou verde)")

    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora do intervalo permitido (10cm - 20cm)")

    aprovada = len(motivos) == 0
    return aprovada, motivos


def buscar_peca_por_id(id_peca):
    """Retorna a peça (dict) pelo ID ou None se não encontrar."""
    for peca in pecas:
        if peca["id"] == id_peca:
            return peca
    return None


def cadastrar_peca():
    """Opção 1 - Cadastrar nova peça"""
    print("\n" + "="*50)
    print(" CADASTRAR NOVA PEÇA")
    print("="*50)

    id_peca = input("Digite o ID da peça: ").strip()

    # Verifica se o ID já existe
    if buscar_peca_por_id(id_peca):
        print(f"\n[ERRO] Já existe uma peça com o ID '{id_peca}'.")
        return

    # Entrada do peso com validação
    try:
        peso = float(input("Digite o peso (em gramas): ").replace(",", "."))
    except ValueError:
        print("\n[ERRO] Peso inválido. Digite um número.")
        return

    cor = input("Digite a cor (azul ou verde): ").strip()

    # Entrada do comprimento com validação
    try:
        comprimento = float(input("Digite o comprimento (em cm): ").replace(",", "."))
    except ValueError:
        print("\n[ERRO] Comprimento inválido. Digite um número.")
        return

    # Validação de qualidade
    aprovada, motivos = validar_peca(peso, cor, comprimento)

    # Cria o dicionário da peça
    nova_peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor.lower(),
        "comprimento": comprimento,
        "status": "aprovada" if aprovada else "reprovada",
        "motivos": motivos
    }

    pecas.append(nova_peca)

    if aprovada:
        caixa_atual.append(id_peca)
        print(f"\n[OK] Peça '{id_peca}' APROVADA e adicionada à caixa atual.")
        print(f"     Peças na caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")

        # Verifica se a caixa encheu
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("\n*** CAIXA FECHADA! Capacidade máxima atingida. ***")
            print(f"*** Nova caixa iniciada. Total de caixas fechadas: {len(caixas_fechadas)} ***")
    else:
        print(f"\n[X] Peça '{id_peca}' REPROVADA.")
        print("    Motivos:")
        for motivo in motivos:
            print(f"    - {motivo}")


def listar_pecas():
    """Opção 2 - Listar peças aprovadas e reprovadas"""
    print("\n" + "="*50)
    print(" LISTA DE PEÇAS")
    print("="*50)

    if not pecas:
        print("Nenhuma peça cadastrada ainda.")
        return

    aprovadas = [p for p in pecas if p["status"] == "aprovada"]
    reprovadas = [p for p in pecas if p["status"] == "reprovada"]

    print(f"\n--- PEÇAS APROVADAS ({len(aprovadas)}) ---")
    if aprovadas:
        for p in aprovadas:
            print(f"  ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    else:
        print("  Nenhuma peça aprovada.")

    print(f"\n--- PEÇAS REPROVADAS ({len(reprovadas)}) ---")
    if reprovadas:
        for p in reprovadas:
            print(f"  ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
            print(f"       Motivos: {', '.join(p['motivos'])}")
    else:
        print("  Nenhuma peça reprovada.")


def remover_peca():
    """Opção 3 - Remover peça cadastrada"""
    print("\n" + "="*50)
    print(" REMOVER PEÇA")
    print("="*50)

    if not pecas:
        print("Nenhuma peça cadastrada para remover.")
        return

    id_peca = input("Digite o ID da peça que deseja remover: ").strip()
    peca = buscar_peca_por_id(id_peca)

    if not peca:
        print(f"\n[ERRO] Peça com ID '{id_peca}' não encontrada.")
        return

    # Remove da lista principal
    pecas.remove(peca)

    # Remove da caixa atual (se estiver lá)
    if id_peca in caixa_atual:
        caixa_atual.remove(id_peca)
        print(f"Peça removida também da caixa atual.")

    # Remove das caixas fechadas (se estiver em alguma)
    for caixa in caixas_fechadas:
        if id_peca in caixa:
            caixa.remove(id_peca)
            print(f"Peça removida de uma caixa fechada.")

    # Remove caixas que ficaram vazias após a remoção
    caixas_fechadas[:] = [c for c in caixas_fechadas if len(c) > 0]

    print(f"\n[OK] Peça '{id_peca}' removida com sucesso.")


def listar_caixas_fechadas():
    """Opção 4 - Listar caixas fechadas"""
    print("\n" + "="*50)
    print(" CAIXAS FECHADAS")
    print("="*50)

    if not caixas_fechadas:
        print("Nenhuma caixa fechada ainda.")
    else:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            print(f"\nCaixa #{i} ({len(caixa)} peças):")
            for id_peca in caixa:
                p = buscar_peca_por_id(id_peca)
                if p:
                    print(f"  - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
                else:
                    print(f"  - ID: {id_peca} (dados não encontrados)")

    # Mostra também a caixa atual (aberta)
    print(f"\n--- CAIXA ATUAL (aberta) ---")
    if caixa_atual:
        print(f"Peças na caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")
        for id_peca in caixa_atual:
            p = buscar_peca_por_id(id_peca)
            if p:
                print(f"  - ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    else:
        print("Caixa atual vazia.")


def gerar_relatorio():
    """Opção 5 - Gerar relatório final consolidado"""
    print("\n" + "="*60)
    print(" RELATÓRIO FINAL CONSOLIDADO")
    print("="*60)

    total_aprovadas = len([p for p in pecas if p["status"] == "aprovada"])
    total_reprovadas = len([p for p in pecas if p["status"] == "reprovada"])
    total_pecas = len(pecas)

    # Quantidade de caixas utilizadas (fechadas + atual se tiver peças)
    qtd_caixas = len(caixas_fechadas)
    if caixa_atual:
        qtd_caixas += 1  # conta a caixa aberta também

    print(f"\nTotal de peças cadastradas : {total_pecas}")
    print(f"Total de peças APROVADAS   : {total_aprovadas}")
    print(f"Total de peças REPROVADAS  : {total_reprovadas}")
    print(f"Quantidade de caixas usadas: {qtd_caixas}")
    print(f"  - Caixas fechadas        : {len(caixas_fechadas)}")
    print(f"  - Caixa atual (aberta)   : {'Sim (' + str(len(caixa_atual)) + ' peças)' if caixa_atual else 'Não (vazia)'}")

    if total_reprovadas > 0:
        print("\n--- Detalhamento das Reprovações ---")
        for p in pecas:
            if p["status"] == "reprovada":
                print(f"  ID {p['id']}: {', '.join(p['motivos'])}")
    else:
        print("\nNenhuma peça foi reprovada.")

    print("\n" + "="*60)


def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("  SISTEMA DE GESTÃO DE PEÇAS E QUALIDADE")
    print("="*50)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("="*50)


def main():
    """Função principal - loop do menu"""
    print("\nBem-vindo ao Sistema de Automação Digital!")
    print("Controle de Produção, Qualidade e Armazenamento de Peças")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("\nEncerrando o sistema... Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Digite um número de 0 a 5.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
