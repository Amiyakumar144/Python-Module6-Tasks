dict={'amiya':98,'barsha':97,'madhu':89,'alekh':97}
char_name=input("enter student name to get  your mark....")

if char_name in dict:
    print(f' hey {char_name} your  mark is ={dict[char_name]}')
else :
    print(f"{char_name} is not a valid students ")



