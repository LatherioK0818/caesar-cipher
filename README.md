# Lab: Cryptography

## Project: Caesar Cipher

### Overview

In this lab, we delve into the world of cryptography by tackling a classic - the Caesar Cipher. Our goal is to develop a method to both encrypt and decrypt messages using this ancient technique. But the challenge doesn't end there - we'll also create a way to decipher encrypted messages without the key!

### Feature Tasks and Requirements

#### 1. Encryption Function

- **Functionality:** Create an `encrypt` function to shift a plain text phrase by a numeric value.
- **Behavior:**
  - A shift in the phrase by the specified number of letters. 
  - For shifts exceeding 26, the function will wrap around.
  - Out of range letter shifts will also wrap around.

  **Examples:**
  - `encrypt('abc', 1)` should return `'bcd'`.
  - `encrypt('abc', 10)` should return `'klm'`.
  - `encrypt('abc', 27)` should return `'bcd'`.
  - `encrypt('zzz', 1)` should return `'aaa'`.

#### 2. Decryption Function

- **Purpose:** Create a `decrypt` function to reverse the encryption process using the numeric shift.
- **Requirement:** The function should restore the encrypted text to its original form when the correct key is provided.

#### 3. Crack Function

- **Objective:** Develop a `crack` function to decode the cipher without the encryption key.
- **Challenge:** The computer must determine if the code was broken with minimal human guidance.
- **Implementation Note:** Utilize a corpus of English words for this task.

#### User Acceptance Tests

The application must be capable of:

- Encrypting a string with a given shift.
- Decrypting a previously encrypted string with the same shift.
- Handling both upper and lower case letters in encryption.
- Allowing non-alpha characters in encryption but ignoring them, including whitespace.
- Decrypting the phrase "It was the best of times, it was the worst of times." without knowing the shift used.

#### Stretch Goals

- Research the Vigenère cipher.
- Find and decode ROT13 encrypted punchlines, spoilers, etc.
- Break the code for a message written in a language other than English.

### Configuration

- **Project Name:** `caesar-cipher`
- **Repository:** Use the project folder as the root of your project's git repository.
- **Submission Instructions:** Refer to Lab Submission Instructions for detailed guidelines.

#### Collaborators

Ekow Yawson
Stephanie G Johnson
Latherio Kidd
