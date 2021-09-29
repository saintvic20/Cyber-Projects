while True:

    ProtocolsDict = {'FTP': '21', 'FTPS': '21', 'SSH': '22', 'SFTP': '22', 'TELNET': '23', 'SMTP': '25','TACAS+': '49', 'DNS': '53',
                     'DHCP': '67/68', 'TFTP': '69', 'HTTP': '80', 'HTTPS': '443', 'KERBEROS': '88/544/2105', 'POP3': '110', 'POP3S': '995',
                     'NTP': '123','MICROSOFT RPC': '135', 'IMAP4': '143', 'IMAP4S': '993', 'SNMP': '161', 'SMB': '445', 'PRINTERS': '515/9100' ,'LDAP': '389',
                     'LDAPS': '636', 'MICROSOFT SQL': '1433/1434', 'ORACLE': '1521', 'H.323': '1720','RADIUS': '1645/1646/1812/1813', 'MYSQL': '3306', 'RDP': '3389', 'SIP': '5060',
                     'POSTGRESQL': '5432', 'RTP': '1024-65,535', 'SRTP': '1024-65,535'}

    PortD = {
        '21': 'FTP or FTPS. FTP is used for file transfers but is not secure. Use SFTP or FTPS. FTPS is FTP over TLS or SSL (make sure to use TLS1.3)',
        '22': 'Either SSH or SFTP. SSH is essentialy the replacement of telnet since it is encryped. SFTP is the secure file transfer protocol.'
              '\nSFTP uses SSH and is a full feature file transfer that runs uninterupted file transfers while being encrypted. SFTP could give you directy listings as well',
        '25': 'SMPT is the simple mail transfer protocol. SMTP is used by mail servers and agents to send/receive email. \nIncorporate it with TLS 1.3 to avoid M-I-T-M attacks.',
        '53': 'DNS (UDP) is the doman name service that is used for converting a domain name to an IP. Many different types of DNS records.',
        '23': 'Telnet which is used to logging to devices remotely. Telnet is very '
              'insecure, sent in clear text.',
        '49': 'TACAS+ (UDP or TCP) is another AAA framework used by CISCO networking devices for remote administration of said devices.',
        '67': 'DHCP (UDP) is the Dynamic Host Configuration Protocol. DHCP is used to dynamically assign hosts ip on a network. DHCP servers could also statically assign IPs. ',
        '69': 'TFTP (UDP) is a very simple form of file transfer. Very insecure. Usually used to send files that are not sensative',
        '80': 'HTTP is used for web applications. Use HTTPS (PORT 443) for a secure '
              'connection over TLS',
        '443': 'HTTPS is HTTP over a secure TLS/SSL connection. Use TLS1.3',
        '88':'Kerberos (udp 88 and tcp 544/2105) is a ticket based authentication service used to access domain services.\n Kerberos is usually found in Microsoft environments and provides SSO.',
        '110': 'POP3 or Post Office Protocol. POP3 is the most recent POP version for receiving email. It is a client/server protocol. \nIt is deisgned to delete mail on the server as soon as the user has '
               'downloaded it (can be specified to save email for some time \nafter it is received however). "Store and foward service". Remember, POP is used to receive email while SMTP is used to transfer email.'
               '\nPOP3S is POP3 using TLS and is usually on port 995',
        '123': 'NTP is network time protocol (UDP). NTP is used to sync devices to a standard time. Very important for logging. \nNTP can be attacked and fed fake information to throw off sync. '
               'To protect NTP, use NTS (Network time Security port 4460). \nAlternatively, NTP can be secured with symmetric keys but would need a key for each client (not scalable with numerous clients).',
        '135': "Microsoft's RPC runs processes for network protocols.",
        '143': 'IMAP4 or Internet Mail Access Protocol 4, is a standard for storing and retrieving messages from SMTP hosts. Unlike POP3, \nIMAP4 stores the message on a server and syncs the email message accorss '
               'multiple devices. IMAP4 is more widely used. \nUse IMAP4S (IMAP4 over TLS1.3) on port 993, for secure communications.',
        '161':'SNMP is the Simple Network Management Protocol (UDP). SNMP is used for management and monitering of network connected devices.\nEnsure to use SNMPv3 as other verions are insecure.',
        '389': 'LDAP is the light weight directory access protocol. It is mostly used in Microsoft Active Directory but can be used in \nother environments like Red Hat'
               'Directroy servers. LDAP helps communicate in a network and is how AD is able to work. (Kerberos could also be used however).\nLDAPS (over port 636) provides security using encryption.',
        '445': 'SMB or Microsoft DS (Domain Services). SMB is Server Message Block and should usually be disabled since SMB is insecure.\nAlways try to use SMB 3 and make sure SMB signing is on.',
        '515': 'Common port for printers (and port 9100).',
        '636': 'LDAPS is the secure version of LDAP that uses encryption. Use TLS1.3!',
        '993': 'IMAP4S or IMAP4 over SSL/TLS',
        '995': 'POP3S or POP3 over SSL/TLS',
        '1433': "Microsoft's SQL database.",
        '1521': "Oracle's SQL database.",
        '1720': 'H.323 is what was used for voice over ip. One of the earliest standards. Based in telephony while its counter part,\n'
                'SIP (udp or tcp port 5060/5061), is text based and uses http.  ',
        '1645': 'Radius (UDP) is a AAA protocol. Radius uses a Radius Server and Radius clients (router, switch, vpn concenctrator). \nUser tries to connect to a Radius client which passes the resuest to the Radius server, '
                'if accepted by the server, the user has network access. \nTo secure Radius, ensure you are using Radius with either EAP-TLS or EAP-TTLS-PAP.',
        '3306': 'MySQL. A relational database based in SQL.',
        '3389': 'RDP or remote desktop protcol. It is used to remotely share a desktop'
                'or just an application. It is crossed plateform but mostly seen in windows. \nBest practice is to turn this off.',
        '5060': 'SIP is session initiation protocol. SIP is used in VOIP to set up calls,'
                'maintaining them, and terminating them.\nSIP uses RTP (Real-Time Protocol) or SRTP (Secure RTP) to transport media like voice and video.\nRTP & SRTP are assigned ports in the unprivileged ranges '
                '(1024 - 65,535).',
        '5432': 'PostgreSQL or Postgres is a free open source relational database.',
        '1024': 'This is the unprivileged range and ranges from 1024-65,535. Protocols in this area are currently outside the scope of this project...\nIn other words, you are on your own :)'}

    print("\nEnter a port or protocol to know more about it. Enter 'list' to list all the protocols or 'q' to quit.")
    print(
        "The port number will provide more detail about the protocols usually found on that port. Assume TCP unless specified.")
    print("If multiple ports, select the first to learn more.\n")
    question = input("What would you like to know? ")
    question = question.upper()

    if question in ProtocolsDict.keys():
        answer = ProtocolsDict[question]
        print("\nThe port number for protocol " + question + " is " + answer + "!\n")

    elif question in PortD.keys():
        answer = PortD[question]
        print("\nAnswer: " + answer + "\n")

    elif question == "LIST":
        print("\nProtocols in program and usual port numbers:")
        print(ProtocolsDict)
        print("\n\n")

    elif question == 'Q':
        break
    else:
        print("\nThe protocol can't be found\n")
