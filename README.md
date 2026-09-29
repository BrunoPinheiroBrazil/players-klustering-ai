# Clusterização de Perfis com K-Means

Este projeto é um exercício prático de Inteligência Artificial (Aprendizado Não Supervisionado) focado em agrupar perfis de jogadores com base em características numéricas. O algoritmo identifica padrões naturais nos dados sem a necessidade de rotulação prévia.

## 🛠️ Tecnologias Utilizadas

O script simula uma base de dados e utiliza três bibliotecas essenciais do ecossistema Python para o fluxo de Machine Learning:

* **Scikit-learn:** Atua como o motor lógico. Ele gera a massa de dados sintéticos e executa o algoritmo matemático `KMeans` para calcular as distâncias e encontrar os agrupamentos corretos.
* **Pandas:** Atua como o estruturador de dados. Ele converte as matrizes numéricas puras em um formato tabular legível (DataFrame), manipulando colunas como "Horas Jogadas" e "Moedas de Ouro".
* **Matplotlib:** Atua como o renderizador visual. Ele pega os resultados processados e plota um gráfico de dispersão espacial, destacando visualmente os membros de cada grupo e seus respectivos centroides geométricos.

## 📁 Estrutura do Projeto

* `main.py`: Código-fonte principal contendo a lógica de geração de dados, clusterização e plotagem gráfica.
* `requirements.txt`: Manifesto de dependências com as bibliotecas necessárias para rodar a aplicação.

## 🚀 Como Executar

Certifique-se de ter o **Python 3** instalado na sua máquina. Abra o terminal na raiz do projeto e execute os comandos abaixo de acordo com o seu sistema operacional:

### Windows (PowerShell/CMD)

1. Crie o ambiente virtual:
```bash
python -m venv venv

2. Ative seu ambiente virtual:
venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o projeto:
python main.py

Mac/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py

Projeto desenvolvido para estudos práticos de Inteligência Artificial.