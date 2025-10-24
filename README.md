# 💰 Simulador de Conta Bancária em Python

Este projeto é um **simulador de conta bancária** desenvolvido em **Python**, com o objetivo de praticar conceitos de **funções, listas, dicionários e modularização**.  
O sistema permite realizar operações bancárias básicas, como **depósito, saque, extrato e criação de contas e usuários**.

---

## 📋 Funcionalidades

O programa apresenta um menu interativo com as seguintes opções:

----------------- MENU ----------------------

[1] Depósito
[2] Saque
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[0] Sair


### 🔹 1. Depósito
- Permite inserir um valor positivo para ser adicionado ao saldo.
- Registra a operação no extrato.

### 🔹 2. Saque
- Realiza a retirada de um valor, desde que haja saldo suficiente.
- Registra a operação no extrato.

### 🔹 3. Extrato
- Exibe o histórico de movimentações e o saldo atual.

### 🔹 4. Criar Usuário
- Solicita **nome**, **data de nascimento**, **CPF** e **endereço**.
- Adiciona o novo usuário à lista `usuarios`.

### 🔹 5. Criar Conta
- Associa uma conta a um usuário existente.
- Define **agência**, **número da conta** e **titular**.

### 🔹 6. Listar Contas
- Mostra todas as contas cadastradas, com os dados do titular.

### 🔹 0. Sair
- Encerra o programa.

---

## 🧩 Estrutura das Funções

| Função | Descrição |
|:--------|:------------|
| `menu()` | Exibe o menu principal e retorna a opção escolhida |
| `deposito(valor, saldo, extrato)` | Realiza um depósito e atualiza o extrato |
| `Saque(valor, saldo, extrato)` | Efetua um saque se houver saldo suficiente |
| `Extrato(saldo, extrato)` | Exibe o extrato e o saldo atual |
| `Criar_usuario(usuarios)` | Cria um novo usuário |
| `filtrar_usuario(cpf, usuarios)` | Busca um usuário pelo CPF |
| `criar_conta(agencia, numero_conta, usuarios)` | Cria uma nova conta vinculada a um usuário |
| `listar_contas(contas)` | Lista todas as contas existentes |
| `main()` | Controla o fluxo principal do programa |

---

## 🧠 Conceitos Utilizados

- 💡 **Funções com parâmetros posicionais e nomeados**  
- 📋 **Listas e dicionários** para armazenamento de dados  
- 🔁 **Laço de repetição (`while True`)** para o menu interativo  
- 🧱 **Modularização e separação de responsabilidades**

---

## ⚙️ Exemplo de Execução

```python
----------------- MENU ----------------------

[1] Depósito
[2] Saque
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[0] Sair

Escolha uma opção: 1
Digite o valor do depósito: 200
Depósito realizado com sucesso

Escolha uma opção: 3

-------EXTRATO--------
Depósito:200
Saldo: 200.00
----------------------------------
````


## 🚀 Melhorias Futuras

Limite diário de saques 💸

Validação de CPF 🧾

Login de usuário 🔐

Armazenamento de dados em arquivo ou banco de dados 🗃️

Interface gráfica com Tkinter ou PyQt 🖥️

## 👨‍💻 Autor

Tiago Souza
Desenvolvido para praticar conceitos de Python e lógica de programação.

📅 Ano: 2025
📚 Projeto de estudo e aprendizado contínuo.
