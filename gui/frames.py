import tkinter as tk
from .widgets import AccountEntry, PrivateKeyEntry, CommandButton, LogText, BalanceFrame
from blockchain.connection import BlockchainConnection
from tasks.polling import PollingTask


class MainFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()

        self.blockchain_connection = BlockchainConnection()
        self.polling_task = PollingTask(self.blockchain_connection)

        self.balance_frame = BalanceFrame(self)
        self.balance_frame.pack(fill=tk.X)

        self.account_entry = AccountEntry(self, self.blockchain_connection)
        self.account_entry.pack(fill=tk.X)

        self.private_key_entry = PrivateKeyEntry(self, self.blockchain_connection)
        self.private_key_entry.pack(fill=tk.X)

        self.connect_button = CommandButton(self, "Connect Wallet", self.blockchain_connection.connect_wallet)
        self.connect_button.pack()

        self.register_button = CommandButton(self, "Register Worker", self.blockchain_connection.register_worker,
                                             state=tk.DISABLED)
        self.register_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = CommandButton(self, "Remove Worker", self.blockchain_connection.remove_worker,
                                           state=tk.DISABLED)
        self.remove_button.pack(side=tk.RIGHT, padx=10)

        self.start_button = CommandButton(self, "Start Polling", self.polling_task.start, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = CommandButton(self, "Stop Polling", self.polling_task.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.log_text = LogText(self)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5)
