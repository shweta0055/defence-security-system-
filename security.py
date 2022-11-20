import mysql.connector as ms
import time
import speech_recognition as sr
import pyttsx3
import stdiomask
time.sleep(3)
print("\n") 
print("\t\t\t\t\t\t============================================================")
print("\t\t\t\t\t\t==--------------------------------------------------------==")
print("\t\t\t\t\t\t==--------|  DEFENSE SECURITY MANAGEMENT SYSTEM  |--------==")
print("\t\t\t\t\t\t==--------------------------------------------------------==")
print("\t\t\t\t\t\t============================================================\n\n")
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Welcome to the world of DEFENSE SECURITY MANAGEMENT ")
engine.say("I AM Sylvie , YOUR assistant")
engine.runAndWait()
mydb = ms.connect(host="localhost", user="root", password="aqwerta_1580")
mc = mydb.cursor()
mc.execute("CREATE DATABASE IF NOT EXISTS DEFENSE")


#Function to display the details about the evidences collected and about the people working under them.
def dispevidence():
    engine.say("enter the access id")
    engine.runAndWait()
    aa = input("ENTER THE ACCESS ID : ")
    if aa == '25806':
        print("\n===ACCESS GRANTED===\n")
        engine.say("access granted")
        engine.runAndWait()
        time.sleep(2)
        print("CONNECTING...\n")
        engine.say("connecting")
        engine.runAndWait()
        time.sleep(2)
        mc.execute("use defense")
        mc.execute("DROP TABLE IF EXISTS EVIDENCE")
        mc.execute("CREATE TABLE EVIDENCE (CASE_CODE INT(3) PRIMARY KEY , CASE_FILE VARCHAR(50),EVIDENCES_COLLECTED VARCHAR(250),SUBORDINATES VARCHAR(25))")
        mc.execute("INSERT INTO EVIDENCE VALUES(444,'LOKESH MURDER','FINGERPRINT','MARY JOSEPH')")
        mc.execute("INSERT INTO EVIDENCE VALUES(566,'GOLD SMUGGLING','2KG OF GOLD','LAKSHMI DHRU')")
        mc.execute("INSERT INTO EVIDENCE VALUES(377,'ONLINE FRAUD',' WHATSAPP CHATS','GRUNGE DILOP')")
        mc.execute("INSERT INTO EVIDENCE VALUES(882,'THEFT FROM SBI BANK','CCTV VISUALS','STEOHEN JAKE')")
        mc.execute("INSERT INTO EVIDENCE VALUES(554,'PICKPOCKET','EYE WITNESS','PHILIP LAHM')")
        mc.execute("SELECT * FROM EVIDENCE")
        print("CASECODE", '%18s' % "CASE", '%35s' % "EVIDENCES COLLECTED", '%26s' % "SUBORDINATES")
        print("-" * 90)
        for i in mc:
            print(i[0], '%25s' % i[1], '%28s'% i[2], '%30s' % i[3])
        time.sleep(4)
    
    else:
        print("|| ACCESS DENIED ||")
        engine.say("access denied")
        engine.runAndWait()
        time.sleep(4)
    return

    

# Spies employed by govt, their personal details. Only accessible by higher officials.
def undercoverspies():
    print("\n===| DETAILS ABOUT THE UNDERCOVER SPIES |===")
    engine.say("enter access id")
    engine.runAndWait()
    b = input("ENTER ACCESS ID : ")
    if b == '25806':
        print("\n===| ACCESS GRANTED |===")
        engine.say("access granted")
        engine.runAndWait()
        time.sleep(2)
        print('GATHERING INFORMATION...\n')
        engine.say("gathering information")
        engine.runAndWait()
        time.sleep(2)
        mc.execute("use defense")
        mc.execute("DROP TABLE IF EXISTS SPIES")
        mc.execute(
            "CREATE TABLE SPIES (CODE int PRIMARY KEY, NAME VARCHAR(20),AGE INT(3) ,STATUS CHAR(10), CURRENT_LOCATION VARCHAR(20),MISSION VARCHAR(250) )")
        mc.execute("INSERT INTO SPIES VALUES(051,'DAVID GEORGE',34,'ACTIVE','LONDON','SWIFT')")
        mc.execute("INSERT INTO SPIES VALUES(052,'CHARLES GREGORY',41,'ACTIVE','GERMANY','ECLAIRS')")
        mc.execute("INSERT INTO SPIES VALUES(053,'SELENA THOMAS',27,'ACTIVE','ENGLAND','TRIDENT')")
        mc.execute("INSERT INTO SPIES VALUES(054,'KEVIN JAMES',31,'ACTIVE','SCOTLAND','IRIS')")
        mc.execute("INSERT INTO SPIES VALUES(055,'ALEXANDER PAUL',38,'ACTIVE','FRANCE','PHOENIX')")
        mc.execute("SELECT * FROM SPIES")
        print("CODE", '%15s' % 'NAME', '%20s' % "AGE", '%20s' % "STATUS", '%20s' % "CURRENT LOCATION",
              '%20s' % "MISSION")
        for i in mc:
            print(i[0], '%21s' % i[1], '%15s' % i[2], '%21s' % i[3], '%15s' % i[4], '%24s' % i[5])
        time.sleep(3)
    else:
        print(" || ACCESS DENIED ||")
        engine.say("access denied")
        engine.runAndWait()
        time.sleep(3)
    return


