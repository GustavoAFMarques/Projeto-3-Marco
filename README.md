# Projeto: Estruturas Lineares em Python

Atividade prática de Programação de Computadores — 1º Semestre 2026  
Prof. Marco Antonio Sanches — Universidade Cruzeiro do Sul

Este repositório contém três programas em Python que simulam situações do dia a dia usando estruturas de dados lineares: listas, pilhas e filas.

---

## Desafio 1 — Sistema de Votação de Representantes

### O que o programa resolve
Simula uma votação de representantes de classe entre três candidatos: Ana, Bruno e Carlos. O programa registra os votos um a um, valida se o candidato existe e, ao final, exibe o resultado com o vencedor ou indica empate.

### Estruturas utilizadas
- **Lista** para armazenar todos os votos registrados
- **count()** para contar os votos de cada candidato
- **Condicionais** para identificar vencedor ou empate

### Como executar
```bash
python desafio_01_votacao.py
```

### Exemplo de entrada e saída
```
Candidatos:
1. Ana
2. Bruno
3. Carlos

Digite o nome do candidato (fim para encerrar): ana
Voto registrado para Ana.

Digite o nome do candidato (fim para encerrar): bruno
Voto registrado para Bruno.

Digite o nome do candidato (fim para encerrar): ana
Voto registrado para Ana.

Digite o nome do candidato (fim para encerrar): fim

Resultado da votação:
Ana: 2 votos
Bruno: 1 votos
Carlos: 0 votos
O vencedor é: Ana
```

---

## Desafio 2 — Editor de Texto com Desfazer

### O que o programa resolve
Simula um editor de texto simples onde o usuário pode digitar palavras e desfazer a última palavra adicionada. Funciona como a função Ctrl+Z de um editor real.

### Estruturas utilizadas
- **Lista como pilha (Stack)** — estrutura LIFO (Last In, First Out)
- **append()** para adicionar palavra ao topo da pilha
- **pop()** para remover a última palavra adicionada

### Como executar
```bash
python desafio_02_editor_pilha.py
```

### Exemplo de entrada e saída
```
EDITOR DE TEXTO
[1] - Digitar palavra
[2] - Desfazer última palavra
[3] - Mostrar texto
[4] - Sair
Escolha uma opção: 1
Digite uma palavra: minha
Palavra adicionada: minha

Escolha uma opção: 1
Digite uma palavra: terra
Palavra adicionada: terra

Escolha uma opção: 3
Texto atual: minha terra

Escolha uma opção: 2
Palavra removida: terra

Escolha uma opção: 3
Texto atual: minha
```

---

## Desafio 3 — Fila de Atendimento da Secretaria

### O que o programa resolve
Simula o sistema de senhas da secretaria de uma universidade. Os alunos retiram uma senha na ordem de chegada e são chamados nessa mesma ordem: quem chegou primeiro é atendido primeiro.

### Estruturas utilizadas
- **Lista como fila (Queue)** — estrutura FIFO (First In, First Out)
- **append()** para adicionar aluno ao final da fila
- **pop(0)** para chamar o primeiro aluno da fila

### Como executar
```bash
python desafio_03_fila_atendimento.py
```

### Exemplo de entrada e saída
```
SECRETARIA ACADÊMICA
[1] - Retirar senha
[2] - Chamar próximo aluno
[3] - Mostrar fila
[4] - Sair
Escolha uma opção: 1
Nome do aluno: Marco
Marco entrou na fila de atendimento.

Escolha uma opção: 1
Nome do aluno: Ana
Ana entrou na fila de atendimento.

Escolha uma opção: 3
Fila atual:
1º - Marco (Senha 100)
2º - Ana (Senha 101)

Escolha uma opção: 2
Chamando aluno: Marco (Senha 100)

Escolha uma opção: 3
Fila atual:
1º - Ana (Senha 101)
```

---

## Organização do repositório

```
projeto_estruturas_lineares/
├── desafio_01_votacao.py
├── desafio_02_editor_pilha.py
├── desafio_03_fila_atendimento.py
└── README.md
```

## Requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária
