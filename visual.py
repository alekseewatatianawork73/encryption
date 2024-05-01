import logic
import customtkinter as ctk

def handle_pressing_btn_result():
    input_data = entry_input.get()
    output_data = 0
    if cmbbox_operations.get() == "Расшифровка морзе":
        output_data = logic.rmorze(input_data) 
    elif cmbbox_operations.get() == "Зашифровка морзе":
        output_data = logic.zmorze(input_data)  
    elif cmbbox_operations.get() == "Зашифровка шифра Цезаря":
        output_data = logic.zc(input_data, input())
    entry_output.configure(state="normal") 
    entry_output.delete(0, "end") 
    entry_output.insert(0, output_data) 
    entry_output.configure(state="readonly") 


def hide(choice):
    if choice == "Зашифровка шифра Цезаря" or choice == "Расшифровка шифра Цезаря":
        lbl_k.grid(row=2, column=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
        k.grid(row=3, column=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
    else:
        lbl_k.grid_remove()  # удаляем текстовую метку для ключа
        k.grid_remove()      # удаляем поле ввода ключа



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Расшифровка и зашифровка") 
root.geometry("1000x500")

lbl_start_message = ctk.CTkLabel(master=root)  # root - главное окно
lbl_start_message.configure(text="Выберите операцию из списка:")

k = ctk.CTkEntry(master=root)
k.configure(justify="center")
lbl_k = ctk.CTkLabel(master=root)
lbl_k.configure(text="Ключ:")


operations = ["Расшифровка морзе", "Зашифровка морзе", "Зашифровка шифра Цезаря", "Расшифровка шифра Цезаря"]
cmbbox_operations = ctk.CTkComboBox(master=root)
cmbbox_operations.configure(justify="center", values=operations, state="readonly", command=hide)
#justify - расположение по центру, state - только для чтения
cmbbox_operations.set("Расшифровка морзе")  # значение по умолчанию

lbl_input, lbl_output = ctk.CTkLabel(master=root), ctk.CTkLabel(master=root)
lbl_input.configure(text="Текст:")
lbl_output.configure(text="Результат:")

entry_input = ctk.CTkEntry(master=root)
entry_input.configure(justify="center")

entry_output = ctk.CTkEntry(master=root)
entry_output.configure(justify="center", state="readonly")



btn_result = ctk.CTkButton(master=root)
btn_result.configure(text="Получить результат", command=handle_pressing_btn_result)

rows, columns = 7, 7

for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

lbl_start_message.grid(row=0, column=3, columnspan=2, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
cmbbox_operations.grid(row=1, column=3, columnspan=2, sticky="ew")
lbl_input.grid(row=2, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
lbl_output.grid(row=2, column=5, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
entry_input.grid(row=3, column=1, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
entry_output.grid(row=3, column=5, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")
btn_result.grid(row=4, column=3, ipadx=4, ipady=4, padx=6, pady=6, sticky="nsew")



root.mainloop()