# alert the agents about the situation
def alertagent():
    engine.say("enter the access id")
    engine.runAndWait()
    b = input("ENTER ACCESS ID : ")
    if b == '25806':
        print("\n===| ACCESS GRANTED |===")
        engine.say("access granted")
        engine.runAndWait()
        time.sleep(2)
        print('''SEND MESSAGE VIA :
             1.MESSAGE
             2.MAIL''')
        engine.say("Would you like to alert the agents via mail or message ?")
        engine.runAndWait()
        x = int(input("ENTER YOUR CHOICE :"))
        if x == 1:
            print("\n==| MESSAGE |==\n")
            engine.say("MESSAGE")
            engine.say("please type the message")
            engine.runAndWait()
            m = input("Type the message : ")
            engine.say("enter the agent ID")
            engine.runAndWait()
            n = int(input("\nEnter the Officer ID : "))
            engine.say("Confirm the message and send the message ?")
            engine.runAndWait()
            mm = input("\nSEND MESSAGE (YES/N0) : ")
            mm=mm.upper()
            if mm == 'YES':
                engine.say("encrypting the message")
                engine.runAndWait()
                print("ENCRYPTING THE MESSAGE .....")
                time.sleep(3)
                engine.say("the message is being sent through the servers in THE UNITED KINGDOM")
                print("SENDING  MESSAGE...")
                time.sleep(2)
                print('-' * 25)
                engine.say("the message has been sent successsfully")
                engine.runAndWait()
                print("MESSAGE SENT SUCCESSFULLY")

            if mm == 'N0':
                engine.say("Are you sure you want to delete this message ?")
                md = input("\nDO YOU WANT TO DISCARD THE MESSAGE(YES/NO) : ")
                md.upper()
                if md == 'YES':
                    engine.say("the message has been discarded")
                    print("==| MESSAGE DISCARDED |==")
                if md == 'NO':
                    mg = m
                    print(m)
                    engine.say("send the message?")
                    engine.runAndWait()
                    mm = input("SEND MESSAGE(YES/NO) : ")
                    if mm == 'YES':
                        engine.say("encrypting the message")
                        engine.runAndWait()
                        print("ENCRYPTING THE MESSAGE ....")
                        time.sleep(3)
                        engine.say("sending the message through the servers in Europe")
                        engine.runAndWait()
                        print("SENDING MESSAGE...")

                        time.sleep(2)
                        engine.say("the message has been sent successfully")
                        engine.runAndWait()
                        print("==| MESSAGE SENT SUCCESSFULLY |==")

        if x == 2:
            print("\n== MAIL ==\n")
            engine.say("mail")
            engine.say("enter the message to be sent")
            engine.runAndWait()
            m = input("Type the message : ")
            engine.say("enter the mail id")
            engine.runAndWait()
            input("Enter the Officer MAIL ID : ")
            engine.say("send the mail ?")
            engine.runAndWait()
            mf = input("SEND MAIL (YES/NO) : ")
            me = mf.upper()

            if me == 'YES':
                engine.say("encrypting the mail")
                engine.runAndWait()
                print("ENCRYPTING THE MAIL .....")
                time.sleep(3)
                engine.say("sending the mail through the servers in India")
                engine.runAndWait()
                print("SENDING MAIL...")
                engine.say("THE MAIL HAS BEEN SENT SUCCESSFULLY")
                engine.runAndWait()
                time.sleep(2)
                print("MAIL SENT SUCCESSFULLY")

            elif me == 'NO':
                engine.say("do you want to discard the mail ?")
                engine.runAndWait()
                md = input("DO YOU WANT TO DISCARD THE MAIL (YES/NO) : ")
                md.upper()
                if md == 'YES':
                    engine.say("the mail has been discarded")
                    engine.runAndWait()
                    print("MAIL DISCARDED")
                if md == 'NO':
                    ms = m
                    print(ms)
                    engine.say("do you want to send the mail ?")
                    engine.runAndWait()
                    me = input("SEND MAIL(YES/NO) : ")
                    if me == 'YES':
                        engine.say("encrypting the mail")
                        engine.runAndWait()
                        print("ENCRYPTING THE MAIL ....")
                        time.sleep(3)
                        engine.say("sending the mail through the servers of Africa")
                        engine.runAndWait()
                        print("SENDING MAIL...")
                        time.sleep(2)
                        engine.say("the mail has been sent successfully")
                        engine.runAndWait()
                        print("MAIL SENT SUCCESSFULLY")

    else:
        print(" || ACCESS DENIED ||")
        engine.say("access denied")
        engine.runAndWait()
    return


