from imports import *

ctk.set_appearance_mode("dark")


def run_app():
    load_file_name = None

    def update_title(master, new_title):
        master.title(new_title)

    def create_text_file(master, text_box):
        nonlocal load_file_name
        load_file_name = None
        update_title(master, 'text.txt')
        text_box.delete('0.0', 'end')

    def load_text_file(master, text_box):
        file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        if file_path:
            nonlocal load_file_name
            load_file_name = file_path.split("/")[-1]
            update_title(master, load_file_name)
            text_box.delete('0.0', 'end')
            with open(file_path, "r", encoding='utf-8') as file:
                lines = file.readlines()
                lines.reverse()
                for line in lines:
                    text_box.insert("0.0", line)

    def save_text_file(text_box):
        file_path = filedialog.asksaveasfilename(filetypes=[('Text Files', '*.txt')],
                                                 initialfile='text.txt' if load_file_name is None else load_file_name,
                                                 defaultextension='.txt')
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text_box.get('0.1', 'end'))
            file.close()

    def display_about_frame(master):
        new_root = ctk.CTkToplevel(master)
        new_root.title('About "Text Editor"')
        new_root.after(300, lambda: new_root.iconbitmap("root_icon.ico"))
        new_root.geometry("500x200")
        new_root.resizable(False, False)

        icon_text_label = ctk.CTkLabel(master=new_root,
                                       text="Text Editor",
                                       fg_color="black",
                                       corner_radius=8,
                                       font=("System", 30))
        icon_text_label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

        description_label = ctk.CTkLabel(master=new_root,
                                         text="A hand-made program that is similar to the basic text editor.\nFunctionality is slightly reduced, but you can use it just like a text editor.",
                                         font=("System", 10),
                                         fg_color="black",
                                         corner_radius=8)
        description_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        github_button = ctk.CTkButton(master=new_root, text="My Github",
                                      fg_color="green4",
                                      corner_radius=15,
                                      text_color="black",
                                      hover_color="dark green",
                                      command=lambda: webbrowser.open("https://github.com/Vladislavus1"),
                                      font=("System", 22))
        github_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

        new_root.transient(master)
        new_root.grab_set()
        master.wait_window(new_root)

    root = ctk.CTk()
    root.title("Text Editor")
    root.iconbitmap('root_icon.ico')
    root.resizable(False, False)
    root.geometry("600x700")

    title_menu = CTkMenuBar(master=root)
    title_file_button = title_menu.add_cascade("File")
    title_about_button = title_menu.add_cascade("About", postcommand=lambda: display_about_frame(root))

    textbox = ctk.CTkTextbox(master=root, width=600, height=700, corner_radius=0)
    textbox.pack(padx=0.5, pady=0.2, anchor=ctk.CENTER)

    title_file_dropdown = CustomDropdownMenu(widget=title_file_button)
    title_file_dropdown.add_option(option="Create", command=lambda: create_text_file(root, textbox))
    title_file_dropdown.add_option(option="Open", command=lambda: load_text_file(root, textbox))
    title_file_dropdown.add_option(option="Save", command=lambda: save_text_file(textbox))

    root.mainloop()


if __name__ == "__main__":
    run_app()