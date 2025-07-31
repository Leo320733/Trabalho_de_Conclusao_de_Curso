# 📊 Confiabilidade de Sistemas com Múltiplos Modelos Estatísticos
Este projeto em Python calcula a **confiabilidade de um determinado sistemas compostos por múltiplos componentes**, usando uma **tabela verdade** e diferentes modelos de confiabilidade: **Exponencial**, **Weibull** e **Lognormal**. O sistema é definido por seus **caminhos mínimos** ou de forma **manual**, permitindo análise de estruturas em série, paralelo ou combinadas.

## 🚀 Funcionalidades
- ✅ Entrada interativa dos dados do sistema e dos componentes
- ✅ Suporte a diferentes modelos estatísticos por componente
- ✅ Geração automática da tabela verdade
- ✅ Cálculo da confiabilidade para diferentes instantes de tempo
- ✅ Visualização gráfica da confiabilidade do sistema
- ✅ Impressão de tabela formatada e confiabilidades 

## 🧪 Modelos Suportados
- **Exponencial**: $R(t) = e^{-t/\alpha}$
- **Weibull**: $R(t) = e^{-(t/\alpha)^\beta}$
- **Lognormal**: $R(t) = P(T > t) = 1 - \Phi\left(\frac{\ln(t) - \mu}{\sigma}\right)$

## 📦 Requisitos
- Bibliotecas:
  - `numpy`
  - `scipy`
  - `matplotlib`
  - `pandas`

## 📋 Instale
pip install numpy scipy matplotlib pandas

## ✍️ Uso
1. Execute o programa principal:
python `nome_do_arquivo.py`

2. Forneça:
* O número de componentes
* O tipo de modelo e parâmetros para cada componente
* De forma manual (ex: 0 ou 1) ou com caminhos mínimos do sistema (ex: "ac bce")

## Exemplo
Digite o número de componentes do sistema (n): 4\
Instante tempo (t): 20\
Número de intervalos de tempo: 2

Para componente 1, Escolha uma das opções: 1\
Valor da alfa: 40

Para componente 2, Escolha uma das opções: 2\
Valor da alfa: 60\
Valor da delta: 2

Para componente 3, Escolha uma das opções: 3\
Valor da mi: 2.8\
Valor da sigma: 0.5

Para componente 4, Escolha uma das opções: 1\
Valor da alfa: 80

Digite os caminhos mínimos separados por espaço (ex: 'abc cd ba'): ac bd

* forma manual\
Linha 1 (0, 0, 0, 0) -> Sistema funciona? (0/1): 0\
Linha 2 (0, 0, 0, 1) -> Sistema funciona? (0/1): 0\
Linha 3 (0, 0, 1, 0) -> Sistema funciona? (0/1): 0\
Linha 4 (0, 0, 1, 1) -> Sistema funciona? (0/1): 0\
Linha 5 (0, 1, 0, 0) -> Sistema funciona? (0/1): 0\
Linha 6 (0, 1, 0, 1) -> Sistema funciona? (0/1): 1\
Linha 7 (0, 1, 1, 0) -> Sistema funciona? (0/1): 0\
Linha 8 (0, 1, 1, 1) -> Sistema funciona? (0/1): 1\
......\
Linha 16 (1, 1, 1, 1) -> Sistema funciona? (0/1): 1

* forma automatica\
![image](https://github.com/user-attachments/assets/bfdc4d71-b7f6-4f3a-982a-e876c524da3c)

📈 Saída no Console\
![image](https://github.com/user-attachments/assets/95500c3d-61cc-482b-9343-94e3b0589f62)

📉 Gráfico Gerado\
![image](https://github.com/user-attachments/assets/7a440396-91e7-4c50-8a3d-d61266bbea7b)

## Contato
Se você tiver dúvidas, sugestões ou quiser contribuir com este projeto, sinta-se à vontade para entrar em contato:
* Email: [leoyin2002@gmail.com](mailto:leoyin2002@gmail.com)
* Github: [Leo yin](https://github.com/Leo320733)
* LinkedIn: [Leo yin](www.linkedin.com/in/leo-yin-54ab79249)
