#definimos la estructura del bloque ✔
import hashlib
import time
difficulty = 5

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash_result, nonce):
        self.index = index               #posición del bloque en la cadena
        self.previous_hash = previous_hash  #hash del bloque anterior
        self.timestamp = timestamp        #momento de creación del bloque
        self.transactions = transactions
        self.data = data                  #transacciones o información del bloque
        self.hash = hash_result                #hash del bloque actual
        self.nonce = nonce


def __str__(self):
        transactions_str = "\n".join([str(tx) for tx in self.transactions])
        return (f"Bloque {self.index}:\nHash anterior: {self.previous_hash}\n"
                f"Timestamp: {self.timestamp}\nTransacciones:\n{transactions_str}\n"
                f"Hash: {self.hash}\nNonce: {self.nonce}\n{'-'*40}")

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"{self.sender} envía {self.amount} a {self.recipient}"



def calculate_hash(index, previous_hash, timestamp, data):
    #concatenamos los atributos del bloque en una cadena
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    
    #generamos el hash SHA-256
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


#------------------------ prueba1--------------------------------------------------------------------
#if __name__ == "__main__":
 #   index = 1
  #  previous_hash = "0"
   # timestamp = time.time()
    #data = "transacción 🤞"
    
    #hash_value = calculate_hash(index, previous_hash, timestamp, data)
    #print(f"Hash del bloque: {hash_value}")
#--------------------------------------------------------------------------------------------------

def create_genesis_block():
    #creamos bloque génesis con index 0 y previous_hash "0"
    index = 0
    previous_hash = "0"
    timestamp = time.time() 
    data = "Bloque Génesis"
    
    genesis_hash = calculate_hash(index, previous_hash, timestamp, data)
    
    return Block(index, previous_hash, timestamp, data, genesis_hash)
#-------------------------------------------- prueba 2--------------------------------

#if __name__ == "__main__":
    #creamos el bloque génesis
 #   genesis_block = create_genesis_block()
    
    #imprimimos los detalles del bloque génesis
  #  print(f"Bloque Génesis - Índice: {genesis_block.index}")
   # print(f"Hash Anterior: {genesis_block.previous_hash}")
    #print(f"Timestamp: {genesis_block.timestamp}")
    #print(f"Data: {genesis_block.data}")
    #print(f"Hash: {genesis_block.hash}")
#----------------------------------------------------------------------------------------
def create_new_block(previous_block, data):
    # acá el indice del nuevo bloque k=k-1 +n; n=1
    index = previous_block.index + 1
    previous_hash = previous_block.hash
    timestamp = time.time()
    new_hash = calculate_hash(index, previous_hash, timestamp, data)
    return Block(index, previous_hash, timestamp, data, new_hash)

#---------------------------------------prueba3---------------------------------------------
#if __name__ == "__main__":
    #creamos la cadena de bloques con el bloque génesis
 #   blockchain = [create_genesis_block()]
    
    #añadimos 3 bloques más a la cadena de bloques
  #  num_of_blocks_to_add = 3
    
   # for i in range(num_of_blocks_to_add):
        #creamos un nuevo bloque usando el último bloque de la cadena
    #    new_block = create_new_block(blockchain[-1], f"Datos del bloque {i+1}")
        
        #añadimos el nuevo bloque a la cadena de bloques
     #   blockchain.append(new_block)
        
        #imprimimos los detalles del nuevo bloque
      #  print(f"Bloque {new_block.index} añadido:")
       # print(f"Hash Anterior: {new_block.previous_hash}")
        #print(f"Timestamp: {new_block.timestamp}")
        #print(f"Data: {new_block.data}")
        #print(f"Hash: {new_block.hash}")
        #print("-" * 40)
#-------------------------------------------------------------------------------------------------

