# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of PO File Translator
- Automatic translation of GNU gettext `.po` files using Google Translate API
- Support for batch processing of locale directories
- Fuzzy translation handling and cleanup
- Previous msgid comment processing
- Environment variable configuration via `.env` files
- Comprehensive error handling and logging
- Support for standard gettext directory structure

### Features
- Translates empty `msgstr` entries
- Updates fuzzy translations with fresh translations
- Processes entries with previous msgid comments
- Automatically removes fuzzy flags after translation
- Cleans up previous msgid comments after processing
- Preserves original `.po` file structure and metadata
- Provides detailed console output for translation progress

### Dependencies
- `requests` for HTTP API calls
- `polib` for `.po` file parsing and manipulation
- `python-dotenv` for environment variable management

## [1.0.0] - Initial Release

### Added
- Core translation functionality
- Google Translate API integration
- Batch processing capabilities
- Error handling and validation
- Documentation and setup guides 