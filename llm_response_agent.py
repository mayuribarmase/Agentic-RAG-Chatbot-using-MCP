import google.generativeai as genai


GEMINI_API_KEY = <"Replace with your real key">   

class LLMResponseAgent:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-pro')

    def generate_answer(self, question, context_chunks):
        context = "\n\n".join(context_chunks)
        prompt = (
            f"Use the following context to answer the question strictly based on it. "
            f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
        )
        response = self.model.generate_content(prompt)
        return response.text