# POSITIONS OF THE AGENTS TO DIRECT THE CLOSEST ONE TO THE DESTINATION
def agentlocate():
    mc.execute("use defense")
    mc.execute("DROP TABLE IF EXISTS ACCESS")
    mc.execute("create table ACCESS (CODE int primary key  , NAME VARCHAR(20), AGE INT(5) , STATUS VARCHAR(10),CURRENT_LOCATION VARCHAR(250), MISSION VARCHAR(250) )")
    mc.execute("INSERT INTO ACCESS VALUES (001,'Mary Joseph',28,'ACTIVE','JAPAN','OVERLORD')")
    mc.execute("INSERT INTO ACCESS VALUES (002,'Steohen Jake',43,'ACTIVE','SWEDEN','THUNDER')")
    mc.execute("INSERT INTO ACCESS VALUES (003,'Lakshmi Dhru',24,'ACTIVE','RUSSIA','DYNAMO')")
    mc.execute("INSERT INTO ACCESS VALUES(004,'Grunge Dilop',36,'ACTIVE','SPAIN','BROSSA')")
    engine.say("enter the access id")
    engine.runAndWait()
    b = input("ENTER ACCESS ID :")
    if b == '25806':
        engine.say("access granted")
        engine.runAndWait()
        print("\n===ACCESS GRANTED===")
        engine.say("enter the location to direct the agents ")
        engine.runAndWait()
        l = input("Enter the location to be directed to :")
        l = l.upper()
        if l == 'JAPAN':
            engine.say("locating the agents")
            engine.runAndWait()
            print("LOCATING AGENTS ...")
            time.sleep(2)
            engine.say("accessing the information .")
            print("ACCESSING INFO ...")
            time.sleep(2)
            print("\n==| AGENTS |==")
            mc.execute("use defense")
            mc.execute("select * from access where code='001'")
            engine.say("send the message to MARY JOSEPH 001 ?")
            engine.runAndWait()
            m = input("SEND MESSAGE TO MARY JOSEPH(YES/NO) : ")
            m = m.upper()
            if m == 'YES':
                engine.say("enter the message")
                engine.runAndWait()
                mm = input("TYPE MESSAGE : ")
                engine.say("sending the message through the servers in UAE")
                engine.runAndWait()
                print("\nSENDING MESSAGE ...")
                time.sleep(2)
                engine.say("The message has been sent successfully")
                print("MESSAGE SENT SUCCESSFULLY")
            if m == 'NO':
                engine.say("message has been discarded")
                engine.runAndWait()
            return

        elif l == 'SWEDEN':
            engine.say("locating the agents")
            engine.runAndWait()
            print("LOCATING AGENTS...")
            time.sleep(2)
            engine.say("accessing the information")
            engine.runAndWait()
            print("ACCESSING INFO...")
            time.sleep(2)
            print("\n==| AGENTS |==")
            mc.execute("select * from access where code='002'")
            engine.say("send the message to steohen jake 002 ?")
            engine.runAndWait()
            m = input("SEND MESSAGE TO STEOHEN JAKE (YES/NO) : ")
            m = m.upper()
            if m == 'YES':
                engine.say("enter the message ")
                engine.runAndWait()
                mm = input("\nTYPE MESSAGE :")
                engine.say("Sending the message through the servers in australia")
                engine.runAndWait()
                print("SENDING MESSAGE...")
                time.sleep(2)
                engine.say("The message has been sent successfully")
                engine.runAndWait()
                print("MESSAGE SENT SUCCESSFULLY")
            if m == 'NO':
                engine.say("The message has been discarded")
                engine.runAndWait()
            return

        elif l == 'RUSSIA':
            engine.say("locating the agents")
            engine.runAndWait()
            print("LOCATING AGENTS...")
            time.sleep(2)
            engine.say("Accessing the information")
            engine.runAndWait()
            print("ACCESSING INFO...")
            time.sleep(2)
            print("\n==| AGENTS |==")
            mc.execute("select * from access where code='003'")
            engine.say("Send the message to Lakshmi dhru 003 ? ")
            engine.runAndWait()
            m = input("SEND MESSAGE TO LAKSHMI DHRU (YES/NO) : ")
            m = m.upper()
            if m == 'YES':
                engine.say("Enter the message")
                engine.runAndWait()
                mm = input("ENTER MESSAGE :")
                engine.say("Sending the message ")
                engine.runAndWait()
                print("SENDING MESSAGE...")
                time.sleep(2)
                engine.say("the message has been sent successfully")
                engine.runAndWait()
                print("MESSAGE SENT SUCCESSFULLY")
            if m == 'NO':
                engine.say("the message has been discarded")
                engine.runAndWait()
            return

        elif l == 'SPAIN':
            engine.say("locating the agents")
            engine.runAndWait()
            print("LOCATING AGENTS...")
            time.sleep(2)
            engine.say("Accessing information")
            engine.runAndWait()
            print("ACCESSING INFO...")
            time.sleep(2)
            print("\n==| AGENTS |==")
            mc.execute("select * from access where code='004'")
            engine.say("Send the message to Grunge Dilop 004 ?")
            m = input("SENT MESSAGE TO GRUNGE DILOP(YES/NO) : ")
            m = m.upper()
            if m == 'YES':
                engine.say("enter the message")
                engine.runAndWait()
                mm = input("TYPE MESSAGE : ")
                engine.say("sending the message through the servers in ITALY")
                engine.runAndWait()
                print("SENDING MESSAGE...")
                time.sleep(2)
                engine.say("the message has been sent successfully ")
                engine.runAndWait()
                print("MESSAGE SENT SUCCESSFULLY")
            if m == 'NO':
                engine.say("the message has been discarded")
                engine.runAndWait()
            return

        else:
            engine.say("Sorry, currently there are no agents in that area ....,but,Code 389 is 7 kilometers from the desired location, would you like to alert him ?")
            engine.runAndWait()
            z=input("Enter the Choice ( YES / NO ) : ")
            z=z.upper()
            if z== 'YES':
                engine.say("Enter the message")
                engine.say("Please note that this message will be automatically encrypted and sent !")
                engine.runAndWait()                
                mm = input("ENTER MESSAGE :")
                engine.say("Sending the message ")
                engine.runAndWait()
                print("SENDING MESSAGE...")
                time.sleep(2)
                engine.say("the message has been sent successfully")
                engine.runAndWait()
                print("MESSAGE SENT SUCCESSFULLY")
            if z == 'NO':
                engine.say("the message has been discarded")
                engine.runAndWait()
            return


    else:
        print(" || ACCESS DENIED ||")
        engine.say("Access denied")
        engine.runAndWait()
    return 


