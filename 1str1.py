s=str(input("Introduceti numele prenumele: "))
a,b =s.split()
if ( a.title()==a and b.title()==b) :
    print("Numele este scris corect")
else :
    print("Eroare")