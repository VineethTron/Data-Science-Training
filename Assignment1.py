annual_sal = int(input("Enter the Salary : "))
hra_amount = int(input("Enter the HRA Amount : "))
other_deducs = int(input("Enter Other Deductions : "))

if other_deducs > 80000 :
    print("Deducations can't be more than 80,000")
else:
    net_taxable_sal = annual_sal - hra_amount - other_deducs
    if net_taxable_sal <= 300000 :
        print("No tax !!")
    else:
        final_amount = net_taxable_sal - 300000
        print("Final Amount = ",final_amount)
        if final_amount > 300000 and final_amount <= 600000 :
            tax = final_amount * 0.1
            print("Tax to be paid = ", tax)
        elif final_amount > 600000 and final_amount <= 1000000:
            tax = final_amount * 0.15
            print("Tax to be paid = ", tax)
        else :              #Salary Greater than 1000000
            tax = final_amount * 0.20
            print("Tax to be paid = ", tax)