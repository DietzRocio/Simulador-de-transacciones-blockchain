import tkinter as tk
from tkinter import messagebox
from blockchain import Block, Transaction, create_genesis_block, create_new_block_with_transactions_and_pow, is_chain_valid

class BlockchainApp:
    def __init__(self, root):
        self.blockchain = [create_genesis_block()]
        
        root.title("Blockchain App 🫦")

        #botón para + bloque
        self.add_block_button = tk.Button(root, text="Añadir Bloque", command=self.add_block)
        self.add_block_button.pack(pady=10)

        #botón para + transacción
        self.add_transaction_button = tk.Button(root, text="Añadir Transacción", command=self.add_transaction)
        self.add_transaction_button.pack(pady=10)

        #area para mostrar el estado de la blockchain
        self.status_text = tk.Text(root, height=20, width=60)
        self.status_text.pack(pady=10)

        #actualiza la interfaz con el estado de la blockchain
        self.update_status()

    def add_block(self):
        transaction_pool = [
            Transaction("pepe", "patricia", 10),
            Transaction("marta", "pepe", 20),
            Transaction("homero", "patricia", 30)
        ]
        new_block = create_new_block_with_transactions_and_pow(self.blockchain[-1], transaction_pool, 4)
        self.blockchain.append(new_block)
        self.update_status()

    def add_transaction(self):
        # Ejemplo simple de cómo añadir una transacción
        transaction = Transaction("pepe", "argento", 10)
        if self.blockchain:
            self.blockchain[-1].transactions.append(transaction)
        self.update_status()

    def update_status(self):
        self.status_text.delete(1.0, tk.END)
        for block in self.blockchain:
            self.status_text.insert(tk.END, str(block) + "\n")
        self.status_text.insert(tk.END, "La cadena es válida: " + str(is_chain_valid(self.blockchain)) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()
