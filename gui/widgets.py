import tkinter as tk
from tkinter import messagebox
from blockchain.connection import BlockchainConnection

class AccountEntry(tk.Entry):
    def __init__(self, master=None, blockchain_connection: BlockchainConnection = None, **kwargs):
        super().__init__(master, **kwargs)
        self.blockchain_connection = blockchain_connection

class PrivateKeyEntry(tk.Entry):
    def __init__(self, master=None, blockchain_connection: BlockchainConnection = None, **kwargs):
        super().__init__(master, **kwargs)
        self.blockchain_connection = blockchain_connection

class CommandButton(tk.Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

class LogText(tk.Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

class BalanceFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
