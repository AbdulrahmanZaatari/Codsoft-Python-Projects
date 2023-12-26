import tkinter as t
from tkinter import simpledialog, messagebox, Listbox, Scrollbar, VERTICAL, END
class Contact:
    def __init__(self, identification, name, phoneNumber, email, address):
        self.id = identification
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.address = address
    def __str__(self):
        return f"ID:{self.id}, Name: {self.name}, phoneNumber: {self.phoneNumber}, email: {self.email}, address: {self.address}"
class Contact_Book:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management")
        self.contacts = []
        self.count = 0
        self.setup_ui()
    def setup_ui(self):
        self.listbox = Listbox(self.root)
        self.scrollbar = Scrollbar(self.root, orient = VERTICAL, command = self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side = t.LEFT, fill = t.BOTH, expand = True)
        self.scrollbar.pack(side = t.LEFT, fill = t.Y)
        t.Button (self.root, text = "Add contact", command = self.add_contact).pack(fill = t.X)
        t.Button (self.root, text = "Delete contact", command = self.delete_contact).pack(fill = t.X)
        t.Button (self.root, text = "View contacts", command = self.view_contacts).pack(fill = t.X)
        t.Button (self.root, text = "Search Contacts", command = self.search_contacts).pack(fill = t.X)
        t.Button (self.root, text = "Update Contacts", command = self.update_contacts).pack(fill = t.X)
    def add_contact(self):
        name = simpledialog.askstring ("name", "Enter contact's name", parent = self.root)
        phoneNumber = simpledialog.askstring ("phoneNumber", "Enter contact's phone number", parent = self.root)
        email = simpledialog.askstring ("email", "Enter contact's email", parent = self.root)
        address = simpledialog.askstring ("address", "Enter contact's address", parent = self.root)
        identification = self.count
        self.count = self.count + 1
        new_contact = Contact (identification, name, phoneNumber, email, address)
        self.contacts.append(new_contact)
        self.view_contacts()
    def view_contacts(self):
         self.listbox.delete(0, END)
         for contact in self.contacts:
            self.listbox.insert(END, contact)
    def delete_contact(self):
        selected_contact = self.listbox.curselection()
        if selected_contact:
            del self.contacts[selected_contact[0]]
            self.view_contacts()
        else:
            messagebox.showinfo("Selection Error", "Please select a contact to delete.")
    def search_contacts(self):
        query = simpledialog.askstring("Search", "Enter contact's name or phone number", parent=self.root)
        if not query:
            messagebox.showinfo("Search Error", "Search query cannot be empty.")
            return
        self.listbox.delete(0, END)
        for contact in self.contacts:
            if query in contact.phoneNumber or query.lower() in contact.name:
                self.listbox.insert(END, contact)
    def update_contacts(self):
        query = simpledialog.askstring("Update", "Enter contact's name or phone number", parent = self.root)
        if not query:
            messagebox.showinfo("Search Error", "No contact found.")
            return
        for contact in self.contacts:
            if query.lower() in contact.name or query in contact.phoneNumber:
                choice = simpledialog.askstring("Update", "What do you want to update (n,pn,e,a)", parent = self.root)
                if choice == "n":
                    self.listbox.delete(0,END)
                    name = simpledialog.askstring("New name", "Insert new name", parent = self.root)
                    contact.name = name
                    self.listbox.insert(END, contact)
                elif choice == "pn":
                    self.listbox.delete(0,END)
                    phone_number = simpledialog.askstring("New phone number", "Insert new phone number", parent = self.root)
                    contact.phoneNumber = phone_number
                    self.listbox.insert(END, contact)
                elif choice == "e":
                    self.listbox.delete(0,END)
                    email = simpledialog.askstring("New email", "Insert new email", parent = self.root)
                    contact.email = email
                    self.listbox.insert(END, contact)
                elif choice == "a":
                    self.listbox.delete(0,END)
                    address = simpledialog.askstring("New address", "Insert new address", parent = self.root)
                    contact.address = address
                    self.listbox.insert(END, contact)
                else:
                    print ("You need to choose a valid choice (n,pn,e,a)")
                


def main():
    root = t.Tk()
    window_width = 600
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    contact_list = Contact_Book(root)
    root.mainloop()
main()

    

        
        
        
        
    
        
