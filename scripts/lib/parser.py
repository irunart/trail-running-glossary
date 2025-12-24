import os
import re
from .constants import (
    ALLOWED_STATUSES,
    REQUIRED_SECTIONS,
    REQUIRED_META_FIELDS,
    REQUIRED_LANG_FIELDS,
    RESERVED_SECTIONS
)

class GlossaryError(Exception):
    def __init__(self, message, filename=None):
        super().__init__(message)
        self.filename = filename

class FileStructureError(GlossaryError): pass

class SectionMissingError(GlossaryError):
    def __init__(self, section, filename=None):
        super().__init__(f"Missing section: '## {section}'", filename)
        self.section = section

class FieldMissingError(GlossaryError):
    def __init__(self, section, field, filename=None):
        super().__init__(f"Missing field '**{field}:**' in section '## {section}'", filename)
        self.section = section
        self.field = field

class FormatError(GlossaryError): pass

def parse_file(filepath):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        raise GlossaryError(f"Could not read file: {str(e)}", filename)

    if not lines:
        raise FileStructureError("File is empty", filename)

    data = {}
    current_section = None
    
    # 1. Check for H1 Title
    title_match = re.match(r'^#\s+(.+)$', lines[0].strip())
    if not title_match:
        raise FileStructureError("File must start with an H1 title (e.g., '# Performance Index')", filename)
    data['title'] = title_match.group(1).strip()

    # 2. Parse sections and fields
    for i, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if not line:
            continue

        # Section Header (H2)
        h2_match = re.match(r'^##\s+(.+)$', line)
        if h2_match:
            current_section = h2_match.group(1).strip()
            data[current_section] = {}
            continue

        # Field (List item)
        # Supports: - **Key:** Value  OR  - Key: Value
        if current_section:
            field_match = re.match(r'^-\s+\*\*(.+?):\*\*\s*(.*)$', line)
            if not field_match:
                field_match = re.match(r'^-\s+([^:]+):\s*(.*)$', line)
            
            if field_match:
                key = field_match.group(1).replace('*', '').strip()
                val = field_match.group(2).strip()
                data[current_section][key] = val

    # 3. Validation Logic
    for s in REQUIRED_SECTIONS:
        if s not in data:
            raise SectionMissingError(s, filename)

    # Validate Meta fields
    for f in REQUIRED_META_FIELDS:
        if f not in data["Meta"]:
            raise FieldMissingError("Meta", f, filename)

    # Validate Language sections (all H2s except Meta and the title)
    for section in data:
        if section in RESERVED_SECTIONS:
            continue
            
        # Every language section must have the required fields
        for field in REQUIRED_LANG_FIELDS:
             if field not in data[section]:
                raise FieldMissingError(section, field, filename)
        
        status = data[section]["Status"]
        if status not in ALLOWED_STATUSES:
             raise FormatError(f"Invalid Status '{status}' in section '{section}'. Must be one of: {', '.join(sorted(ALLOWED_STATUSES))}", filename)

    return data

def parse_all(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".md") and not filename.startswith("_"):
            filepath = os.path.join(directory, filename)
            results.append(parse_file(filepath))
    return results
