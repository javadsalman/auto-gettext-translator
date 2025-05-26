# PO File Translator

A Python tool that automatically translates GNU gettext `.po` (Portable Object) files using the Google Translate API. This tool is designed to help developers quickly translate their internationalization files while maintaining the proper gettext format.

## Features

- 🌍 Automatic translation of `.po` files using Google Translate API
- 🔄 Handles fuzzy translations and updates them with fresh translations
- 📁 Batch processing of entire locale directories
- 🧹 Automatically cleans up fuzzy flags and previous msgid comments
- ⚡ Preserves original `.po` file structure and metadata
- 🛡️ Error handling for failed translations

## Prerequisites

- Python 3.6+
- Google Cloud Translation API key
- GNU gettext `.po` files

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd translate
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google Translate API key:
   - Get an API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Cloud Translation API
   - Create a `.env` file in the project root:
```bash
GOOGLE_TRANSLATE_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python translate.py /path/to/your/locale_directory
```

### Directory Structure

Your locale directory should follow the standard gettext structure:
```
locale/
├── en_US/
│   └── LC_MESSAGES/
│       ├── messages.po
│       └── other.po
├── fr_FR/
│   └── LC_MESSAGES/
│       └── messages.po
└── es_ES/
    └── LC_MESSAGES/
        └── messages.po
```

### Example

```bash
# Translate all .po files in the locale directory
python translate.py ./locale

# The tool will process each language directory and translate:
# - Empty msgstr entries
# - Entries marked as fuzzy
# - Entries with previous msgid comments
```

## How It Works

The tool processes `.po` files by:

1. **Scanning** the provided locale directory for language subdirectories
2. **Finding** all `.po` files in `LC_MESSAGES` folders
3. **Identifying** entries that need translation:
   - Empty `msgstr` (untranslated strings)
   - Entries with `fuzzy` flag (uncertain translations)
   - Entries with previous `msgid` comments (changed source strings)
4. **Translating** using Google Translate API
5. **Cleaning up** by removing fuzzy flags and previous msgid comments
6. **Saving** the updated `.po` files

## Configuration

### Environment Variables

- `GOOGLE_TRANSLATE_API_KEY`: Your Google Cloud Translation API key (required)

### Language Codes

The tool automatically converts locale codes (e.g., `en_US`) to Google Translate language codes (e.g., `en-US`) by replacing underscores with hyphens.

## Error Handling

- **Missing API Key**: The script will exit with an error message
- **Invalid Directory**: Validates that the provided path exists
- **Translation Errors**: Individual translation failures are logged but don't stop the process
- **API Errors**: Network and API errors are caught and reported

## Output

The tool provides detailed output showing:
- Which files are being processed
- Each translation performed
- Any errors encountered
- Confirmation when files are saved

Example output:
```
Processing ./locale/fr_FR/LC_MESSAGES/messages.po ...
Translated: 'Hello, world!' -> 'Bonjour le monde!'
Translated: 'Welcome' -> 'Bienvenue'
Saved translations to ./locale/fr_FR/LC_MESSAGES/messages.po
```

## Dependencies

- `requests`: For making HTTP requests to Google Translate API
- `polib`: For parsing and manipulating `.po` files
- `python-dotenv`: For loading environment variables from `.env` file

## Limitations

- Requires a valid Google Cloud Translation API key
- API usage may incur costs based on Google's pricing
- Translation quality depends on Google Translate's capabilities
- Does not handle plural forms specially (translates each form independently)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Documentation

- **[Setup Guide](SETUP.md)** - Detailed step-by-step setup instructions
- **[Examples](EXAMPLES.md)** - Practical examples and use cases
- **[Changelog](CHANGELOG.md)** - Version history and changes
- **[Environment Example](env.example)** - Example configuration file

## Quick Start

1. Copy `env.example` to `.env` and add your Google Translate API key
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python translate.py /path/to/your/locale`

For detailed setup instructions, see the [Setup Guide](SETUP.md).

## Support

If you encounter any issues or have questions, please [open an issue](link-to-issues) on GitHub.
