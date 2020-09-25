# import re
# def txt_match(text):
#             patterns = '^[a-zA-Z0-9]+@+[a-z].com$'
#         if re.search(patterns,text):
#                 return 'Found a match!'
            
#         else:
#                 return('Not matched!')

# print(txt_match("deep23101999@gmail.com"))

import re

#Email,Pincode,Phone no.

def txt_match(text):
    patterns= r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    if re.search(patterns,text):
        # return ('It is correct')
        def txt_ma(txt):
            pincode= r"^[1-9][0-9]{5}$"
            if re.search(pincode,txt):
                def txt_mat(phone):
                    pp=r"[0-9][1-9]{9}$"
                    if re.search(pp,phone):
                        return "All information is correct"
                    else:
                        return "phone number is incorrect"
                print(txt_mat("8511452463"))
            else:
                return "pincode is not correct"
        print(txt_ma("390007"))
    else:
        return ('Not correct')
print(txt_match("deep23101999@gmail.com"))


#password

password = "Deep@1shivi"
flag = 0
while True:   
    if (len(password)<8): 
        flag = -1
        break
    elif not re.search("[a-z]", password): 
        flag = -1
        break
    elif not re.search("[A-Z]", password): 
        flag = -1
        break
    elif not re.search("[0-9]", password): 
        flag = -1
        break
    elif not re.search("[_@$]", password): 
        flag = -1
        break
    elif re.search("\s", password): 
        flag = -1
        break
    else: 
        flag = 0
        print("Valid Password") 
        break
  
if flag ==-1: 
    print("Not a Valid Password")

#output
All information is correct
None
None
Valid Password