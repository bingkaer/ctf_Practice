import hashlib

import requests

COLLISION_A = bytes.fromhex(
    "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"
)
COLLISION_B = bytes.fromhex(
    "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5b"
    "d8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70"
)

# 验证
print(COLLISION_A != COLLISION_B)  # True
print(hashlib.md5(COLLISION_A).hexdigest())  # 79054025255fb1a26e4bc422aef54eb4
print(hashlib.md5(COLLISION_B).hexdigest())  # 79054025255fb1a26e4bc422aef54eb4

# 组装并发送


resp = requests.post(
    "http://f4ccc12c6659e8fba25a5f1d.http-ctf2.dasctf.com/levell14.php",
    data={"param1": COLLISION_A, "param2": COLLISION_B},
)
print(resp.text)
