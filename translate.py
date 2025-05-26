import os
import sys
import requests
import polib


def translate_text(text, target_lang, api_key):
    """Translate text via Google Translate API."""
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": target_lang,
        "format": "text",
        "key": api_key
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data["data"]["translations"][0]["translatedText"]

def main():
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    if not api_key:
        print("Error: Please set the GOOGLE_TRANSLATE_API_KEY environment variable.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print(f"Usage: python {os.path.basename(sys.argv[0])} /path/to/your/locale_dir")
        sys.exit(1)

    locale_dir = sys.argv[1]
    if not os.path.isdir(locale_dir):
        print(f"Error: '{locale_dir}' is not a valid directory.")
        sys.exit(1)

    for lang in os.listdir(locale_dir):
        lang_path = os.path.join(locale_dir, lang, "LC_MESSAGES")
        if not os.path.isdir(lang_path):
            continue
        for fname in os.listdir(lang_path):
            if not fname.endswith(".po"):
                continue
            po_path = os.path.join(lang_path, fname)
            print(f"Processing {po_path} ...")
            po = polib.pofile(po_path)
            updated = False
            target = lang.replace("_", "-")
            for entry in po:
                if entry.obsolete:
                    continue

                # detect previous msgid (#| msgid "...")
                has_previous = getattr(entry, 'previous_msgid', None) not in (None, '')

                # determine if translation is needed:
                # - empty msgstr
                # - fuzzy flag
                # - has a previous msgid comment
                needs_translation = has_previous or not entry.msgstr or 'fuzzy' in entry.flags

                if needs_translation:
                    try:
                        # always translate the current msgid
                        translation = translate_text(entry.msgid, target, api_key)
                        entry.msgstr = translation
                        updated = True
                        print(f"Translated: '{entry.msgid}' -> '{translation}'")

                        # clear fuzzy flag if present
                        if 'fuzzy' in entry.flags:
                            entry.flags.remove('fuzzy')

                        # remove previous-msgid comment if present
                        if has_previous:
                            entry.previous_msgid = None

                    except Exception as e:
                        print(f"Error translating '{entry.msgid}': {e}")

            if updated:
                po.save(po_path)
                print(f"Saved translations to {po_path}")

if __name__ == "__main__":
    import dotenv
    dotenv.load_dotenv()
    main()
