import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class App(ctk.CTk):
    def __init__(self, win_width: int = 200, win_height: int = 400) -> None:
        """
        This is the main app class.
        :param win_width: This is the width of the window.
        :param win_height: This is the height of the window.
        """
        super().__init__()

        self.__buttons_frame = None  # This variable contain buttons frame
        self.__output_frame = None  # This variable contain result frame (what show example)

        self.__result_label = None  # This variable contain result label (what show actual example)
        self.__symbol_label = None  # This variable contain symbol label (what show selected symbol)

        self.title = 'Calculator'
        self.geometry(f'{win_width}x{win_height}')
        self.resizable(False, False)
        self.__init_frames()
        self.__init_buttons()
        self.__init_result()

        self.__example = ''  # This variable contain an actual example
        self.__buffer_example = ''  # This variable contain a buffer of example (what show in result)
        self.__buffer_symbol = ''  # This variable contain a buffer of symbol (what show in result)

    def __init_frames(self) -> None:
        """
        This function is used to initialize the frames.
        :return: None
        """
        self.__buttons_frame = ctk.CTkFrame(self, 350, 350, corner_radius=0)
        self.__buttons_frame.place(x=0, y=100)

        self.__output_frame = ctk.CTkFrame(self, 350, 100, corner_radius=0)
        self.__output_frame.place(x=0, y=0)

    def __init_result(self) -> None:
        """
        This function is used to initialize the result.
        :return: None
        """
        self.__result_label = ctk.CTkLabel(self.__output_frame, text='0', font=("Arial", 32))
        self.__result_label.place(x=100, y=20)

        self.__symbol_label = ctk.CTkLabel(self.__output_frame, text='', font=("Arial", 32))
        self.__symbol_label.place(x=20, y=20)

    def __init_buttons(self) -> None:
        """
        This function is used to initialize the buttons.
        :return: None
        """
        ctk.CTkButton(self.__buttons_frame, text='0', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(0)).grid(row=0, column=0, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='1', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(1)).grid(row=0, column=1, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='2', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(2)).grid(row=0, column=2, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='3', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(3)).grid(row=1, column=0, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='4', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(4)).grid(row=1, column=1, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='5', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(5)).grid(row=1, column=2, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='6', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(6)).grid(row=2, column=0, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='7', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(7)).grid(row=2, column=1, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='8', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(8)).grid(row=2, column=2, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='9', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str(9)).grid(row=3, column=0, padx=0, pady=0)

        ctk.CTkButton(self.__buttons_frame, text='+', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('+')).grid(row=0, column=4, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='-', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('-')).grid(row=1, column=4, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='*', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('*')).grid(row=2, column=4, padx=0, pady=0)
        ctk.CTkButton(self.__buttons_frame, text='/', width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('/')).grid(row=3, column=4, padx=0, pady=0)

        ctk.CTkButton(self.__buttons_frame, text="=", width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('=')).grid(row=3, column=1, padx=0, pady=0)

        ctk.CTkButton(self.__buttons_frame, text="C", width=88, height=88, corner_radius=0, font=("Arial", 32),
                      command=lambda: self.__add_to_str('c')).grid(row=3, column=2, padx=0, pady=0)

    def __add_to_str(self, element) -> None:
        """
        This function is used to add a string to the result.
        :param element: This is the string to be added.
        :return: None
        """
        if element == 0 and len(self.__example) == 0:
            return
        if element == '=':
            try:
                print(eval(self.__example))
                self.__primer = str(eval(self.__example))
                self.__buffer_symbol = ''
                self.__buffer_primer = self.__primer
            except SyntaxError:
                self.__buffer_primer = ''
                self.__primer = ''
                self.__buffer_symbol = ''
                self.__result("Syntax Error")
            return
        if element == '+' or element == '-' or element == '*' or element == '/':
            self.__example += str(' {} '.format(element))
            self.__buffer_primer = ''
            self.__buffer_symbol = element
            self.__result('0')
            return
        if element == 'c':
            self.__primer = ''
            self.__buffer_primer = ''
            self.__buffer_symbol = ''
            self.__result('0')
            return
        if len(self.__buffer_example) > 14:
            return

        self.__example += str(element)
        self.__buffer_example += str(element)

        print(self.__example)

        self.__result()

    def __result(self, custom_result: str = None) -> None:
        """
        This function is used to display the result.
        :param custom_result: This is the string to be displayed (optional).
        :return:
        """
        self.__result_label.configure(text=self.__buffer_primer)
        self.__symbol_label.configure(text=self.__buffer_symbol)
        if custom_result:
            self.__result_label.configure(text=custom_result)

    def render(self) -> None:
        """
        This function is used to render the app.
        :return:
        """

        self.mainloop()


app = App(350, 450)
app.render()
