from nlp.predict import predict_sentiment
from fuzzy.fuzzy_system import evaluate_satisfaction

print("\n=== SISTEMA INTELIGENTE DE ATENDIMENTO ===\n")

while True:

    text = input("Digite a mensagem (ou 'sair'): ")

    if text.lower() == "sair":
        break

    wait_time = int(input("Tempo de espera: "))

    sentiment, confidence = predict_sentiment(text)

    score = evaluate_satisfaction(confidence, wait_time)

    print("\n--- RESULTADO ---")
    print("Sentimento:", sentiment)
    print("Confiança:", round(confidence, 2))
    print("Satisfação:", round(score, 2))
    print("-----------------\n")