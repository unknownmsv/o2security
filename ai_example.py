# test_ai_client.py
import sys
from o2security.ai import O2AI

def main():
    """
    Main function to run the command-line AI chat client.
    """
    # --- IMPORTANT ---
    # Replace this with the exact name of the AI project you created in the web UI.
    PROJECT_NAME = "ai"
    
    print("=============================================")
    print(f"  O₂Security AI Chat Client (Project: {PROJECT_NAME})")
    print("=============================================")
    print("Type your message and press Enter to chat.")
    print("Type 'exit' to quit the program.")
    print("Type 'clear' to wipe the conversation memory.")
    print("---------------------------------------------")

    try:
        # 1. Initialize the AI client for your project
        ai_client = O2AI(project_name='ai')
        
        # Optional: You can override the system prompt at runtime
        # ai_client.set_system_prompt("You are a friendly Python expert.")
        
    except FileNotFoundError as e:
        print(f"\n[ERROR] Could not find the project configuration.")
        print(f"Details: {e}")
        print(f"Please make sure you have created the AI project '{PROJECT_NAME}' in the web dashboard.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred during initialization: {e}")
        sys.exit(1)

    # 2. Start the interactive chat loop
    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("AI: Goodbye!")
            break
        
        if user_input.lower() == 'clear':
            ai_client.clear_memory()
            print("AI: Conversation history has been cleared.")
            continue

        if not user_input:
            continue

        # 3. Send the message to the AI and get the response
        try:
            print("AI: Thinking...")
            response = ai_client.chat(user_input)
            # Use ANSI escape codes to move cursor up and clear the line
            # This replaces "Thinking..." with the actual response for a cleaner look.
            sys.stdout.write("\033[F") # Move cursor up one line
            sys.stdout.write("\033[K") # Clear line
            print(f"AI: {response}")
        except Exception as e:
            print(f"\n[ERROR] An error occurred while communicating with the AI: {e}")


if __name__ == "__main__":
    main()
