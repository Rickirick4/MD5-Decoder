import _md5

counter = 1

password_in = raw_input("Get the MD5 Hash: ")
password_File = raw_input("Get the wordlist path: ")

try:
      password_File = open(password_File, "r")
except:
    print("\nFile not found!!")
    quit()

for password in password_File:
    pathMD5 = _md5.new(password.strip()).hexdigest()
    print("Trying password %d: %s" % (counter, password.strip()))
    counter += 1



    if password_in == pathMD5:
        print("\n[+]Password Found!! \nPassword is: %s" % password)
        break
else:
    print("\n[-]Password not found...")