import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import nltk
from transformers import BertTokenizer, BertForQuestionAnswering
from nltk.tokenize import sent_tokenize
import torch

# Télécharger les ressources nécessaires pour NLTK
nltk.download('punkt')

# Fonction pour extraire la réponse à partir du modèle "question_answering"
def get_answer(question, context):
    tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    model = BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')

    inputs = tokenizer(question, context, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**inputs)

    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    return answer, answer_start, answer_end

# Demander à l'utilisateur d'entrer l'article
print("Veuillez entrer l'article :")
article = input()

# Tokenization en phrases
article_sentences = sent_tokenize(article)

# Chatbot interactif
print("Le chatbot est prêt à répondre à vos questions ! Entrez 'exit' pour quitter.")
while True:
    user_input = input("Posez une question : ")
    if user_input.lower() == 'exit':
        break

    # Rechercher la réponse dans l'article
    answer, answer_start, answer_end = get_answer(user_input, article)
    if answer_start == 0 and answer_end == 0:
        print("La réponse ne figure pas dans l'article.")
    else:
        print("Réponse :", answer)
