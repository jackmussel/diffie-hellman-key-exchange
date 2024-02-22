**Diffie Hellman Key Exchange Program**
<br/>
<br/>
**Overview**
<br/>
This Python program implements a key exchange algorithm based on the Diffie-Hellman-Merkle key exchange protocol. The key exchange process allows two parties to securely agree upon a shared secret key over an insecure communication channel.

**Features**
<br/>
- Fast Modular Exponentiation Algorithm: The program includes a fast modular exponentiation function (fast_mod_exp) to efficiently calculate modular exponentiation.
- Miller-Rabin Primality Test: The Miller-Rabin primality test is employed to generate random prime numbers, ensuring the security of the key exchange.
- Prime Number Generation: The get_prime function generates a random prime number using the Miller-Rabin test.
- Primitive Root Generator: The get_generator function finds a primitive root generator for a given prime number.
- Key Exchange Algorithm: The main function (main) executes the key exchange algorithm, generating public and private keys for both parties and verifying the shared secret key.

**Usage**
<br/>
1. Run the program to initiate the key exchange.
2. The program will output the generated prime number, generator, each party's secret key, public key, and if the shared keys match.

**Dependencies**
<br/>
The program requires the Python programming language to be installed on the system.

**Important Note**
<br/>
This implementation serves educational purposes and should not be used in a production environment without thorough review and consideration of security best practices.
Feel free to modify and adapt this code for your specific needs. If you have any questions or suggestions, please don't hesitate to reach out.

Author: Jack Musselwhite

Date: 11/14/23

**License**
<br/>
<br/>
MIT License
<br/>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
