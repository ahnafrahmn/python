
print(" ft ==>  meters ")
print("Give a spapce between feets and inches")
ft, i = input("ft , inch :: ").split()
ft = int(ft)
i = int(i)
h = ft*0.3048 + i*0.0254
h = float(h)
print(ft, "ft", i, "inches", "==>", format(h, ".2f"), "meters")
