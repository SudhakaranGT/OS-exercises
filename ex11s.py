import time
import multiprocessing.shared_memory as shared_memory

# Server code

shm_server = shared_memory.SharedMemory(create=True, size=100, name='sm2')
buffer = shm_server.buf

try:
    while True:
        # Display the data from shared memory
        server_data = bytes(buffer[:100]).decode('utf-8')
        print("Server data in memory:", server_data)

        # Check if the data in shared memory equals "exit" and terminate if true
        if buffer[:4] == b'exit':
            shm_server.close()
            shm_server.unlink()
            break

        message1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        buffer[:100] = b'\x00' * 100
        message_bytes1 = message1.encode('utf-8')
        buffer[:len(message_bytes1)] = message_bytes1

        time.sleep(5)
finally:
    # Clean up
    shm_server.close()
    shm_server.unlink()


