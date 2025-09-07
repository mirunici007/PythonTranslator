import customtkinter as ctk
import tkinter as tk
from translator_logic import languages, Translator

class AutocompleteComboBox(ctk.CTkFrame):
    def __init__(self,master,values,height,width,placeholder_text):
        super().__init__(master)

        self.values = values
        self.filtred_values = values
        self.suggestions_window_height = height
        self.suggestions_window_width = width
        self.placeholder_text = placeholder_text

        self.entry_text = ctk.CTkEntry(self, font = ctk.CTkFont(size = 15),width = 150,
                                  placeholder_text = self.placeholder_text)
        self.entry_text.grid(row = 0, column = 0, padx = 0, pady = 10)
        self.entry_text.bind("<KeyRelease>", self.update_suggestions)

        self.suggestions_window = None

    def update_suggestions(self,event = None):
        input_text = self.entry_text.get().lower()
        self.filtred_languages = [language for language in self.values if input_text in language.lower()]

        if self.suggestions_window:
            self.suggestions_window.destroy()

        if not self.filtred_languages:
            return
        
        self.suggestions_window = ctk.CTkToplevel(self)
        self.suggestions_window.wm_overrideredirect(True)

        x = self.winfo_rootx()
        y = self.winfo_rooty()+50
        self.suggestions_window.geometry(f"{self.suggestions_window_width}x{self.suggestions_window_height}+{x}+{y}")

        scroll_frame = ctk.CTkScrollableFrame(self.suggestions_window,
                                         width = self.suggestions_window_width - 50, height = self.suggestions_window_height)
        scroll_frame.grid(row = 0, column = 0)

        for index, value in enumerate(self.filtred_languages):
            button = ctk.CTkButton(scroll_frame, text = value, font = ctk.CTkFont(size = 15),
                                command = lambda v=value: self.select_language(v))
            button.grid(row = index, column = 0, padx = 10, pady = 5, sticky = "nsew")

    def select_language(self,value):
        self.entry_text.delete(0,"end")
        self.entry_text.insert(0,value)

        if self.suggestions_window:
            self.suggestions_window.destroy()
            self.suggestions_window = None

    def get_language(self):
        return self.entry_text.get()
           

