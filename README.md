# RC4-Python
A simple encrypt/decrypt Python script using RC4

This is a simple implementation of RC4 cipher referring to Wikipedia: http://en.wikipedia.org/wiki/RC4 .

The keys and plaintext are UTF-8(Linux)/GBK(Windows), the keystream and ciphertext are in hexadecimal.

    Usage: $ ./RC4.py filename encrypt/decrypt [keyfile]  
      e.g. $ ./RC4.py plain.txt encrypt key.txt  
           $ ./RC4.py hex.txt decrypt key.txt  

              plain.txt : plaintext   
              hex.txt : ciphertext  
              key.txt : keys  
              keystream.txt : keystream 
