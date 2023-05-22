# hashlib
 This is a project that revolves around the hashlib library in python. 
 The goal is to hash any file input 
 This means that we will generate a String/byte sequence that will allow us to identify a file.
 
 
(SOME APPLICATIONS OF HASHING A FILE)
  - *Duplicate file detetection*: hashes can be used to identify duplicates and remove them. We generate the hashes of the files, compare them and if theyre identical we eliminate one of them. This ensure memory optimization and management. 
  
  - *Password storage*: To store passwords in a file, it is important to protect them from unauthorized access. INstead of storing the actual values of the passwords, we can store their hash values. 
 
  - *Data Integrity verification*: We can use hashing to verify the integrity of files, and check if they have been corrupted or altered during their transmission or storage. By generating a hash value, we can compare this value with the received hash value to check for any changes.

--> Hash functions provide a fast and efficient way to verify FILE INTEGRITY, DETECT DUPLICATES, ENSURE SECURITY(PERFORM OTHER TASKS RELATED TO FILE MANAGEMEMENT AND ANALYSIS)

# REAL LIFE EXAMPLE OF HASHING:
Anti-virus software compares hashes of malware with hashes of software components within a computer system in order to detect malware.
Malware hashes are used by virus protection software to check for viruses.


--------------                                       ---------------------------------                              
|    Input   |     ---> Cryptographic hash function  | the digest: malware hash value |
|   Malware  |                                       ---------------------------------
--------------

# What does this mean? to hash a file
When we have an arbitrary sized file that is read by a function to allow us to generate a fixed-length value from it
hash functions return an integer value.
hash functions can only work on immutable objects 
     - immutable objects: String, Tuple, Frozen set, User defined objects(depending on their impoementation)
     - mutable objects: lists, dictionaries, sets, User defined objects(depending on their impoementation)
    
Hashing a file will help us return a certain type of 'id' which can help us do particular tasks     
Strong hashes with large amounts of bytes can help us distinguish between many different files.

