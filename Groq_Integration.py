import os

class ChatGroq:
    """Mocking Groq Class"""

    def __init__(self, model, temperature=0, max_retries=2):
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.valid_models = [
            "llama-4-8b-instant",
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant"
        ]

        if model not in self.valid_models:
            raise ValueError(f"Invalid model: {model}")
        
    def invoke(self, messages):
        """Mock invoke method that returns a simulated response."""
        if not isinstance(messages, list) or len(messages) == 0:
            raise ValueError("Message must be a non-empty list")
        
        if self.model == "llama-4-8b-instant":
            content = f"[Llama 4 Response] Machine learning is a subset of AI that enables computers to learn patterns from data without explicit programming."
        elif self.model == "llama-3.3-70b-versatile":
            if self.temperature > 0.2:
                content = content = f"[Llama 3.3 Creative Response] Machine learning is like teaching a computer to recognize patterns in data, much like how humans learn from experience!"
            else:
                content = f"[Llama 3.3 Response] Machine learning allows computers to learn and improve from data without being explicitly programmed."
        else:
            content = f"[Mock Response] This is a simulated response from {self.model}"

        return MockAIMessage(content)
    
class MockAIMessage:
    """Mock AI Mesage response"""
    def __init__(self, content):
        self.content = content

class implement_set_api_key():
    """
    IMPLEMENT: Set the GROQ API KEY environment variable.

    Args: api_key (str): Your Groq API Key
    """
    def __init__(self, api_key: str):
        os.environ["GROQ_API_KEY"] = api_key

def check_api_key():
    """
    Check if GROQ API KEY is set in the environment variables.
    Raise an exception if the API key is not set.
    """
    if "GROQ_API_KEY" not in os.environ:
        raise Exception("GROQ_API_KEY environment variable is required")

def implement_llama_4_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 4.
    Use the exact model name from console.groq.com
    Set temperature=0 for consistent responses
    """
    return ChatGroq(temperature=0, model="llama-4-8b-instant", max_retries=2)


def implement_llama_3_3_model():
    """
    IMPLEMENT: Create and return a ChatGroq instance for Llama 3.3.
    Use the exact model name from console.groq.com
    Set for slightly more creative responses
    """
    return ChatGroq(temperature=0.3, model="llama-3.3-70b-versatile", max_retries=2)

def implement_query_model(model, prompt):
    """
    IMPLEMENT: Send a query to the model and return the response content.
    
    Args:
        model: The ChatGroq model instance
        prompt: The text prompt to send
        
    Returns:
        str: The response content
    """
    try:
        messages = [("human", prompt)]
        response = model.invoke(messages)
        return response.content
    except Exception as e:
        raise Exception(f"Error: {str(e)}")


def implement_compare_models(prompt):
    """
    IMPLEMENT: Query both models and return a dictionary with both responses.
    
    Args:
        prompt: The text prompt to send to both models
        
    Returns:
        dict: Dictionary with responses from both models
    """
    dict1 = {"response1": implement_query_model(implement_llama_3_3_model(),prompt), "response2": implement_query_model(implement_llama_4_model(),prompt)}
    return dict1

def main():
    """
    Main function to test your implementations.
    """
    print("🚀 Groq Model Switching Exercise (LangChain Integration)")
    print("=" * 55)
    print("📝 This exercise simulates langchain-groq package behavior!")
    print("🌐 Model names should match console.groq.com exactly")
    print()
    
    try:
        # Test your set_api_key implementation
        print("🔑 Setting API key...")
        implement_set_api_key("mock_api_key_for_testing")
        
        # Check if API key was set correctly
        check_api_key()
        print("✓ API key validation working!")
        
        # Test prompt
        test_prompt = "Explain the concept of machine learning in one sentence."
        
        # Test your model implementations
        print(f"\n🤖 Testing your Llama 4 implementation:")
        llama4 = implement_llama_4_model()
        response4 = implement_query_model(llama4, test_prompt)
        print(f"Llama 4: {response4}\n")
        
        print(f"🤖 Testing your Llama 3.3 implementation:")
        llama33 = implement_llama_3_3_model()
        response33 = implement_query_model(llama33, test_prompt)
        print(f"Llama 3.3: {response33}\n")
        
        # Test your comparison implementation
        print("🔄 Testing your model comparison:")
        comparison = implement_compare_models(test_prompt)
        print("Comparison results:")
        for model, response in comparison.items():
            print(f"  {model}: {response}")
        
        print("\n🎉 All implementations working!")
        print("✅ Great job implementing the LangChain-Groq patterns!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        if "GROQ_API_KEY" in str(e):
            print("\n💡 Check your implement_set_api_key() function!")
        else:
            print("📝 Check your function implementations!")
            print("🌐 Verify model names match console.groq.com exactly")


if __name__ == "__main__":
    main()

