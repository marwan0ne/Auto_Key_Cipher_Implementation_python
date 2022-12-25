# Auto_Key_Cipher_Implementation_python
The Autokey Cipher is one such example. In general, the term autokey refers to any cipher where the key is based on the original plaintext. In its simplest form, it was first described by Girolamo Cardano, and consisted of using the plaintext itself as the keystream. However, since there was no key involved in this system, it suffered the same major flaw as the Atbash and the Trithemius Ciphers: if you knew it had been used, it was trivial to decode.
The most famous version of the Autokey Cipher, however, was described by Blaise de Vigenère in 1586 (the one that was later misattributed the Vigenère Cipher). This cipher incorporates a keyword in the creation of the keystream, as well as the original plaintext.
**Encryption**:

Encryption using the Autokey Cipher is very similar to the Vigenère Cipher, except in the creation of the keystream.
The keystream is made by starting with the keyword or keyphrase, and then appending to the end of this the plaintext itself.
We then use a Tabula Recta to find the keystream letter across the top, and the plaintext letter down the left, and use the crossover letter as the ciphertext letter.
As an example we shall encode the plaintext "meet me at the corner" using the keyword king. First we must generate the keystream, which starts with the keyword, and then continues with the plaintext itself, getting kingmeetme.


**Decryption**:

To decrypt a ciphertext using the Autokey Cipher, we start just as we did for the Vigenère Cipher, and find the first letter of the key across the top, find the ciphertext letter down that column, and take the plaintext letter at the far left of this row. As well as being the plaintext letter, we now need to add this letter to the end of the keystream as we shall need it later. Continuing to decode each letter, we add them to the end of the keystream each time.
We shall decrypt the ciphertext "QNXEPKMAEGKLAAELDTPDLHN" which has been encrypted using the keyword queen. We start with the information shown in the table below.
