import socket

TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", 0))          # ローカル適当ポートで受ける
sock.settimeout(2.0)

def send(cmd: str):
    sock.sendto(cmd.encode("ascii"), (TELLO_IP, TELLO_PORT))
    try:
        data, addr = sock.recvfrom(1024)
        print(cmd, "=>", data.decode("ascii", errors="replace").strip(), "<-", addr)
    except socket.timeout:
        print(cmd, "=>", "NO RESPONSE")

send("command")
send("battery?")
# ap <モバイルホットスポットのSSID> <モバイルホットスポットのパスワード>
send("ap pi raspberry")

# send("ap YourSSID YourPassword")
sock.close()
