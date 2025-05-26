# Setup Guide

This guide will walk you through setting up the PO File Translator tool step by step.

## Step 1: Google Cloud Setup

### 1.1 Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click "Select a project" at the top of the page
4. Click "New Project"
5. Enter a project name (e.g., "po-translator")
6. Click "Create"

### 1.2 Enable the Translation API

1. In the Google Cloud Console, make sure your new project is selected
2. Go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard)
3. Click "Enable APIs and Services"
4. Search for "Cloud Translation API"
5. Click on "Cloud Translation API"
6. Click "Enable"

### 1.3 Create API Credentials

1. Go to [APIs & Services > Credentials](https://console.cloud.google.com/apis/credentials)
2. Click "Create Credentials" > "API Key"
3. Copy the generated API key
4. (Optional but recommended) Click "Restrict Key" to limit its usage:
   - Under "API restrictions", select "Restrict key"
   - Choose "Cloud Translation API"
   - Click "Save"

## Step 2: Project Setup

### 2.1 Clone and Install

```bash
# Clone the repository
git clone <your-repository-url>
cd translate

# Create a virtual environment (recommended)
python -m venv projectenv

# Activate the virtual environment
# On Windows:
projectenv\Scripts\activate
# On macOS/Linux:
source projectenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2.2 Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Create the .env file
touch .env  # On Windows: type nul > .env
```

Add your API key to the `.env` file:
```
GOOGLE_TRANSLATE_API_KEY=your_actual_api_key_here
```

**Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## Step 3: Prepare Your PO Files

### 3.1 Directory Structure

Organize your locale files in the standard gettext structure:

```
your_project/
└── locale/
    ├── en_US/
    │   └── LC_MESSAGES/
    │       └── messages.po
    ├── fr_FR/
    │   └── LC_MESSAGES/
    │       └── messages.po
    ├── es_ES/
    │   └── LC_MESSAGES/
    │       └── messages.po
    └── de_DE/
        └── LC_MESSAGES/
            └── messages.po
```

### 3.2 PO File Format

Your `.po` files should contain entries like:

```po
# Comment
#: source_file.py:123
msgid "Hello, world!"
msgstr ""

#: source_file.py:456
#, fuzzy
msgid "Welcome to our application"
msgstr "Bienvenue dans notre application"

#: source_file.py:789
#| msgid "Old message"
msgid "New message"
msgstr ""
```

The tool will translate:
- Empty `msgstr` entries
- Entries marked as `fuzzy`
- Entries with previous `msgid` comments (`#| msgid`)

## Step 4: Test the Setup

### 4.1 Verify Installation

```bash
# Check if all dependencies are installed
python -c "import requests, polib, dotenv; print('All dependencies installed successfully')"
```

### 4.2 Test API Connection

```bash
# Test with a small locale directory
python translate.py /path/to/your/locale
```

### 4.3 Expected Output

You should see output like:
```
Processing /path/to/locale/fr_FR/LC_MESSAGES/messages.po ...
Translated: 'Hello, world!' -> 'Bonjour le monde!'
Saved translations to /path/to/locale/fr_FR/LC_MESSAGES/messages.po
```

## Troubleshooting

### Common Issues

1. **"Error: Please set the GOOGLE_TRANSLATE_API_KEY environment variable"**
   - Make sure your `.env` file exists and contains the API key
   - Verify the API key is correct (no extra spaces or quotes)

2. **"403 Forbidden" or API errors**
   - Check that the Translation API is enabled in Google Cloud Console
   - Verify your API key has the correct permissions
   - Ensure you haven't exceeded API quotas

3. **"No such file or directory"**
   - Verify the locale directory path is correct
   - Check that the directory structure follows the gettext format

4. **Import errors**
   - Make sure you've activated your virtual environment
   - Run `pip install -r requirements.txt` again

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify your Google Cloud setup
3. Test with a simple `.po` file first
4. Open an issue on GitHub with the error details

## Cost Considerations

- Google Translate API charges per character translated
- Check current pricing at [Google Cloud Pricing](https://cloud.google.com/translate/pricing)
- Consider setting up billing alerts in Google Cloud Console
- Test with small files first to estimate costs

## Security Best Practices

1. Never commit your `.env` file or API keys to version control
2. Use API key restrictions in Google Cloud Console
3. Regularly rotate your API keys
4. Monitor API usage in Google Cloud Console
5. Consider using service accounts for production environments 