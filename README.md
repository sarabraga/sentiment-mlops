# Sentiment Analysis RoBERTa (TweetEval)

Questo modello è stato fine-tunato a partire da `cardiffnlp/twitter-roberta-base-sentiment-latest`
per la classificazione automatica del sentiment dei tweet in **positivo**, **neutro** e **negativo**.

## Dataset
- Nome: TweetEval Sentiment
- Numero di esempi: 45.615 (train), 2.000 (validation), 12.284 (test)

## Architettura
- Base model: RoBERTa (CardiffNLP)
- Tokenizzazione: max_length=128
- Framework: Hugging Face Transformers

## Metriche di performance
| Modello | Accuracy | F1-Score |
|----------|-----------|----------|
| FastText (Baseline) | 0.5613 | 0.5444 |
| **RoBERTa (Fine-tuned)** | **0.7316** | **0.7310** |

## MLOps Pipeline
- Preprocessing e tokenizzazione automatica
- Training e early stopping su validation
- Valutazione automatica su test set
- Deploy continuo su Hugging Face Hub

## Informazioni autore
Autore: SARABRAGA27  
Organizzazione: MachineInnovators Inc.  
Anno: 2025
