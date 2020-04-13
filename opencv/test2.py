from multiprocessing.connection import Client
c = Client(('localhost', 25000), authkey=b'peekaboo')



ans = c.recv()
print(ans)