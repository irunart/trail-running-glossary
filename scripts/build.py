import sys
import os
import json
import csv

# Add the scripts directory to the path so we can import lib.parser
sys.path.append(os.path.dirname(__file__))

from lib.parser import parse_all, GlossaryError

def main():
    glossary_dir = "glossary"
    dist_dir = "dist"
    
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)

    print(f"--- Glossary Build ---")
    
    try:
        data = parse_all(glossary_dir)
        
        # 1. Export JSON
        json_path = os.path.join(dist_dir, "glossary.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ Generated JSON: {json_path}")

        # 2. Export CSV (Flattened)
        csv_path = os.path.join(dist_dir, "glossary.csv")
        
        # Identify all languages dynamically (all sections except title and Meta)
        languages = set()
        for entry in data:
            for section in entry.keys():
                if section not in ["title", "Meta"]:
                    languages.add(section)
        
        languages = sorted(list(languages))
        
        header = ["Title", "Category", "Definition"]
        for lang in languages:
            header.append(f"{lang} Term")
            header.append(f"{lang} Status")
            
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for entry in data:
                row = [
                    entry.get("title", ""),
                    entry.get("Meta", {}).get("Category", ""),
                    entry.get("Meta", {}).get("Definition", "")
                ]
                for lang in languages:
                    lang_data = entry.get(lang, {})
                    row.append(lang_data.get("Term", ""))
                    row.append(lang_data.get("Status", ""))
                writer.writerow(row)
        print(f"✅ Generated CSV: {csv_path}")

    except GlossaryError as e:
        print(f"❌ Build failed during parsing: {str(e)}")
        sys.exit(1)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"❌ Build failed: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
