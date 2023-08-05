import hashlib
import hmac
from typing import Any, Dict, Optional

from cryptography.hazmat.primitives.ciphers.aead import AESCCM

from ..cose_key import COSEKey
from ..exceptions import DecodeError, EncodeError, VerifyError


class SymmetricKey(COSEKey):
    """"""

    def __init__(self, cose_key: Dict[int, Any]):
        """"""
        super().__init__(cose_key)

        self._key: bytes = b""

        # Validate kty.
        if cose_key[1] != 4:
            raise ValueError("kty(1) should be Symmetric(4).")

        # Validate k.
        if -1 not in cose_key:
            raise ValueError("k(-1) not found.")
        if -1 in cose_key and not isinstance(cose_key[-1], bytes):
            raise ValueError("k(-1) should be bytes(bstr).")
        self._key = cose_key[-1]

        if 3 not in cose_key:
            raise ValueError("alg(3) not found.")
        self._alg = cose_key[3]


class HMACKey(SymmetricKey):
    """"""

    def __init__(self, cose_key: Dict[int, Any]):
        """"""
        super().__init__(cose_key)

        self._hash_alg = None
        self._trunc = 0

        # Validate alg.
        if self._alg == 4:  # HMAC 256/64
            self._hash_alg = hashlib.sha256
            self._trunc = 8
        elif self._alg == 5:  # HMAC 256/256
            self._hash_alg = hashlib.sha256
            self._trunc = 32
        elif self._alg == 6:  # HMAC 384/384
            self._hash_alg = hashlib.sha384
            self._trunc = 48
        elif self._alg == 7:  # HMAC 512/512
            self._hash_alg = hashlib.sha512
            self._trunc = 64
        else:
            raise ValueError(f"Unsupported or unknown alg({self._alg}) for HMAC.")

    def sign(self, msg: bytes) -> bytes:
        """"""
        try:
            return hmac.new(self._key, msg, self._hash_alg).digest()[0 : self._trunc]
        except Exception as err:
            raise EncodeError("Failed to sign.") from err

    def verify(self, msg: bytes, sig: bytes):
        """"""
        if hmac.compare_digest(sig, self.sign(msg)):
            return
        raise VerifyError("Failed to compare digest.")


class AESCCMKey(SymmetricKey):
    """"""

    def __init__(self, cose_key: Dict[int, Any]):
        """"""
        super().__init__(cose_key)

        self._cipher: AESCCM
        self._nonce_len = 0

        # Validate alg.
        if self._alg == 10:  # AES-CCM-16-64-128
            if len(self._key) != 16:
                raise ValueError(
                    "The length of AES-CCM-16-64-128 key should be 16 bytes."
                )
            self._cipher = AESCCM(self._key, tag_length=8)
            self._nonce_len = 13
        elif self._alg == 11:  # AES-CCM-16-64-256
            if len(self._key) != 32:
                raise ValueError(
                    "The length of AES-CCM-16-64-256 key should be 32 bytes."
                )
            self._cipher = AESCCM(self._key, tag_length=8)
            self._nonce_len = 13
        elif self._alg == 12:  # AES-CCM-64-64-128
            if len(self._key) != 16:
                raise ValueError(
                    "The length of AES-CCM-64-64-128 key should be 16 bytes."
                )
            self._cipher = AESCCM(self._key, tag_length=8)
            self._nonce_len = 7
        elif self._alg == 13:  # AES-CCM-64-64-256
            if len(self._key) != 32:
                raise ValueError(
                    "The length of AES-CCM-64-64-256 key should be 32 bytes."
                )
            self._cipher = AESCCM(self._key, tag_length=8)
            self._nonce_len = 7
        elif self._alg == 30:  # AES-CCM-16-128-128
            if len(self._key) != 16:
                raise ValueError(
                    "The length of AES-CCM-16-128-128 key should be 16 bytes."
                )
            self._cipher = AESCCM(self._key)
            self._nonce_len = 13
        elif self._alg == 31:  # AES-CCM-16-128-256
            if len(self._key) != 32:
                raise ValueError(
                    "The length of AES-CCM-16-128-256 key should be 32 bytes."
                )
            self._cipher = AESCCM(self._key)
            self._nonce_len = 13
        elif self._alg == 32:  # AES-CCM-64-128-128
            if len(self._key) != 16:
                raise ValueError(
                    "The length of AES-CCM-64-128-128 key should be 16 bytes."
                )
            self._cipher = AESCCM(self._key)
            self._nonce_len = 7
        elif self._alg == 33:  # AES-CCM-64-128-256
            if len(self._key) != 32:
                raise ValueError(
                    "The length of AES-CCM-64-128-256 key should be 32 bytes."
                )
            self._cipher = AESCCM(self._key)
            self._nonce_len = 7
        else:
            raise ValueError(f"Unsupported or unknown alg({self._alg}) for AES CCM.")

    def encrypt(self, msg: bytes, nonce: bytes, aad: Optional[bytes] = None) -> bytes:
        """"""
        if len(nonce) != self._nonce_len:
            raise ValueError(
                "The length of nonce should be %d bytes." % self._nonce_len
            )
        try:
            return self._cipher.encrypt(nonce, msg, aad)
        except Exception as err:
            raise EncodeError("Failed to encrypt.") from err

    def decrypt(self, msg: bytes, nonce: bytes, aad: Optional[bytes] = None) -> bytes:
        """"""
        if len(nonce) != self._nonce_len:
            raise ValueError(
                "The length of nonce should be %d bytes." % self._nonce_len
            )
        try:
            return self._cipher.decrypt(nonce, msg, aad)
        except Exception as err:
            raise DecodeError("Failed to decrypt.") from err
