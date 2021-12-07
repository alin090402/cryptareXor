# Team
Sava Constantin-Alin, 151

Balauta Amargheoalei Albert Ionut, 152

# Commands

For encryption:
```
python3 crypt.py password decryptedFile output
```

For decryption:
```
python3 decrypt.py ecryptedFile password output
```

# Opponent

**Team name:** Spaghetti Code

**Project link:** https://github.com/Alexu33/proiect-1-ASC

**Password:** AsJY74sL93fgsd

# Code Explanation

We start from the idea that the character **' '** (space) is the most used character in a Romanian text.
We don't know the length of the password so we try every possibility between 10 and 15.
For a **k** length we separate the bytes from the encrypted file into **k** substrings:
```
0, k, 2k .......................
1, k + 1, 2k + 1................
................................
k-1, k + (k-1), 2k + (k - 1)....
```
**For each substring:**
We use a dictionary to find the frequency of every byte from the encrypted file. 
The byte with the greatest frequency corresponds to the character **' '** (space) from the original text.
If we xor that byte with the ascii code of **' '** (32) we'll find a character from the password
