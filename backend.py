import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=3000,
                temperature=0.5
            ).choices[0].text
            return response
        except openai.error.RateLimitError:
            return "There is no longer free versions of GPTs from openai api."

# Test area ->
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)