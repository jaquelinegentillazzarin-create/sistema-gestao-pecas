# Sistema de Gestão de Peças, Qualidade e Armazenamento

Protótipo de automação digital desenvolvido em Python para controle de produção e qualidade de peças em uma linha de montagem industrial.

## Descrição do Problema

O processo de inspeção de peças era feito manualmente, gerando atrasos, falhas de conferência e aumento de custo. Este sistema automatiza:

- Cadastro de peças (ID, peso, cor e comprimento)
- Avaliação automática de qualidade
- Armazenamento em caixas com capacidade limitada (10 peças)
- Geração de relatórios consolidados

## Critérios de Qualidade

Uma peça é **aprovada** somente se atender **todos** os critérios abaixo:

| Critério       | Regra                        |
|----------------|------------------------------|
| Peso           | Entre 95g e 105g             |
| Cor            | Azul ou Verde                |
| Comprimento    | Entre 10cm e 20cm            |

Se qualquer critério não for atendido, a peça é **reprovada** e o(s) motivo(s) são registrados.

## Funcionalidades do Menu

1. **Cadastrar nova peça**  
   Solicita ID, peso, cor e comprimento. Valida os dados e adiciona a peça ao sistema. Se aprovada, coloca na caixa atual. Quando a caixa atinge 10 peças, ela é fechada automaticamente e uma nova é iniciada.

2. **Listar peças aprovadas/reprovadas**  
   Mostra todas as peças cadastradas separadas por status, incluindo os motivos de reprovação.

3. **Remover peça cadastrada**  
   Remove uma peça pelo ID. Também remove a peça de qualquer caixa (atual ou fechada) em que ela esteja.

4. **Listar caixas fechadas**  
   Exibe todas as caixas já fechadas (com as peças de cada uma) e também o estado da caixa atual (aberta).

5. **Gerar relatório final**  
   Mostra totais de peças aprovadas, reprovadas (com motivos), quantidade de caixas utilizadas e detalhes.

0. **Sair**  
   Encerra o programa.

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado

### Passo a passo

1. Baixe ou clone este repositório
2. Abra o terminal (ou prompt de comando) na pasta do projeto
3. Execute o comando:

```bash
python sistema_gestao_pecas.py
```

ou

```bash
python3 sistema_gestao_pecas.py
```

4. O menu interativo será exibido. Digite o número da opção desejada e pressione Enter.

## Exemplos de Uso

### Exemplo 1 – Cadastrar peça aprovada

```
Escolha uma opção: 1

==================================================
 CADASTRAR NOVA PEÇA
==================================================
Digite o ID da peça: P001
Digite o peso (em gramas): 100
Digite a cor (azul ou verde): azul
Digite o comprimento (em cm): 15

[OK] Peça 'P001' APROVADA e adicionada à caixa atual.
     Peças na caixa atual: 1/10
```

### Exemplo 2 – Cadastrar peça reprovada

```
Escolha uma opção: 1

==================================================
 CADASTRAR NOVA PEÇA
==================================================
Digite o ID da peça: P002
Digite o peso (em gramas): 80
Digite a cor (azul ou verde): vermelho
Digite o comprimento (em cm): 25

[X] Peça 'P002' REPROVADA.
    Motivos:
    - Peso fora do intervalo permitido (95g - 105g)
    - Cor inválida (deve ser azul ou verde)
    - Comprimento fora do intervalo permitido (10cm - 20cm)
```

### Exemplo 3 – Relatório final (após 10 peças aprovadas, fechando exatamente 1 caixa)

```
============================================================
 RELATÓRIO FINAL CONSOLIDADO
============================================================

Total de peças cadastradas : 12
Total de peças APROVADAS   : 10
Total de peças REPROVADAS  : 2
Quantidade de caixas usadas: 1
  - Caixas fechadas        : 1
  - Caixa atual (aberta)   : Não (vazia)

--- Detalhamento das Reprovações ---
  ID P002: Peso fora do intervalo permitido (95g - 105g), Cor inválida (deve ser azul ou verde), Comprimento fora do intervalo permitido (10cm - 20cm)
  ID P005: Cor inválida (deve ser azul ou verde)
```

## Estrutura do Código

- **Listas principais**: `pecas`, `caixas_fechadas`, `caixa_atual`
- **Funções**:
  - `validar_peca()` → aplica as regras de qualidade
  - `cadastrar_peca()` → cadastra e decide aprovação/reprovação
  - `listar_pecas()` → mostra aprovadas e reprovadas
  - `remover_peca()` → remove peça e atualiza caixas
  - `listar_caixas_fechadas()` → mostra caixas fechadas + atual
  - `gerar_relatorio()` → relatório consolidado
  - `main()` → loop do menu interativo

## Observações

- O sistema armazena tudo em memória (as listas são perdidas ao fechar o programa).
- IDs devem ser únicos.
- A cor é tratada sem diferenciação de maiúsculas/minúsculas.
- Aceita vírgula ou ponto como separador decimal no peso e comprimento.

## Autor

Trabalho desenvolvido para a disciplina de Algoritmos e Lógica de Programação.
