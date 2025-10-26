import gradio as gr
from transformers import pipeline

MODEL_ID = "SARABRAGA27/sentiment-analysis-roberta"
pipe = pipeline("text-classification", model=MODEL_ID)

def predict_sentiment(text):
    if not text.strip():
        return "Inserisci un testo per l'analisi."
    result = pipe(text)[0]
    label_map = {
        "LABEL_0": "Negativo",
        "LABEL_1": "Neutro",
        "LABEL_2": "Positivo"
    }
    label = label_map.get(result["label"], result["label"])
    return f"{label} (score: {result['score']:.2f})"

demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(label="Scrivi un tweet o un commento"),
    outputs=gr.Textbox(label="Sentiment rilevato"),
    title="Analisi del Sentiment con RoBERTa",
    description="Demo interattiva basata su SARABRAGA27/sentiment-analysis-roberta"
)

if __name__ == "__main__":
    demo.launch()
