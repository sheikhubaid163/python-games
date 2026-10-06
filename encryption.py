from cryptography.fernet import Fernet
import time

# Generate a key for encryption and decryption
def generate_key():
    return Fernet.generate_key()

# Encrypt user input data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data.encode())
    return encrypted

# Decrypt data with traps for attackers
def decrypt_data(encrypted, key, attempts):
    decoy_data = ["Decoy Data 1", "Decoy Data 2", "Decoy Data 3"]
    for attempt in range(attempts):
        try:
            cipher = Fernet(key)
            decrypted = cipher.decrypt(encrypted).decode()
            print("Decryption Successful! Data:", decrypted)
            return decrypted
        except:
            print(f"Failed Attempt {attempt + 1}. Providing Decoy Data...")
            print("Decoy Data:", decoy_data[attempt % len(decoy_data)])
            time.sleep(2)  # Artificial delay to slow attackers
    print("Too many failed attempts. System locked. Goodbye.")
    time.sleep(5)  # Delay attacker further
    return None

# Main function
def main():
    # Generate a secure key
    real_key = generate_key()
    cipher = Fernet(real_key)

    # Get user input and encrypt it
    user_input = input("Enter data to encrypt: ")
    encrypted_data = encrypt_data(user_input, real_key)
    print("Encrypted Data:", encrypted_data)

    # Test decryption (with traps for attackers)
    print("\nSimulating decryption attempts...")
    wrong_key = generate_key()  # Simulating an attacker with the wrong key
    decrypt_data(encrypted_data, wrong_key, attempts=3)  # Wrong key (fails)

    print("\nNow decrypting with the correct key...")
    decrypt_data(encrypted_data, real_key, attempts=1)  # Correct key (succeeds)

if __name__ == "__main__":
    main()
