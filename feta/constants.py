import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey, EllipticCurvePrivateKey


def load_private_key(path, password) -> EllipticCurvePrivateKey:
    with open(path, "rb") as file:
        return serialization.load_pem_private_key(file.read(), password, backend=default_backend())


def load_public_key(path) -> EllipticCurvePublicKey:
    with open(path, "rb") as file:
        return serialization.load_ssh_public_key(file.read(), backend=default_backend())


WORKING_DIR = os.environ["WORKING_DIR"]
ENCODING = "UTF-8"
JWT_ALGORITHM = "HS256"
TOKEN_LIFETIME_SECONDS = 0.5 * 60
KEYPAIR_LIFETIME_SECONDS = 1 * 60
REGISTRY_URL = os.environ["REGISTRY_URL"]
PRIVATE_KEY = load_private_key(os.environ["PRIVATE_KEY_FILE_PATH"], os.environ.get("PRIVATE_KEY_PASSWORD"))
PUBLIC_KEY = load_public_key(os.environ["PUBLIC_KEY_FILE_PATH"])
