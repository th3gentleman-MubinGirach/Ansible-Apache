import os 

os.system("tput setaf 6")
print("Welcome to Ansible+Apache magic")

def further():
	print("Great lets move ahead")
	os.system("touch new.html")
	html=input("What should be the content of the html file you would like to keep: ")
	filehtml = open("new.html", "w") 
	filehtml.writelines(html) 
	filehtml.close()
	os.system("ansible-playbook playbook.yml")

def inventory():
   print("Since you dont have an inventory i am creating an inventory for you at /root named as inventory.txt")
   os.system("touch inventory.txt")
   defaultentry="[hosts]"
   fileinv = open("inventory.txt", "w") 
   fileinv.writelines(defaultentry) 
   fileinv.close()
   print("Thats great you need to add the following path root/inventory.txt config file /etc/ansible/ansible.cfg in the inventory parameter ")
   
       
	


	


useri=input("Is your inventory good to go?: ")
if useri == "yes":
   further()

elif useri == "no":
    inventory()
    

else:
	print("PLEASE CHECK YOUR INPUT")
    
 
