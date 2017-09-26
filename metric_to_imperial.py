metres = int(input("Enter the number..."))
#inches = metres/0.0254
#feet = float(inches/12)
#print("The inches are %d." % inches)
#print("The feet is %d feet." % feet)
feet = metres/0.3048
inches = (feet/12)*10
print("The %d metre convert to feet is %d feet %d inches." %(metres,feet,inches))