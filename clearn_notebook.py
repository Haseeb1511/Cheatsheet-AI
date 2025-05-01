import nbformat
# pip install nbformat nbconvert

# Load the notebook with explicit UTF-8 encoding
notebook_path = 'Rag_with_weviate.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as file:
    notebook = nbformat.read(file, as_version=4)

# Remove the metadata for widgets if it exists
if 'metadata' in notebook:
    notebook['metadata'].pop('widgets', None)

# Save the cleaned notebook with UTF-8 encoding
with open('Rag_with_weviate.ipynb', 'w', encoding='utf-8') as file:
    nbformat.write(notebook, file)
