import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    #       Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)

    # connect your socket to the server here.
    sock.connect(server_address)

    #       you can use this variable to accumulate the entire message received back
    #       from the server
    received_message = []

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # send your message to the server here.
        sock.sendall(bytes(msg, 'utf8'))

        amount_received = 0
        amount_expected = len(msg)

        #       the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        while amount_received < amount_expected:
            #       Log each chunk you receive.  Use the print statement below to
            #       do it. This will help in debugging problems
            chunk = sock.recv(16)
            amount_received += len(chunk)
            received_message.append(chunk.decode())
            print('received "{0}"'.format(chunk.decode()), file=log_buffer)

    except Exception as e:
        traceback.print_exc(e)
        sys.exit(1)
    finally:
        #       after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        sock.close()
        print('closing socket', file=log_buffer)
        return ''.join(received_message)


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     usage = '\nusage: python echo_client.py "this is my message"\n'
    #     print(usage, file=sys.stderr)
    #     sys.exit(1)

    # msg = sys.argv[1]
    msg = 'hello this is a random string for my program to process'
    client(msg)
