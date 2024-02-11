import os
# Create a pipe
pipe_read, pipe_write = os.pipe()
# Create a child process
pid = os.fork()
if pid == 0:
# This is the child process
    os.close(pipe_write) # Close the write end of the pipe in the child
    child_data = os.read(pipe_read, 1024)
    print(f"Child received: {child_data.decode()}")
else:
# This is the parent process
    os.close(pipe_read) # Close the read end of the pipe in the parent
    data_to_send = "Hello from Parent!"
    os.write(pipe_write, data_to_send.encode())
    os.wait() # Wait for the child process to finish

#Two pipes with two parent and children
import os
# Create two pipes
pipe1_read, pipe1_write = os.pipe()
pipe2_read, pipe2_write = os.pipe()
# Create Parent 2
pid2 = os.fork()
if pid2 == 0:
# This is Parent 2
    os.close(pipe1_read) # Close the read end of Pipe 1 in Parent 2
    os.close(pipe2_write) # Close the write end of Pipe 2 in Parent 2
    data_to_send2 = "Hello from Parent 2 to Child 11!"
    os.write(pipe1_write, data_to_send2.encode())
    os._exit(0) # Exit the child process without waiting
else:
# Create Parent 1
    pid1 = os.fork()
if pid1 == 0:
    # This is Parent 1
    os.close(pipe2_read) # Close the read end of Pipe 2 in Parent 1
    os.close(pipe1_write) # Close the write end of Pipe 1 in Parent 1
    data_to_send1 = "Hello from Parent 1 to Child 21!"
    os.write(pipe2_write, data_to_send1.encode())
    os._exit(0) # Exit the child process without waiting
else:
    # This is the main parent process
    # Wait for both child processes to finish
    os.waitpid(pid1, 0)
    os.waitpid(pid2, 0)
    message_from_child1 = os.read(pipe1_read, 1024).decode()
    message_from_child2 = os.read(pipe2_read, 1024).decode()
    # Print the messages
    print(message_from_child1)
    print(message_from_child2)

