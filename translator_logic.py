from deep_translator import GoogleTranslator

languages = {
    #  Western Europe
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",

    #   Eastern & Central Europe
    "Romanian": "ro",
    "Polish": "pl",
    "Czech": "cs",
    "Slovak": "sk",
    "Hungarian": "hu",
    "Bulgarian": "bg",
    "Croatian": "hr",
    "Slovenian": "sl",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Russian": "ru",
    "Ukrainian": "uk",
    "Serbian": "sr",
    "Belarusian": "be",

    #   Northern Europe
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Finnish": "fi",
    "Icelandic": "is",
    "Irish": "ga",

    #   Southern Europe
    "Greek": "el",
    "Macedonian": "mk",
    "Albanian": "sq",
    "Bosnian": "bs",
    "Montenegrin": "me",
    "Catalan": "ca",
    "Basque": "eu",
    "Galician": "gl",
    "Maltese": "mt",

    # --- Asia ---
    "Turkish": "tr",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Arabic": "ar",

    # --- Africa ---
    "Swahili": "sw",
    "Amharic": "am",
    "Zulu": "zu",
}

class Translator:
    def __init__(self, source_language, target_language):

        self.source_language = source_language
        self.target_language = target_language
        
    def translate_text(self, input_text):
        if self.source_language not in languages.keys() or self.target_language not in languages.keys():
            raise ValueError("Unsupported language")

        translated_text = GoogleTranslator(source=languages[self.source_language],
                                            target=languages[self.target_language]).translate(input_text)
        return translated_text