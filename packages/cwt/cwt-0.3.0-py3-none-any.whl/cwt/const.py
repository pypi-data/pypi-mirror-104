# Registered CWT Claims
CWT_CLAIM_NAMES = {
    "hcert": -260,  # map
    "EUPHNonce": -259,  # bstr
    "EATMAROEPrefix": -258,  # bstr
    "EAT-FDO": -257,  # array
    "iss": 1,  # text string
    "sub": 2,  # text string
    "aud": 3,  # text string
    "exp": 4,  # integer or floating-point number
    "nbf": 5,  # integer or floating-point number
    "iat": 6,  # integer or floating-point number
    "cti": 7,  # byte string
    "cnf": 8,  # map
}

# COSE key types
COSE_KEY_TYPES = {
    "OKP": 1,  # OCtet Key Pair
    "EC2": 2,  # Elliptic Curve Keys w/ x- and y-coordinate pair
    "RSA": 3,  # RSA Key
    "Symmetric": 4,  # Symmetric Keys
    "HSS-LMS": 5,  # Public key for HSS/LMS hash-based digital signature
    "WalnutDSA": 6,  # WalnutDSA public key
}

# COSE Algorithms for Content Encryption Key (CEK).
COSE_ALGORITHMS_CEK = {
    "A128GCM": 1,  # AES-GCM mode w/ 128-bit key, 128-bit tag
    "A192GCM": 2,  # AES-GCM mode w/ 192-bit key, 128-bit tag
    "A256GCM": 3,  # AES-GCM mode w/ 256-bit key, 128-bit tag
    "AES-CCM-16-64-128": 10,  # AES-CCM mode 128-bit key, 64-bit tag, 13-byte nonce
    "AES-CCM-16-64-256": 11,  # AES-CCM mode 256-bit key, 64-bit tag, 13-byte nonce
    "AES-CCM-64-64-128": 12,  # AES-CCM mode 128-bit key, 64-bit tag, 7-byte nonce
    "AES-CCM-64-64-256": 13,  # AES-CCM mode 256-bit key, 64-bit tag, 7-byte nonce
    "AES-CCM-16-128-128": 30,  # AES-CCM mode 128-bit key, 128-bit tag, 13-byte nonce
    "AES-CCM-16-128-256": 31,  # AES-CCM mode 256-bit key, 128-bit tag, 13-byte nonce
    "AES-CCM-64-128-128": 32,  # AES-CCM mode 128-bit key, 128-bit tag, 7-byte nonce
    "AES-CCM-64-128-256": 33,  # AES-CCM mode 256-bit key, 128-bit tag, 7-byte nonce
    # etc.
}

# COSE Algorithms for MAC.
COSE_ALGORITHMS_MAC = {
    "HMAC 256/64": 4,  # HMAC w/ SHA-256 truncated to 64 bits
    "HMAC 256/256": 5,  # HMAC w/ SHA-256
    "HMAC 384/384": 6,  # HMAC w/ SHA-384
    "HMAC 512/512": 7,  # HMAC w/ SHA-512
    "AES-MAC128/64": 14,  # AES-MAC 128-bit key, 64-bit tag
    "AES-MAC256/64": 15,  # AES-MAC 256-bit key, 64-bit tag
    "AES-MAC128/128": 25,  # AES-MAC 128-bit key, 128-bit tag
    "AES-MAC256/128": 26,  # AES-MAC 256-bit key, 128-bit tag
    # etc.
}

# COSE Algorithms for Symmetric Keys.
COSE_ALGORITHMS_SYMMETRIC = dict(COSE_ALGORITHMS_MAC, **COSE_ALGORITHMS_CEK)
