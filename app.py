import sys
from client import Client


cli = Client()

if len(sys.argv) == 2 and sys.argv[1] == 'findAll':
    cli.findAll()
elif len(sys.argv) == 3:
    id = sys.argv[2]
    if sys.argv[1] == 'find':
        cli.find(id)
    elif sys.argv[1] == 'delete':
        cli.delete(id)
elif len(sys.argv) == 5:
    id = sys.argv[2]
    name = sys.argv[3]
    major = sys.argv[4]
    cli.insert(id, name, major)
else:
    print('No está enviando los parametros adecuados')
