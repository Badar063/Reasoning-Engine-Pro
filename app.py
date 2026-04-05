# ============================================
# REASONING AGENT - Advanced Logic & Reasoning App
# ============================================
# A sophisticated AI agent that demonstrates transparent reasoning
# by showing its thought process before providing answers.
# ============================================

import sys
import time
from typing import Optional

# Install and import required libraries
try:
    import google.generativeai as genai
except ImportError:
    print("Installing required packages...")
    !pip install -q google-generativeai
    import google.generativeai as genai

# ============================================
# CONFIGURATION SECTION
# ============================================

class ReasoningAgent:
    """
    A sophisticated AI agent that performs step-by-step reasoning
    before providing answers to complex problems.
    """
    
    def __init__(self, api_key: str, model_name: str = 'gemini-pro'):
        """
        Initialize the Reasoning Agent with the specified API key and model.
        
        Args:
            api_key: Google AI API key
            model_name: The Gemini model to use (default: 'gemini-pro')
        """
        self.api_key = api_key
        self.model_name = model_name
        self.model = None
        self.chat = None
        self._configure_api()
        self._initialize_model()
        
    def _configure_api(self) -> None:
        """Configure the Google Generative AI API."""
        try:
            genai.configure(api_key=self.api_key)
            print("✓ API configured successfully")
        except Exception as e:
            print(f"✗ Failed to configure API: {e}")
            sys.exit(1)
    
    def _initialize_model(self) -> None:
        """Initialize the Gemini model with system instructions."""
        # Define the system prompt that enforces reasoning format
        system_prompt = """
You are a Reasoning Agent specialized in logical analysis and problem-solving.
You must NEVER answer immediately without showing your reasoning.

For every question, follow this exact format:

### 1. THOUGHT PROCESS
- Break down the problem step-by-step
- Identify key variables, constraints, and assumptions
- Check for logical traps, fallacies, or common misconceptions
- Consider multiple perspectives if applicable
- Draft your solution approach
- Verify your reasoning for consistency

### 2. FINAL ANSWER
- Provide the direct, concise answer based on your analysis
- Highlight the key conclusion clearly
- Include relevant units, numbers, or explanations as needed

Remember: Quality reasoning leads to accurate answers. Always think before responding.
"""
        
        try:
            self.model = genai.GenerativeModel(self.model_name)
            self.chat = self.model.start_chat(history=[
                {'role': 'user', 'parts': [system_prompt]},
                {'role': 'model', 'parts': ["Understood. I am ready to reason step-by-step for any problem you present."]}
            ])
            print("✓ Reasoning Agent initialized successfully")
        except Exception as e:
            print(f"✗ Failed to initialize model: {e}")
            sys.exit(1)
    
    def process_query(self, user_input: str, show_animation: bool = True) -> Optional[str]:
        """
        Process a user query and return the agent's response.
        
        Args:
            user_input: The user's question or problem
            show_animation: Whether to show thinking animation
            
        Returns:
            The agent's response text or None if error
        """
        if not user_input or not user_input.strip():
            return "Please enter a valid question or problem."
        
        # Optional thinking animation
        if show_animation:
            print("🤔 Analyzing", end="", flush=True)
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            print()
        
        try:
            response = self.chat.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Error processing your query: {e}"
    
    def display_welcome(self) -> None:
        """Display welcome message and app information."""
        print("\n" + "="*60)
        print(" " * 15 + "🧠 REASONING AGENT 🧠")
        print("="*60)
        print("\nWelcome to the Advanced Reasoning & Logic Application!")
        print("\nThis AI agent specializes in:")
        print("  • Complex problem-solving")
        print("  • Logical reasoning and analysis")
        print("  • Detecting fallacies and misconceptions")
        print("  • Step-by-step solution breakdowns")
        print("\n" + "-"*60)
        print("\n📝 Instructions:")
        print("  • Enter any logic puzzle, riddle, or complex problem")
        print("  • The agent will show its reasoning process")
        print("  • Type 'exit', 'quit', or 'bye' to end the session")
        print("\n" + "="*60 + "\n")
    
    def display_response(self, response: str) -> None:
        """
        Display the agent's response with proper formatting.
        
        Args:
            response: The agent's response text
        """
        print("\n🤖 AGENT RESPONSE:")
        print("-"*50)
        print(response)
        print("-"*50 + "\n")
    
    def run_interactive_session(self) -> None:
        """Run the main interactive session."""
        self.display_welcome()
        
        # Example problems to get users started
        print("💡 EXAMPLE PROBLEMS TO TRY:")
        examples = [
            "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?",
            "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?",
            "A farmer has 15 chickens. All but 8 die. How many are left?"
        ]
        
        for i, example in enumerate(examples, 1):
            print(f"  {i}. {example[:80]}...")
        
        print("\n" + "="*60)
        
        # Main interaction loop
        while True:
            try:
                # Get user input
                user_input = input("👤 You: ").strip()
                
                # Check for exit command
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("\n✨ Thank you for using the Reasoning Agent. Goodbye! ✨")
                    break
                
                # Skip empty input
                if not user_input:
                    continue
                
                # Process the query
                response = self.process_query(user_input)
                
                # Display the response
                if response:
                    self.display_response(response)
                
            except KeyboardInterrupt:
                print("\n\n⚠️ Session interrupted. Goodbye! ⚠️")
                break
            except Exception as e:
                print(f"\n⚠️ An unexpected error occurred: {e}")
                print("Please try again or restart the session.\n")


# ============================================
# MAIN EXECUTION
# ============================================

def main():
    """
    Main function to run the Reasoning Agent application.
    """
    print("="*60)
    print(" " * 20 + "REASONING AGENT SETUP")
    print("="*60)
    
    # Get API key with clear instructions
    print("\n🔑 GOOGLE AI API KEY REQUIRED")
    print("To use this application, you need a Google AI API key.")
    print("Get your API key from: https://makersuite.google.com/app/apikey")
    print("\n⚠️  IMPORTANT: Never share your API key publicly!\n")
    
    # Try to get API key from Colab secrets or user input
    api_key = None
    
    # Check if running in Colab with secrets
    try:
        from google.colab import userdata
        api_key = userdata.get('GOOGLE_API_KEY')
        if api_key:
            print("✓ API key loaded from Colab secrets")
    except (ImportError, Exception):
        pass
    
    # If no key found, prompt user
    if not api_key:
        api_key = input("Enter your Google API key: ").strip()
        
        if not api_key:
            print("\n❌ No API key provided. Exiting...")
            print("Please get an API key from: https://makersuite.google.com/app/apikey")
            sys.exit(1)
        
        print("\n✓ API key received")
    
    # Create and run the reasoning agent
    try:
        # Initialize the agent
        agent = ReasoningAgent(api_key=api_key)
        
        # Run the interactive session
        agent.run_interactive_session()
        
    except Exception as e:
        print(f"\n❌ Failed to initialize the Reasoning Agent: {e}")
        print("\nTroubleshooting tips:")
        print("  1. Verify your API key is correct")
        print("  2. Check your internet connection")
        print("  3. Ensure you have access to Gemini Pro")
        sys.exit(1)


# Run the application
if __name__ == "__main__":
    main()
