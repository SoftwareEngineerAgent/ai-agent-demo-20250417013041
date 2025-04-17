```python
# ai_agent.py
import openai
import os


class AIAgent:
    """
    A class responsible for interacting with the OpenAI API to generate code based on prompts.
    """

    def __init__(self, api_key):
        """
        Initializes the AIAgent with the OpenAI API key.
        Args:
            api_key (str): The OpenAI API key.
        """
        openai.api_key = api_key
        self.model_name = "gpt-3.5-turbo"  # You can change to another model if you like

    def generate_code(self, prompt):
        """
        Generates code based on the given prompt using the OpenAI API.

        Args:
            prompt (str): The prompt to generate code from.

        Returns:
            str: The generated code, or None if an error occurred.
        """
        try:
            completion = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates Python code based on user requests."},
                    {"role": "user", "content": prompt}
                ]
            )
            
            return completion.choices[0].message["content"]
        except Exception as e:
            print(f"Error generating code: {e}")
            return None

    def generate_code_with_functions(self, prompt, functions, function_call="auto"):
        """
        Generates code based on the given prompt using the OpenAI API with function calling support.

        Args:
            prompt (str): The prompt to generate code from.
            functions (list): A list of function definitions to use.
            function_call (str): Specifies the function call behavior. "auto" or {"name": "<function_name>"}

        Returns:
            str: The generated code, or None if an error occurred.
        """
        try:
            completion = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates Python code based on user requests and can use functions when appropriate."},
                    {"role": "user", "content": prompt}
                ],
                functions=functions,
                function_call=function_call,
            )
            
            return completion.choices[0]
        except Exception as e:
            print(f"Error generating code: {e}")
            return None
    


if __name__ == '__main__':
    # Example usage:
    # Replace with your actual API key or environment variable
    api_key = os.getenv("OPENAI_API_KEY")  
    if not api_key:
        print("Error: OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")
    else:
        agent = AIAgent(api_key)
        prompt = "Write a Python function that calculates the factorial of a number."
        code = agent.generate_code(prompt)

        if code:
            print("Generated code:")
            print(code)
        else:
            print("Failed to generate code.")
```