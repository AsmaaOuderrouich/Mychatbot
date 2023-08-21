from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import chatbot  # Importez votre code Python de chatbot ici

class ChatbotApp(App):
    def build(self):
        self.title = 'Chatbot App'
        return ChatbotLayout()

class ChatbotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatbotLayout, self).__init__(**kwargs)
        
        self.orientation = 'vertical'

        self.article_input = TextInput(hint_text='Entrez l\'article', multiline=True)
        self.add_widget(self.article_input)

        self.question_input = TextInput(hint_text='Posez une question')
        self.add_widget(self.question_input)

        self.answer_label = Label(text='', size_hint=(1, 0.3))
        self.add_widget(self.answer_label)

        self.submit_button = Button(text='Obtenir Réponse', size_hint=(1, 0.2))
        self.submit_button.bind(on_release=self.get_answer)
        self.add_widget(self.submit_button)

    def get_answer(self, instance):
        article = self.article_input.text
        question = self.question_input.text

        # Utilisez votre code chatbot pour obtenir la réponse
        answer = chatbot.get_answer(question, article)

        self.answer_label.text = f'Réponse : {answer}'

if __name__ == '__main__':
    ChatbotApp().run()
