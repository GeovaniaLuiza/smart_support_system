<<<<<<< HEAD
# Smart Support System | Sistema Inteligente de Atendimento ao Cliente
=======
# Smart Support System
>>>>>>> 87ef6ab054ebf7803b2cf6dc0477ffce05612274

Sistema inteligente híbrido para análise de sentimentos, tratamento de incerteza e otimização de alocação de recursos em atendimento ao cliente.

---

# Objetivo

Desenvolver um sistema inteligente capaz de processar informações não estruturadas (texto), tratar incertezas por meio de lógica fuzzy e otimizar decisões de alocação de recursos utilizando algoritmos de Inteligência Artificial.

---

# Arquitetura do Sistema

O sistema é dividido em três camadas principais:

---

## Camada I — Processamento de Linguagem Natural (PLN)

- Algoritmo: Naive Bayes / Logistic Regression  
- Técnica: TF-IDF + pré-processamento textual  
- Função: Classificação de sentimentos  

### Classes:
- Positivo  
- Neutro  
- Negativo  

### Dataset:
https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment
---

## Camada II — Sistema Fuzzy (Incerteza)

- Tipo: Sistema de Inferência Fuzzy (Mamdani)
- Entradas:
  - Probabilidade do sentimento (PLN)
  - Tempo de espera do cliente

- Saída:
  - Nível de satisfação (0 a 100)

### Regras:
- Se sentimento é positivo e espera é baixa → satisfação alta  
- Se sentimento é negativo e espera é alta → insatisfação  

---

## Camada III — Otimização Estocástica

- Algoritmo: Simulated Annealing  
- Problema: Alocação de atendentes  
- Objetivo: Maximizar eficiência e satisfação  

---

# Modelagem com Grafos

- Tipo: Grafo bipartido  
- Nós:
  - Tickets de clientes  
  - Atendentes  
- Arestas: possíveis atendimentos  

---

# Tecnologias Utilizadas

- Python  
- Pandas  
- Scikit-learn  
- NLTK  
- Fuzzy Logic  
- Streamlit (opcional)

---

# Estrutura do Projeto
<<<<<<< HEAD

=======
>>>>>>> 87ef6ab054ebf7803b2cf6dc0477ffce05612274

```bash
smart_support_system/
│
├── app.py
├── streamlit_app.py
│
├── data/
│ └── Tweets.csv
│
├── nlp/
│ ├── preprocess.py
│ ├── train_model.py
│ ├── predict.py
│ └── sentiment_model.pkl
│
├── fuzzy/
│ └── fuzzy_system.py
│
├── optimization/
│ └── simulated_annealing.py
│
├── graph/
│ └── graph_model.py
│
└── README.md
```

---

# Como Executar

## 1. Instalar dependências
```bash
pip install -r requirements.txt

2. Treinar modelo
python -m nlp.train_model

3. Executar sistema (terminal)
python app.py

4. (Opcional) Interface web
python -m streamlit run streamlit_app.py
<<<<<<< HEAD
```

## 2. Arquitetura do sistema
```bash
Usuário
   ↓
PLN (Naive Bayes)
   ↓
Probabilidade de sentimento
   ↓
Sistema Fuzzy
   ↓
Nível de satisfação
   ↓
Simulated Annealing
   ↓
Otimização da decisão
```
=======

Resultados
Classificação automática de sentimentos
Avaliação de satisfação do cliente
Otimização de alocação de recursos
Redução de tempo de espera

Conclusão

O sistema integra diferentes áreas da Inteligência Artificial:

PLN para interpretação de texto
Fuzzy para incerteza
Metaheurísticas para otimização
Grafos para modelagem estrutural
👨‍💻 Projeto Acadêmico

Disciplina: Inteligência Artificial (N2)
Sistema desenvolvido para fins educacionais
>>>>>>> 87ef6ab054ebf7803b2cf6dc0477ffce05612274
