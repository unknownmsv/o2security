import subprocess
import sys

def install_package():
    """
    Installs the O₂Security library using pip in the current Python environment.
    """
    try:
        print("🚀 Installing O₂Security library...")
        
        # Using sys.executable to ensure using the correct Python interpreter
        # The 'pip install .' command installs the package in the current directory
        command = [sys.executable, "-m", "pip", "install", "."]
        
        # Execute the command
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        print("\n--- Installation Output ---")
        print(result.stdout)
        print("--------------------------")
        
        print("\n✅ O₂Security library installed successfully!")
        print("You can now use it with 'from o2security import tokman'")

    except subprocess.CalledProcessError as e:
        print("\n❌ Installation error:")
        print(e.stderr)
    except FileNotFoundError:
        print("\n❌ Error: 'pip' command not found. Please ensure Python and pip are installed.")

if __name__ == "__main__":
    install_package()