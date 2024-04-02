from web3 import Web3
from web3.exceptions import Web3Exception

# Intentar conectarse a la red de Ganache
try:
    ganache_url = "http://localhost:7545"
    w3 = Web3(Web3.HTTPProvider(HTTP://127.0.0.1:7545))

if not w3.is_connected():
    print("No se pudo conectar a Ganache. Asegúrate de que Ganache esté en funcionamiento.")
    exit() 

except Exception as e:
print(f"Error al intentar conectar con Ganache: {e}")
exit()

print("Conectado a Ganache")

# Direccion del contrato inteligente desplegado
contract_address = "0x5Dc26573c3aC5b203974D5827253f95b7E128368" 

# Direccion del socio principal
socio_principal_address = "0x99105689Fb4e509D7BF8939d6AB7E12007c2ad42" 

# Clave privada del socio principal (necesaria para firmar transacciones)
socio_principal_private_key = "0x394701418c190a01dc390be8a9fd4d78d20f6efa7b3b75737aef6a085e2b1781" #


contract_abi = “[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"GarantiaLiquidada","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"PrestamoAprobado","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"}],"name":"PrestamoReembolsado","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"prestatario","type":"address"},{"indexed":false,"internalType":"uint256","name":"monto","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"plazo","type":"uint256"}],"name":"SolicitudPrestamo","type":"event"},{"inputs":[{"internalType":"address","name":"nuevoCliente","type":"address"}],"name":"altaCliente","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"nuevoPrestamista","type":"address"}],"name":"altaPrestamista","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"aprobarPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"clientes","outputs":[{"internalType":"bool","name":"activado","type":"bool"},{"internalType":"uint256","name":"saldoGarantia","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"depositarGarantia","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"empleadosPrestamista","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"liquidarPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"},{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"obtenerDetalleDePrestamo","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"prestatario","type":"address"},{"internalType":"uint256","name":"monto","type":"uint256"},{"internalType":"uint256","name":"plazo","type":"uint256"},{"internalType":"uint256","name":"tiempoSolicitud","type":"uint256"},{"internalType":"uint256","name":"tiempoLimite","type":"uint256"},{"internalType":"bool","name":"aprobado","type":"bool"},{"internalType":"bool","name":"reembolsado","type":"bool"},{"internalType":"bool","name":"liquidado","type":"bool"}],"internalType":"struct PrestamoDefi.Prestamo","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"prestatario_","type":"address"}],"name":"obtenerPrestamosPorPrestatario","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id_","type":"uint256"}],"name":"reembolsarPrestamo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"socioPrincipal","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"monto_","type":"uint256"},{"internalType":"uint256","name":"plazo_","type":"uint256"}],"name":"solicitarPrestamo","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"}]”

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Funcion para enviar transaccion:
def enviar_transaccion(w3, txn_dict, private_key):  
    try:

        signed_txn = w3.eth.account.sign_transaction(txn_dict, private_key=private_key)
txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)             

return txn_receipt
except Exception as e:

# Lanzar la excepción para ser capturada por la función que llama
raise Exception(f"Error al enviar la transacción: {e}")


# Funciones de interacción con el contrato
# Función para dar de alta un prestamista por el socio principal
def alta_prestamista(nuevo_prestamista_address): 
     try:

