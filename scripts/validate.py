import sys
import os

# Add the scripts directory to the path so we can import lib.parser
sys.path.append(os.path.dirname(__file__))

from lib.parser import parse_all, GlossaryError

def main():
    # We expect to run this from the project root
    glossary_dir = "glossary"
    
    if not os.path.exists(glossary_dir):
        print(f"Error: Directory '{glossary_dir}' not found. Are you running from the project root?")
        sys.exit(1)

    print(f"--- Glossary Validation ---")
    
    files_processed = 0
    errors_found = 0

    # Get all .md files (excluding templates starting with _)
    files = [f for f in os.listdir(glossary_dir) if f.endswith(".md") and not f.startswith("_")]
    
    for filename in files:
        filepath = os.path.join(glossary_dir, filename)
        try:
            from lib.parser import parse_file
            parse_file(filepath)
            print(f"✅ {filename}: OK")
            files_processed += 1
        except GlossaryError as e:
            print(f"❌ {filename}: {str(e)}")
            errors_found += 1
        except Exception as e:
            print(f"❌ {filename}: Unexpected error: {str(e)}")
            errors_found += 1

    print(f"---------------------------")
    if errors_found > 0:
        print(f"Validation FAILED. {errors_found} error(s) found in {len(files)} files.")
        sys.exit(1)
    else:
        print(f"Validation PASSED. {files_processed} files are valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
