from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.add_labels()
        return self.root

    def add_labels(self):
        names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]  # List of names
        for name in names:
            label = Label(text=name, font_size=24)  # Create a label for each name
            self.root.ids.main.add_widget(label)  # Add the label to the main BoxLayout

DynamicLabelsApp().run()
