# Examples

This document provides practical examples of how to use the PO File Translator.

## Directory Structure Example

Here's how your locale directory should be organized:

```
my_project/
└── locale/
    ├── en_US/
    │   └── LC_MESSAGES/
    │       ├── messages.po
    │       └── django.po
    ├── fr_FR/
    │   └── LC_MESSAGES/
    │       ├── messages.po
    │       └── django.po
    ├── es_ES/
    │   └── LC_MESSAGES/
    │       ├── messages.po
    │       └── django.po
    └── de_DE/
        └── LC_MESSAGES/
            ├── messages.po
            └── django.po
```

## Sample PO File (Before Translation)

Here's an example of a `messages.po` file before running the translator:

```po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: MyProject 1.0\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-01-15 10:30+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: fr\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: views.py:25
msgid "Welcome to our application"
msgstr ""

#: views.py:42
msgid "Please enter your name"
msgstr ""

#: views.py:58
#, fuzzy
msgid "Save changes"
msgstr "Sauvegarder"

#: views.py:73
msgid "Delete item"
msgstr ""

#: views.py:89
#| msgid "Old login message"
msgid "Please log in to continue"
msgstr ""

#: forms.py:15
msgid "Email address"
msgstr ""

#: forms.py:23
msgid "Password"
msgstr ""
```

## Sample PO File (After Translation)

After running the translator, the same file would look like this:

```po
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
msgid ""
msgstr ""
"Project-Id-Version: MyProject 1.0\n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2024-01-15 10:30+0000\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"Language: fr\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"

#: views.py:25
msgid "Welcome to our application"
msgstr "Bienvenue dans notre application"

#: views.py:42
msgid "Please enter your name"
msgstr "Veuillez entrer votre nom"

#: views.py:58
msgid "Save changes"
msgstr "Sauvegarder les modifications"

#: views.py:73
msgid "Delete item"
msgstr "Supprimer l'élément"

#: views.py:89
msgid "Please log in to continue"
msgstr "Veuillez vous connecter pour continuer"

#: forms.py:15
msgid "Email address"
msgstr "Adresse e-mail"

#: forms.py:23
msgid "Password"
msgstr "Mot de passe"
```

## Command Examples

### Basic Usage

```bash
# Translate all PO files in the locale directory
python translate.py ./locale
```

### Real-world Examples

```bash
# Django project
python translate.py ./myproject/locale

# Flask-Babel project
python translate.py ./babel/translations

# Custom locale directory
python translate.py /path/to/my/translations
```

## Console Output Examples

### Successful Translation

```
Processing ./locale/fr_FR/LC_MESSAGES/messages.po ...
Translated: 'Welcome to our application' -> 'Bienvenue dans notre application'
Translated: 'Please enter your name' -> 'Veuillez entrer votre nom'
Translated: 'Save changes' -> 'Sauvegarder les modifications'
Translated: 'Delete item' -> 'Supprimer l'élément'
Translated: 'Please log in to continue' -> 'Veuillez vous connecter pour continuer'
Translated: 'Email address' -> 'Adresse e-mail'
Translated: 'Password' -> 'Mot de passe'
Saved translations to ./locale/fr_FR/LC_MESSAGES/messages.po

Processing ./locale/es_ES/LC_MESSAGES/messages.po ...
Translated: 'Welcome to our application' -> 'Bienvenido a nuestra aplicación'
Translated: 'Please enter your name' -> 'Por favor ingrese su nombre'
Translated: 'Save changes' -> 'Guardar cambios'
Translated: 'Delete item' -> 'Eliminar elemento'
Translated: 'Please log in to continue' -> 'Inicie sesión para continuar'
Translated: 'Email address' -> 'Dirección de correo electrónico'
Translated: 'Password' -> 'Contraseña'
Saved translations to ./locale/es_ES/LC_MESSAGES/messages.po
```

### Error Handling

```
Processing ./locale/fr_FR/LC_MESSAGES/messages.po ...
Translated: 'Welcome to our application' -> 'Bienvenue dans notre application'
Error translating 'Complex technical term': 400 Bad Request
Translated: 'Save changes' -> 'Sauvegarder les modifications'
Saved translations to ./locale/fr_FR/LC_MESSAGES/messages.po
```

## Integration Examples

### With Django

```bash
# After updating your source code and running makemessages
python manage.py makemessages -l fr -l es -l de

# Translate the updated PO files
python translate.py ./locale

# Compile the translations
python manage.py compilemessages
```

### With Flask-Babel

```bash
# Extract messages
pybabel extract -F babel.cfg -o messages.pot .

# Update existing translations
pybabel update -i messages.pot -d babel/translations

# Translate the updated PO files
python translate.py ./babel/translations

# Compile translations
pybabel compile -d babel/translations
```

### In a CI/CD Pipeline

```yaml
# Example GitHub Actions workflow
name: Auto-translate PO files
on:
  push:
    paths:
      - 'locale/**/*.po'

jobs:
  translate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Translate PO files
        env:
          GOOGLE_TRANSLATE_API_KEY: ${{ secrets.GOOGLE_TRANSLATE_API_KEY }}
        run: python translate.py ./locale
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add locale/
          git commit -m "Auto-translate PO files" || exit 0
          git push
```

## Tips and Best Practices

1. **Test with a small subset first**: Start with one language and a few strings to verify the setup
2. **Review translations**: Machine translations may need human review for accuracy
3. **Backup your files**: Always backup your PO files before running the translator
4. **Use version control**: Commit your files before translation so you can see the changes
5. **Monitor API usage**: Keep track of your Google Translate API usage to manage costs 