# FILE REGARDING THE CORRUPTED OFFICIALS IN THE PRESENT GOVERNMENT (DETAILS COLLECTED UNDER THE DIRECTION OF THE PRESIDENT)
def corruptoff():
    engine.say("enter the access ID")
    engine.runAndWait()
    b = input("ENTER ACCESS ID : ")
    if b == '25806':
        engine.say("Access granted")
        engine.runAndWait()
        print("\n===ACCESS GRANTED===")
        time.sleep(2)
        engine.say("Gathering information")
        engine.runAndWait()
        print("\nGATHERING INFORMATION...")
        time.sleep(2)
        print("\n")
        mc.execute("use defense")
        mc.execute("DROP TABLE IF EXISTS CORRUPTED_OFFICIALS")
        mc.execute("CREATE TABLE CORRUPTED_OFFICIALS(CODE INT PRIMARY KEY, NAME CHAR(25),CORRUPTION VARCHAR(25), AREAS_OF_CORRUPTION VARCHAR(25),DESIGNATION VARCHAR(25),PARTY_POLITICAL VARCHAR(25))")
        mc.execute("INSERT INTO CORRUPTED_OFFICIALS VALUES(091,'SATHEESH PAL','FRAUD','CONSTRUCTION','SI','LDF')")
        mc.execute("INSERT INTO CORRUPTED_OFFICIALS VALUES(092,'CHRIS JOSEPH','BRIBERY','FINANCE','ACP','UDF')")
        mc.execute("INSERT INTO CORRUPTED_OFFICIALS VALUES(093,'NASSER LAIQ','NEPOTISM','ROAD BUILDING','SP','BJP')")
        mc.execute("INSERT INTO CORRUPTED_OFFICIALS VALUES(094,'JAMES ANDROZ','EMBEZZLEMENT','TAX SYSTEM','CI','LDF')")
        mc.execute("INSERT INTO CORRUPTED_OFFICIALS VALUES(095,'TARIQ SUFAYAN','NEPOTISM','EDUCATION','ASP','UDF')")
        mc.execute("SELECT * FROM CORRUPTED_OFFICIALS")
        print("CODE", '%15s' % 'NAME', '%20s' % 'CORRUPTION', '%26s' % 'AREAS OF CORRUPTION', '%17s' % 'DESIGNATION',
              '%20s' % 'POLITICAL PARTY')
        for i in mc:
            print(i[0], '%20s' % i[1], '%15s' % i[2], "%24s" % i[3], "%17s" % i[4], "%15s" % i[5])
        time.sleep(5)
        print("\nPRIVACY | TERMS AND CONDITIONS ")
        print("\n THIS INFORMATION IS COLLECTED UNDER THE ORDER OF PRESIDENT OF LYVIA")
        print(" COPYRIGHT © 2021, GOVERNMENT OF LYVIA, ALL RIGHTS RESERVED ")
        time.sleep(7)
    else:
        print("|| ACCESS DENIED ||")
        engine.say("access denied")
        engine.runAndWait()
        time.sleep(3)
    return