#---------------------------ahora vamos a validar la cadena--------------------------------------
def is_chain_valid(blockchain):
    #verificamos
    previous_block = blockchain[0]
    index = 1
    while index<len(blockchain):
        block = blockchain[index]
        
        #verificamos hash del bloque actual
        if block.hash != calculate_hash(block.index, block.previous_hash, block.timestamp, block.data):
            return False
        
        #verificamos el hash del bloque anterior
        if block.previous_hash != previous_block.hash:
            return False
        
        previous_block = block
        index += 1
    
    return True

#-------------------------------------prueba4--------------------------------------------------
#if __name__ == "__main__":
#    blockchain = [create_genesis_block()]
    
  #  num_of_blocks_to_add = 3
    
  #  for i in range(num_of_blocks_to_add):
   #     new_block = create_new_block(blockchain[-1], f"Datos del bloque {i+1}")
    #    blockchain.append(new_block)
        
     #   print(f"Bloque {new_block.index} añadido:")
      #  print(f"Hash Anterior: {new_block.previous_hash}")
      #  print(f"Timestamp: {new_block.timestamp}")
      #  print(f"Data: {new_block.data}")
    #    print(f"Hash: {new_block.hash}")
   #     print("-" * 40)
    
    # Verificamos la validez de la cadena
  #  print("La cadena es válida:", is_chain_valid(blockchain))
#--------------------------------------------------------------------------------------------------

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return f"{self.sender} envía {self.amount} a {self.recipient}"

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash_result, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions  #lista de transacciones
        self.hash = hash_result
        self.nonce = nonce

    def __str__(self):
        transactions_str = "\n".join([str(tx) for tx in self.transactions])
        return (f"Bloque {self.index}:\nHash anterior: {self.previous_hash}\n"
                f"Timestamp: {self.timestamp}\nTransacciones:\n{transactions_str}\n"
                f"Hash: {self.hash}\nNonce: {self.nonce}\n{'-'*40}")

#-------------------------- Ejemplo5---------------------------------------------------
#if __name__ == "__main__":
#    blockchain = [create_genesis_block()]

    #creamos algunas transacciones y añadir bloques
 #   transaction_pool = [
  #      Transaction("Alice", "Bob", 10),
   #     Transaction("Bob", "Charlie", 20),
    #    Transaction("Charlie", "Dave", 30)
    #]
    
    # ++ bloques con transacciones
    #new_block = create_new_block_with_transactions_and_pow(blockchain[-1], transaction_pool, 4)
    #blockchain.append(new_block)

    #for block in blockchain:
    #    print(block)

    # verificar la cadena
   # print("¿La cadena es válida?", is_chain_valid(blockchain))

#función para calcular el hash del bloque con transacciones y nonce
def calculate_hash_with_transactions(index, previous_hash, timestamp, transactions, nonce):
    tx_str = "".join([str(tx) for tx in transactions])
    value = str(index) + previous_hash + str(timestamp) + tx_str + str(nonce)
    return hashlib.sha256(value.encode()).hexdigest()


#creamos bloque con transacciones y PoW
def create_new_block_with_transactions_and_pow(previous_block, transactions, difficulty):
    index = previous_block.index + 1
    previous_hash = previous_block.hash
    timestamp = time.time()

    nonce = 0
    hash_result = calculate_hash_with_transactions(index, previous_hash, timestamp, transactions, nonce)
     #hasta encontrar un hash válido que comience con el número de ceros determinado por "difficulty"
    while not hash_result.startswith('0' * difficulty):
        nonce += 1
        hash_result = calculate_hash_with_transactions(index, previous_hash, timestamp, transactions, nonce)

    return Block(index, previous_hash, timestamp, transactions, hash_result, nonce)

def create_genesis_block():
    genesis_transactions = [Transaction("Genesis", "Network", 0)]
    return create_new_block_with_transactions_and_pow(Block(0, "0", time.time(), genesis_transactions, "0", 0), genesis_transactions, 4)

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i - 1]

        if current_block.hash != calculate_hash_with_transactions(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.transactions, current_block.nonce):
            return False

        if current_block.previous_hash != previous_block.hash:
            return False

    return True