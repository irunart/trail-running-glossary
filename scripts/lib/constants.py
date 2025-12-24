# Validation Constraints
ALLOWED_STATUSES = {"Draft", "Reviewed"}

# File Structure
REQUIRED_SECTIONS = ["Meta", "English (EN)"]
REQUIRED_META_FIELDS = ["Definition", "Category"]
REQUIRED_LANG_FIELDS = ["Term", "Status"]

# Reserved Sections that are not language definitions
RESERVED_SECTIONS = {"title", "Meta"}
