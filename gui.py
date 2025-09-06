import customtkinter as ctk
import tkinter as tk
from translator_logic import languages

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
        self.geometry("800x600")

        self.label = ctk.CTkLabel(self, text = "Translator App", font = ctk.CTkFont(size = 30, weight = "bold"))
        self.label.grid(row = 0,column = 0, columnspan = 4, padx = 275, pady = 10, sticky = "nsew")

        self.frame1 = ctk.CTkFrame(self, fg_color = "transparent")
        self.frame1.grid(row = 1, column = 0, pady = 10, sticky = "w")

        self.autocombo1 = AutocompleteComboBox(self.frame1, list(languages.keys()),200,250,"Select Language")
        self.autocombo1.grid(row = 1, column = 0, padx=10, pady = 10, sticky = "e")

        self.button_source = ctk.CTkButton(self.frame1, text = "Select", command = self.autocombo1.get_language,
                                            font = ctk.CTkFont(size = 15, weight = "bold"))
        self.button_source.grid(row = 1, column = 1, padx = (20,0), pady = 10, sticky = "w")

        self.text_input = ctk.CTkTextbox(self, width=250, height=200, fg_color="gray85", font = ctk.CTkFont(size = 15))
        self.text_input.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")

        self.frame2 = ctk.CTkFrame(self, fg_color = "transparent")
        self.frame2.grid(row = 1, column = 1, pady = 10, sticky = "w")

        self.autocombo2 = AutocompleteComboBox(self.frame2, list(languages.keys()),200,250,"Select Language")
        self.autocombo2.grid(row = 1, column = 0, padx=(20,0), pady = 10, sticky = "w")

        self.button_target = ctk.CTkButton(self.frame2, text = "Select", command = self.autocombo2.get_language,
                                            font = ctk.CTkFont(size = 15, weight = "bold"))
        self.button_target.grid(row = 1, column = 1, padx = (0,0), pady = 10, sticky = "w")

        self.text_output = ctk.CTkTextbox(self, width=250, height=200, fg_color="gray85", font = ctk.CTkFont(size = 15))
        self.text_output.grid(row=2, column=1, padx=(20,0), pady=(0, 10), sticky="nsew")