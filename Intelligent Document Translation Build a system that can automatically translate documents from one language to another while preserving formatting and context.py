from google.cloud import translate

# Initialize the Translation API client
client = translate.TranslationServiceClient()

# Load the document
with open('path_to_input_file', 'r', encoding='utf-8') as file:
    document_text = file.read()

# Set the source and target languages
source_language = 'en'
target_language = 'fr'

# Translate the document
response = client.translate_text(
    parent=f"projects/{project_id}/locations/{location_id}",
    contents=[document_text],
    mime_type='text/plain',
    source_language_code=source_language,
    target_language_code=target_language,
)

# Extract the translated text
translated_text = response.translations[0].translated_text

# Save the translated document
with open('path_to_output_file', 'w', encoding='utf-8') as file:
    file.write(translated_text)
