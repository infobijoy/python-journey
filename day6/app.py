# Real Projects & Freelancer Eligibility & Discount Access
skill = input("Skill: ")
experience = int(input("Years: "))

if skill == "python" and experience >= 1:
    print("Ready for jobs")
else:
    print("Need more growth")


vip = True
coupon = False

if vip or coupon:
    print("Discount Applied")
else:
    print("No Discount")