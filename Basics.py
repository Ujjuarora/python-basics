#------------------ printing in python ------------------#
print("x is 1.");
print("Mohit", "\n\n")
print("arun");
print('Hello');


#------------------ variation in printing  ------------------#
print("Tarun", end=" :-)")


#------------------ input variable printing  ------------------#
_x_string = input("Please Enter x::");
_y_string = input("Please Enter y::");

#------------------ converting input variable printing  ------------------#
_x_int=int(_x_string);
_y_int=int(_y_string);

print("value Entered are :: " , (_y_int/_x_int));

appx_pi = 22 / 7;
print (appx_pi);
x=5;

print(x);

########################## String Basics ##########################

weather = 'It\'s a nice and warm day'
print (weather);

colors = 'Blue\nRed\nGreen'
print (colors);

print("============================")
raw_str = r'Blue\nRed\nGreen'  ## r is used for not using \n and showing as it is.
print(raw_str);


########################## String Concatenation ##########################
str1 = 'Hello'
str2 = ' World'
print(str1 + str2)

style_char = '-';
style_char * 20;
print(style_char);
style_char=style_char * 20;
print(style_char);


# assigning multiple line string to variable
poem = """\
Dil diyan gallan karange naal naal baeke,   
akkha naal akkhan nu milake,   
Dil diyan gallan ...!!
""" ;
print(poem ,end='');


########################## Boolean Basics ##########################

a=0;
print(bool(2),bool(1),bool(a));
print(bool(1));
print(bool(a));
print(bool(2));
print(bool(''));






