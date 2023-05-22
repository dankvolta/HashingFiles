import hashlib 

# h1 = hashlib.sha224(b"C")

# print(h1)
# print(hashlib.algorithms_available)

# print(hashlib.algorithms_guaranteed)

# h = hashlib.new("SHA256")       # we specify the algorithm to be used using the method hashlib.new("name_of_algorithm")

# h.update(b"Hello World!")       # update("message_to_hash") : this method hashes the input argument (we write 'b' before the message because 
#                                 # we have to pass the imput argument in its byte form)

# print('the hash value is: ' + str(h.digest()), "\n")               # .digest() helps to display the result of the previously hashed input
# print('the hex representation of the digest message of Hello World! is: ' + str(h.hexdigest()))            # .hexdigest() gives us the same hash but under a hexadecimal representation 


myPassword = "thisismypasswrd"

fakePassword = "helloworld"

# we choose a hashing algorithm 

p = hashlib.new("SHA256")
p.update(myPassword.encode())   # if we are passing a string variable name, we can encode it using the encode() method rather than
                                    # using b token. 'b' token is useful when the value we pass is a string in itself
correct_password_hash = p.hexdigest()

p1 = hashlib.new("SHA256")
p1.update(fakePassword.encode())

fake_password_hash = p1.hexdigest()



if correct_password_hash == fake_password_hash:
    print("access granted")
else:
    print("access denied")




