import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # instantiate a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # bind your new sock 'sock' to the address above and begin to listen
    # for incoming connections
    sock.bind(address)
    sock.listen(5)
    try:

        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            #       make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            conn, addr = sock.accept()
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    #       receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    data = conn.recv(16)
                    data_string = data.decode()
                    print('received "{0}"'.format(data_string), file=log_buffer)

                    # Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.
                    conn.sendall(data)
                    print('sent "{0}"'.format(data_string), file=log_buffer)

                    # Check here to see whether you have received the end
                    # of the message. If you have, then break from the `while True`
                    # loop.
                    if len(data_string) < 16:
                        print('End of message', file=log_buffer)
                        break

            except Exception as e:
                traceback.print_exc(e)
                sys.exit(1)
            finally:
                #       When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.
                conn.close()
                print('echo complete, client connection closed', file=log_buffer)
                break

    except KeyboardInterrupt:
        #       Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
