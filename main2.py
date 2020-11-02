from functional import outer,something

globalstate = "Global state"

reference = outer("Great world!!")
something()
reference2 = outer("Greater World!!!");
something()

print('------------------------------------------------')

reference();
reference2();