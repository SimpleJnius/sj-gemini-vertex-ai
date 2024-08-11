# Gemini (Firebase-Vertex-AI)

Access Gemini Android SDK in Python 

## Usage
**Note: NO NEED FOR THREAD OR ASYNC.**

### For autocompletion in IDE
```shell
pip install sjgeminifvai
```

### Set up your firebase project for Android
Read more [here](https://firebase.google.com/docs/vertex-ai/get-started?hl=en&authuser=0&platform=android#set-up-firebase)

### Add SDK to buildozer.spec file
```rpmspec
requirements=sjgeminifvai,simplejnius

android.gradle_dependencies=com.google.guava:guava:32.0.1-android,
  org.reactivestreams:reactive-streams:1.0.4,com.google.firebase:firebase-vertexai:16.0.0-beta04
```

### Interact with Vertex Gemini API Without Streaming
Wait for the entire result instead of streaming; 
the result is only returned after the model completes the entire generation process.

```python
from sjgeminifvai.jclass import (
    FirebaseVertexAI,
    ContentBuilder,
    GenerativeModelFutures
)
from simplejnius.guava.jclass import Futures
from simplejnius.guava.jinterface import FutureCallback
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class GeminiApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.future_callback = None
        self.response = None
        self.prompt = None
        self.textinput = None
        self.label = None

        # Initialize the Vertex AI service and the generative model
        # Specify a model that supports your use case
        # Gemini 1.5 models are versatile and can be used with all API capabilities
        vertex = FirebaseVertexAI.getInstance()
        self.gm = vertex.generativeModel("gemini-1.5-flash")

        # Use the GenerativeModelFutures Java compatibility layer which offers
        # support for ListenableFuture and Publisher APIs
        self.model = GenerativeModelFutures.from_(self.gm)

    def build(self):
        self.label = Label()
        self.textinput = TextInput(
            size_hint_y=.1,
            hint_text="Chat with gemini",
            on_text_validate=self.chat_gemini
        )
        box = BoxLayout(orientation="vertical")
        box.add_widget(self.label)
        box.add_widget(self.textinput)
        return box

    def chat_gemini(self, instance):
        # Provide a prompt that contains text
        self.prompt = (
            ContentBuilder()
            .addText(instance.text)
            .build()
        )

        # To generate text output, call generateContent with the text input
        self.response = self.model.generateContentResponse(self.prompt)

        self.future_callback = FutureCallback(
            callback=dict(
                on_success=self.get_gemin_reply,
                on_failure=print
            )
        )
        Futures.addCallback(self.response, self.future_callback)

    def get_gemini_reply(self, result):
        self.label.text = result.getText()


if __name__ == "__main__":
    GeminiApp().run()

# report any bug or error if the above code does not work as expected
```

### Interact with Vertex Gemini API With Streaming
You can achieve faster interactions by not waiting for the entire result from the model generation, 
and instead use streaming to handle partial results.

This example shows how to use generateContentStream to stream 
generated text from a prompt request that includes only text:

```python
from sjgeminifvai.jclass import (
    FirebaseVertexAI,
    ContentBuilder,
    GenerativeModelFutures
)
from simplejnius.reactivestreams.jinterface import Subscriber
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock


class GeminiApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subscriber = None
        self.gcr = None
        self.streaming_response = None
        self.prompt = None
        self.textinput = None
        self.label = None

        # Initialize the Vertex AI service and the generative model
        # Specify a model that supports your use case
        # Gemini 1.5 models are versatile and can be used with all API capabilities
        vertex = FirebaseVertexAI.getInstance()
        self.gm = vertex.generativeModel("gemini-1.5-flash")

        # Use the GenerativeModelFutures Java compatibility layer which offers
        # support for ListenableFuture and Publisher APIs
        self.model = GenerativeModelFutures.from_(self.gm)

    def build(self):
        self.label = Label()
        self.textinput = TextInput(
            size_hint_y=.1,
            hint_text="Chat with gemini",
            on_text_validate=self.chat_gemini
        )
        box = BoxLayout(orientation="vertical")
        box.add_widget(self.label)
        box.add_widget(self.textinput)
        return box

    def chat_gemini(self, instance):
        # Provide a prompt that contains text
        self.prompt = (
            ContentBuilder()
            .addText(instance.text)
            .build()
        )

        # To stream generated text output, call generateContentStream with the text input
        self.streaming_response = self.model.generateContentStream(self.prompt)

        self.subscriber = Subscriber(
            callback=dict(
                on_next=self.get_gemini_reply,
                on_complete=lambda result: setattr(self.label, "text", result.getText()),
                on_error=print,
                on_subscribe=print
            )
        )
        self.streaming_response.subscribe(self.subscriber)

    def get_gemini_reply(self, result):
        chunk = result.getText()

        def add_chunk_to_label(_):
            self.label.text += chunk

        Clock.schedule_once(add_chunk_to_label)


if __name__ == "__main__":
    GeminiApp().run()

# report any bug or error if the above code does not work as expected
```

# Examples to interact with images and videos coming soon 