class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Translator App")
        self.geometry("1125x600")
        self.app_language = "English"
        self.select_lang = "select language"
        

        self.label = ctk.CTkLabel(self, text = "Translator App", font = ctk.CTkFont(size = 30, weight = "bold"))
        self.label.grid(row = 0,column = 0, columnspan = 4, padx = 375, pady = 10, sticky = "w")

        self.lang_frame = ctk.CTkFrame(self, bg_color = "transparent", height=50)
        self.lang_frame.grid(row = 0, column = 2, padx = (0, 0), pady = 10, sticky = "nw")

        self.lang_choose = AutocompleteComboBox(self.lang_frame, list(languages.keys()),300,200,"   App Language",
                                                )
        self.lang_choose.grid(row = 0, column = 0, padx = (0, 20))
        self.lang_choose.entry_text.insert(0,"       "+self.app_language)

        
        self.translate_window_button = ctk.CTkButton(self.lang_frame, text="Translate window", command=self.update_ui_language, font=ctk.CTkFont(size=15, weight="bold"))
        self.translate_window_button.grid(row=1, column=0, columnspan=2, pady=(10,0), sticky="ew", padx=(0, 20))

        self.frame1 = ctk.CTkFrame(self, fg_color = "transparent")
        self.frame1.grid(row = 1, column = 0, padx = (40, 0), pady = 10, sticky = "w")

        self.autocombo1 = AutocompleteComboBox(self.frame1, list(languages.keys()),500,250,"   Select Language")
        self.autocombo1.grid(row = 1, column = 0, padx=10, pady = 10, sticky = "e")

        #self.button_source = ctk.CTkButton(self.frame1, text = "Select", command = self.autocombo1.get_language,
        #                                    font = ctk.CTkFont(size = 15, weight = "bold"))
        #self.button_source.grid(row = 1, column = 1, padx = (10,0), pady = 10, sticky = "w")

        self.text_input = ctk.CTkTextbox(self, width=400, height=200, fg_color="gray85", font = ctk.CTkFont(size = 20))
        self.text_input.grid(row=2, column=0, padx=(50,20), pady=(0, 10), sticky="nsew")

        self.frame2 = ctk.CTkFrame(self, fg_color = "transparent")
        self.frame2.grid(row = 1, column = 1, pady = 10, sticky = "w")

        self.autocombo2 = AutocompleteComboBox(self.frame2, list(languages.keys()),500,250,"   Select Language")
        self.autocombo2.grid(row = 1, column = 0, padx=(20,0), pady = 10, sticky = "w")

        #self.button_target = ctk.CTkButton(self.frame2, text = "Select", command = self.autocombo2.get_language,
        #                                    font = ctk.CTkFont(size = 15, weight = "bold"))
        #self.button_target.grid(row = 1, column = 1, padx = (20,0), pady = 10, sticky = "w")

        self.text_output = ctk.CTkTextbox(self, width=400, height=200, fg_color="gray85", font = ctk.CTkFont(size = 20))
        self.text_output.grid(row=2, column=1, padx=(20,0), pady=(0, 10), sticky="nsew")

        self.translate_button = ctk.CTkButton(self, text = "Translate", command = self.translate_input, 
                                              font = ctk.CTkFont(size = 20, weight = "bold"), width = 150)
        self.translate_button.grid(row = 3, column = 0, padx = (50,0), pady = (0,), sticky = "ew",columnspan=2)

        
        self.label.configure(text="Translator App", font=ctk.CTkFont(family="Arial", size=30, weight="bold"))
        if hasattr(self, 'button_source'):
            self.button_source.configure(text="Select", font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'button_target'):
            self.button_target.configure(text="Select", font=ctk.CTkFont(family="Arial", size=15))
        self.translate_button.configure(text="Translate", font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'translate_app_button'):
            self.translate_app_button.configure(text="Select application language", font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'confirm_lang_button'):
            self.confirm_lang_button.configure(text="Confirm application language", font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'translate_window_button'):
            self.translate_window_button.configure(text="Translate window", font=ctk.CTkFont(family="Arial", size=15, weight="bold"))
        self.autocombo1.entry_text.configure(placeholder_text="Select Language", font=ctk.CTkFont(family="Arial", size=15))
        self.autocombo2.entry_text.configure(placeholder_text="Select Language", font=ctk.CTkFont(family="Arial", size=15))
        self.lang_choose.entry_text.configure(placeholder_text="App Language", font=ctk.CTkFont(family="Arial", size=15))

        
        self.language_keys = list(languages.keys())
        
        self.lang_display_map = {}
        self.lang_reverse_map = {}
        
        for lang in self.language_keys:
            self.lang_display_map[lang] = lang
            self.lang_reverse_map[lang] = lang
        self.lang_choose.values = self.language_keys
        self.autocombo1.values = self.language_keys
        self.autocombo2.values = self.language_keys

    def translate_input(self):
        input_text = self.text_input.get("1.0","end").strip()
        
        source_lang_display = self.autocombo1.get_language()
        target_lang_display = self.autocombo2.get_language()
        source_lang = self.lang_reverse_map.get(source_lang_display, source_lang_display)
        target_lang = self.lang_reverse_map.get(target_lang_display, target_lang_display)

        if source_lang not in languages or target_lang not in languages or not input_text:
            return
        
        translator = Translator(source_lang, target_lang)
        translated_text = translator.translate_text(input_text)

        self.text_output.delete("1.0", "end")
        self.text_output.insert("1.0", translated_text)

    def update_app_language(self):
        new_language = self.lang_choose.get_language()
        if new_language in languages:
            self.app_language = new_language
            self.lang_choose.entry_text.delete(0,"end")
            self.lang_choose.entry_text.insert(0,"       "+self.app_language)
            self.label.configure(text=f"Translator App ({self.app_language})")
            
    def update_ui_language(self):
        selected_lang_display = self.lang_choose.get_language()
        
        selected_lang = self.lang_reverse_map.get(selected_lang_display, selected_lang_display)
        if not selected_lang or selected_lang not in languages:
            return
        translator = Translator("English", selected_lang)
        self.label.configure(text=translator.translate_text("Translator App"), font=ctk.CTkFont(family="Arial", size=30, weight="bold"))
        if hasattr(self, 'button_source'):
            self.button_source.configure(text=translator.translate_text("Select"), font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'button_target'):
            self.button_target.configure(text=translator.translate_text("Select"), font=ctk.CTkFont(family="Arial", size=15))
        self.translate_button.configure(text=translator.translate_text("Translate"), font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'translate_app_button'):
            self.translate_app_button.configure(text=translator.translate_text("Select application language"), font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'confirm_lang_button'):
            self.confirm_lang_button.configure(text=translator.translate_text("Confirm application language"), font=ctk.CTkFont(family="Arial", size=15))
        if hasattr(self, 'translate_window_button'):
            self.translate_window_button.configure(text=translator.translate_text("Translate window"), font=ctk.CTkFont(family="Arial", size=15, weight="bold"))
        
        translated_languages = [translator.translate_text(lang) for lang in self.language_keys]
        self.lang_display_map = dict(zip(self.language_keys, translated_languages))
        self.lang_reverse_map = dict(zip(translated_languages, self.language_keys))
        self.lang_choose.values = translated_languages
        self.autocombo1.values = translated_languages
        self.autocombo2.values = translated_languages
        self.lang_choose.entry_text.configure(placeholder_text=translator.translate_text("App Language"), font=ctk.CTkFont(family="Arial", size=15))
        self.autocombo1.entry_text.configure(placeholder_text=translator.translate_text("Select Language"), font=ctk.CTkFont(family="Arial", size=15))
        self.autocombo2.entry_text.configure(placeholder_text=translator.translate_text("Select Language"), font=ctk.CTkFont(family="Arial", size=15))
