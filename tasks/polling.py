from blockchain.connection import BlockchainConnection
from tkinter import messagebox

class PollingTask:
    def __init__(self, blockchain_connection: BlockchainConnection):
        self.blockchain_connection = blockchain_connection

    def start(self):
        try:
            self.blockchain_connection.register_worker()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start polling: {str(e)}")

    def stop(self):
        try:
            self.blockchain_connection.remove_worker()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop polling: {str(e)}")
