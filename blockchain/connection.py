import json
import os
import sys
from web3 import Web3
from tkinter import messagebox
from src.getPower import get_power
from config.config import get_config


class BlockchainConnection:
    def __init__(self):
        self.web3, self.config = self.initialize_web3()
        self.contract_address = self.web3.to_checksum_address(self.config['contract_address'])
        abi_path = os.path.join(self.get_basedir(), '../ABI', 'Marketplace.json')
        with open(abi_path, 'r') as f:
            abi = json.load(f)

        self.marketplace_contract = self.web3.eth.contract(address=self.contract_address, abi=abi['abi'])
        self.gas = self.config['gas']
        self.gasPrice = self.config['gasPrice']
        self.gasPrice_wei = self.web3.to_wei(str(self.gasPrice), 'gwei')
        self.chainId = self.config['chainId']
        self.computing_power = int(get_power())
        self.is_connected = False

    def get_basedir(self):
        if getattr(sys, 'frozen', False):
            return sys._MEIPASS
        return os.path.dirname(os.path.realpath(__file__))

    def initialize_web3(self):
        config = get_config()
        provider = config['provider']
        web3 = Web3(Web3.HTTPProvider(provider))
        return web3, config

    def connect_wallet(self, account_address: str, private_key: str):
        try:
            self.account_address = self.web3.to_checksum_address(account_address)
            self.private_key = private_key
            self.is_connected = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect wallet: {str(e)}")

    def register_worker(self):
        try:
            tx = self.marketplace_contract.functions.registerWorker(self.computing_power).buildTransaction({
                'chainId': self.chainId,
                'gas': self.gas,
                'gasPrice': self.gasPrice_wei,
                'nonce': self.web3.eth.getTransactionCount(self.account_address)
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register worker: {str(e)}")

    def remove_worker(self):
        try:
            tx = self.marketplace_contract.functions.removeWorker().buildTransaction({
                'chainId': self.chainId,
                'gas': self.gas,
                'gasPrice': self.gasPrice_wei,
                'nonce': self.web3.eth.getTransactionCount(self.account_address)
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
            self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove worker: {str(e)}")
