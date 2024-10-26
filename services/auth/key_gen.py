from Crypto.PublicKey import RSA
import base64
import hashlib

# Generate a new RSA key pair
key = RSA.generate(2048)

# Export private key (PEM)
private_key = key.export_key()

# Export public key (PEM)
public_key = key.publickey().export_key()

# Get modulus and exponent
modulus = base64.urlsafe_b64encode(key.n.to_bytes((key.size_in_bits() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=')
exponent = base64.urlsafe_b64encode(key.e.to_bytes((key.e.bit_length() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=')

# Generate a unique key ID (e.g., a hash of the public key)
key_id = hashlib.sha256(public_key).hexdigest()

print("Private Key:", private_key.decode())
print("Public Key:", public_key.decode())
print("Modulus (n):", modulus)
print("Exponent (e):", exponent)
print("Key ID (kid):", key_id)