def age():
    mc.execute("use defense")
    mc.execute("DROP TABLE IF EXISTS AGENTS")
    mc.execute("CREATE table AGENTS (Code int PRIMARY KEY)")
    mc.execute("INSERT INTO AGENTS VALUES(001)")
    mc.execute("INSERT INTO AGENTS VALUES (002)")
    mc.execute("INSERT INTO AGENTS VALUES(003)")
    mc.execute("INSERT INTO AGENTS VALUES(004)")
    mydb.commit()
    mc.execute("SELECT*FROM AGENTS")
    print("\nCODE")
    for i in mc:
        print(i[0])
    time.sleep(3)

    print("\nWould you like to Access more information ?")
    engine.say("Would you like to Access more information ?")
    engine.runAndWait()
    print("YES - 1 / NO - 2\n")
    aa = int(input("Enter your choice : "))
    if aa == 1:
        print("\nAccessing More Info. . . . . . . . ")
        engine.say("Accessing more information")
        engine.runAndWait()
        time.sleep(2)
        engine.say("Enter the access id")
        engine.runAndWait()
        ab = input("\nEnter the Access ID : ")
        if ab == "25806":
            print("\n== Access Granted ==")
            engine.say("Access Granted")
            engine.runAndWait()
            time.sleep(2)
            engine.say("please wait")
            engine.runAndWait()
            print("\nCONNECTING TO SERVER . . . . . . . . ")
            engine.say("connecting to server")
            engine.runAndWait()
            time.sleep(3)
            mc.execute("use defense")
            mc.execute("DROP TABLE IF EXISTS ACCESS")
            mc.execute("create table ACCESS (CODE int primary key  , NAME VARCHAR(20), AGE INT(5) , STATUS VARCHAR(10), CURRENT_LOCATION VARCHAR(250), MISSION VARCHAR(250) )")
            mc.execute("INSERT INTO ACCESS VALUES (001,'Mary Joseph',28,'ACTIVE','JAPAN','OVERLORD')")
            mc.execute("INSERT INTO ACCESS VALUES (002,'Steohen Jake',43,'ACTIVE','SWEDEN','THUNDER')")
            mc.execute("INSERT INTO ACCESS VALUES (003,'Lakshmi Dhru',24,'ACTIVE','RUSSIA','DYNAMO')")
            mc.execute("INSERT INTO ACCESS VALUES(004,'Grunge Dilop',36,'ACTIVE','SPAIN','BROSSA')")
            mc.execute("SELECT*FROM ACCESS")
            print("\nCODE", "%10s" % "NAME", "%20s" % "AGE", "%20s" % "STATUS", "%20s" % "CURRENT LOCATION",
                  "%10s" % "MISSION")
            for i in mc:
                print(i[0], '%21s' % i[1], '%12s' % i[2], '%20s' % i[3], '%15s' % i[4], '%15s' % i[5])
            time.sleep(4)
        else:
            print("|| ACCESS DENIED ||")
            engine.say("ACCESS DENIED")
            engine.runAndWait()
            time.sleep(3)
    elif aa == 2:
        engine.say("What else would you like to do ?")
        engine.runAndWait()

    else:
        print("INVALID OPTION")
        engine.say("INVALID OPTION")
        
    return



