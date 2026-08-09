import os
import pathlib

def create_ai_projects_structure():
    """Create the multi-app AI projects structure with empty files"""
    
    # Define the complete folder structure
    structure = {
        "": [  # Root directory files
            ".env",
            "requirements.txt",
            "README.md",
            "main.py",
            "__init__.py"
        ],
        "apps/debugging_assistant": [
            "app.py",
            "prompts.py",
            "__init__.py"
        ],
        "apps":["__init__.py"],
        "config": [
            "config.yaml",
            "model_config.py",
            "__init__.py"
        ],
        "utils": [
            "llm_client.py",
            "text_helpers.py",
            "mcp_helper.py",
            "debugging_helper.py",
            "itinerary_helper.py",
            "__init__.py"
        ],
        "utils/prompts": [
            "debugging_prompt.json",
            "mcp_generator_prompt.json",
            "itinerary_prompt.json",
            "__init__.py"
        ]
    }
    
    print("Creating AI Python Projects structure...")
    
    # Create all folders and files
    for folder, items in structure.items():
        # Create folder if it doesn't exist
        if folder:
            os.makedirs(folder, exist_ok=True)
            print(f"📁 Created folder: {folder}/")
        
        # Create files within the folder
        for item in items:
            file_path = os.path.join(folder, item) if folder else item
            
            # Handle directories (ending with /)
            if item.endswith('/'):
                os.makedirs(file_path, exist_ok=True)
                print(f"📁 Created folder: {file_path}")
            else:
                # Create empty file
                pathlib.Path(file_path).touch()
                print(f"📄 Created file: {file_path}")
    
    print("\n✅ AI Python Projects structure created successfully!")
    print("📂 All files and folders are now ready in 'ai-python-projects/' directory.")

if __name__ == "__main__":
    create_ai_projects_structure()