def other():
    engine.say("PLEASE SELECT FROM THE GIVEN OPTIONS ONLY")
    engine.runAndWait()
    print("\n==== Please select from the given options ====")
    time.sleep(3)
    return

def main():
    engine.say("Please select from the following options")
    engine.runAndWait()
    ch = "yY"
    for ch in "yY":
        print("\n","="*50)
        ac = int(input("\nCheck the Details of the Subordinates - 1 \nFiles about Evidences Collected - 2\nDetails about the undercover spies - 3\nALERT THE AGENTS - 4\nLocate an Agent - 5\nCorruption in the Ruling Government - 6\nExit - 0\n\nPlease select according to your requirement : "))
        if ac == 1:
            age()

        elif ac == 2:
            dispevidence()

        elif ac == 3:
            undercoverspies()

        elif ac == 4:
            alertagent()

        elif ac == 5:
            agentlocate()

        elif ac == 6:
            corruptoff()
        
        elif ac == 0:
            engine.say("Exiting the portal . ")
            engine.runAndWait()
            print("Exiting The Portal . . . . . . ")
            time.sleep(2)
            engine.say("See you soon ")
            engine.runAndWait()
            exit()

        elif ac>=7:
            other()


engine.say("Please Say the username")
engine.runAndWait()
try :
    with sr.Microphone() as source:
        print("Listening . . . . . .")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        try:
            for i in range(1,0,-1):
                if 'king'==command:
                    engine.say("Welcome")
                    engine.runAndWait()
                    wor = 'ring'
                    for i in range(3,0,-1):
                        print()
                        engine.say("Please enter your passcode")
                        engine.runAndWait()
                        password = stdiomask.getpass()
                        if password.lower() == wor:
                            print("\n== ACCESS GRANTED ==\n\n")
                            engine.say(" ACCESS GRANTED !")
                            engine.runAndWait()
                            time.sleep(2)
                            print("|| Welcome Agent 007 ||\n")
                            engine.say("Welcome back Agent 007 ")
                            engine.runAndWait()
                            main()
                         
                        else:
                             engine.say("Incorrect password !")
                             engine.runAndWait()
                             print("==| Password is Incorrect ! |==")

                    if i == 1:
                        engine.say("You have been denied access !")
                        engine.runAndWait()
                        print("\n==| ACCESS DENIED |==")
                        engine.say("Headquarters has been alerted ! The files have been encrypted and under lock down ,until further notice from the headquarters !")
                        engine.runAndWait()
                        exit()
                        
                    else:
                         pass

                else:
                    engine.say("Access Denied")
                    engine.runAndWait()
                    print("\n== ACCESS DENIED ==")
                    exit()

        except:
            print("-" * 25)
            exit()
except:
    print("~"*25)
