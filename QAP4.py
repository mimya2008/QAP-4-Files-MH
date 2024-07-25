# Description: Program for The One Stop Insurance Company to enter and calculate new insurance policy
# information for its multiple customers.
# Author: 
# Date(s):
 
 
# Define required libraries.
import datetime
import FormatValues as FV

import time
import sys

 
# Define program constants.

# NEXT_POLICY_NUM = 1944
# BASIC_PREMIUM = 869.00
# DIS_ADD_CARS = .25
# COST_EX_LIA_COVERAGE = 130.00
# COST_GLASS_COVERAGE = 86.00
# COST_LOANER_CAR_COVERAGE = 58.00
# HST_RATE= .15
# PROCESS_FEE = 39.99

PAY_TIME = 8



# Open the defaults file and read the values into variables
# The file must be created first since it is being read, it must exits. 

f = open('Const.dat', 'r')
# Values are stored as strings, covert according
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())

DIS_ADD_CARS = float(f.readline())
COST_EX_LIA_COVERAGE = float(f.readline())
COST_GLASS_COVERAGE = float(f.readline())
COST_LOANER_CAR_COVERAGE = float(f.readline())

HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()


# Define program functions.

def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


 
# Main program starts here.
while True:
   
    # Gather user inputs.
    CustFirstName = "Mimya"#input("Enter the Customer First Name: ").title
    CustLastName = "Hafiz"#input("Enter the Customer Last Name: ").title
    FullName = CustFirstName + " " + CustLastName
    StAdd= "12 Torbay Road"#input("Enter the Street Address: ")
    City = "St. John's"#input("Enter the City: ").title
    

    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MN", "SK", "AB", "BC", "YT", "NW", "NT"]
    while True:
        Prov = "NL"#input("Enter the Province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be Blank - Please Reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 Digit Code - Please Reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a Valid Province - Please Reenter.")
        else:
            break



    Postal = "A1A2V2"#input("Enter the Postal Code (X9X9X9): ").upper()
    PhoneNum = "7097659098"#input("Enter the Phone Number (9999999999): ")
    PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
    CellNum = "7097659098"#input("Enter the Cell Number (9999999999): ")
    CellNum = "(" + CellNum[0:3] + ") " + CellNum[3:6] + "-" + CellNum[6:]

    InsCarsNum = int(input("Enter the Number of Cars Being Insured: "))
    
    
    ExtLiability = input("Enter the Extra Liability Status up to $1,000,000(Y/N): ").upper()
    if ExtLiability == "Y":
        ExtLiabilityAmt = COST_EX_LIA_COVERAGE
    else:
        ExtLiabilityAmt = 0
                                

    GlassCoverage = input("Enter the Optional Glass Coverage Status(Y/N): ").upper()
    if GlassCoverage == "Y":
        GlassCoverageAmt = COST_GLASS_COVERAGE
    else:
        GlassCoverageAmt = 0


    LoanerCar = input("Enter the Optional Loaner Car Status(Y/N): ").upper()
    if LoanerCar == "Y":
        LoanerCarAmt = COST_LOANER_CAR_COVERAGE
    else:
        LoanerCarAmt = 0

   


    # Current Date
    CurDate = datetime.datetime.now()
    InvoiceDate= CurDate.strftime("%Y-%m-%d")


    # first payment date


    FirstPaymentYear = CurDate.year
    FirstPaymentMonth = CurDate.month + 1

    if FirstPaymentMonth > 12:
        FirstPaymentMonth = 1
        FirstPaymentYear += 1
    
    FirstPaymentDate = datetime.date(FirstPaymentYear, FirstPaymentMonth, 1)
    FirstPaymentDate= FirstPaymentDate.strftime("%Y-%m-%d")



    # Process each claims, date, amount and store results in lists.
    ClaimNumLst = []
    ClaimDateLst= []
    ClaimAmtLst = []
 
    NumClaims = int(input("How many Claims are to be Recorded: "))
    for j in range(1, NumClaims + 1):

        ClaimNum = int(input("Enter the Claim Number: "))
        ClaimNumLst.append(ClaimNum)

        ClaimDate = input("Enter the Claim Date: ")
        ClaimDateLst.append(ClaimDate)

        ClaimAmt = float(input("Enter the Claim Amount: "))
        ClaimAmtLst.append(ClaimAmt)


    # Perform required calculations.
    
    if InsCarsNum == 1: 
        INS_PRE_RATE = BASIC_PREMIUM
    else:
        Add_Ins_Pre_Rate = BASIC_PREMIUM - (BASIC_PREMIUM * DIS_ADD_CARS)
        INS_PRE_RATE = BASIC_PREMIUM + (Add_Ins_Pre_Rate * (InsCarsNum - 1))

        
    TotExtraCost = ExtLiabilityAmt + GlassCoverageAmt + LoanerCarAmt
    TotInsPremium = INS_PRE_RATE + TotExtraCost

    HST = TotInsPremium * HST_RATE
    TotCost = TotInsPremium + HST

    TotCost_ProcessFee = TotCost + PROCESS_FEE

    print("Payment Options:")
    print("1. Full.")
    print("2. Monthly.")
    print("3. Down Pay.")

    #PayOptionLst = ["Full", "Monthly", "Down Pay"]
    PayOptionLst = [1, 2, 3]
    while True:
        PayOption = int(input("Enter the Payment Option(1,2,3): "))
        if PayOption == "":
            print("Error - Payment Option cannot be blank - Please Reenter.")
        
        elif PayOption not in PayOptionLst:
            print("Error - Not a valid Payment Option - Please Reenter.")
        else:
            break
    
   

    if PayOption == 3:    
        PaidAmt = float(input("Enter the Down Payment Amount: "))
        MonthlyPayment = (TotCost + PROCESS_FEE - PaidAmt) / PAY_TIME
                
    elif PayOption == 1:
            PaidAmt = TotCost
            MonthlyPayment = 0

    else:
        PaidAmt = 0
        MonthlyPayment = (TotCost + PROCESS_FEE) / PAY_TIME        
    

    
    
    # Display results
    # For the Insurance Details Data
    f = open("Policy.dat", "a") #Mode can be 'a' for append, 'w' for overwrite, 'r' to read.
 
    # Any value written to a file must be recognized as a string.
    f.write(f"{str(NEXT_POLICY_NUM)}, ")
    f.write(f"{InvoiceDate}, ") # This is the current system date

    f.write(f"{FullName}, ")
    f.write(f"{StAdd}, ")
    f.write(f"{City}, ")
    f.write(f"{Prov}, ")
    f.write(f"{Postal}, ")
    f.write(f"{PhoneNum}, ")
    f.write(f"{CellNum}, ")


    f.write(f"{InsCarsNum}, ")
    f.write(f"{INS_PRE_RATE}, ")
    f.write(f"{ExtLiability}, ")
    f.write(f"{GlassCoverage}, ")
    f.write(f"{LoanerCar}, ")
    f.write(f"{TotInsPremium}, ")

    f.write(f"{PayOption}, ")
    f.write(f"{PaidAmt}, ")
    f.write(f"{MonthlyPayment},\n ")
    f.close()


    # For the Previous Claim Details Data

    f = open("Claims.dat", "a") #Mode can be 'a' for append, 'w' for overwrite, 'r' to read.
 
    # Any value written to a file must be recognized as a string.
    f.write(f"{InvoiceDate}, ") # This is the current system date
    f.write(f"{ClaimDate}, ")
    f.write(f"{str(ClaimNum)}, ")
    f.write(f"{CustFirstName}, ")
    f.write(f"{CustLastName}, ")
    f.write(f"{str(ClaimAmt)}\n")
 
    f.close()



    print()
    print()
    print(f"       ======================================================================================================")
    print(f"                                             One Stop Insurance Company                       ")
    print(f"                                             Insurance Premium Details                        ")
    print(f"       ======================================================================================================")

    print(f"       Mail To:                                                                               ")
    print(f"       {FullName}                                                           ")
    print(f"       {StAdd}                                                         ")
    print(f"       {City}, {Prov}                                                  ")
    print(f"       {Postal}                                                                        Policy No:         {NEXT_POLICY_NUM:>5d}                            ")
    print(f"       Phone Number: {PhoneNum:>13s}                                                  Invoice Date: {InvoiceDate:>10s}")                                                 
    print(f"       Cell Number:  {CellNum:>13s}                                                  Due Date:     {FirstPaymentDate:>10s}")
    print(f"       ======================================================================================================")

    print(f"                      For questions regarding policy or premiums, please contact  your agency")
    print(f"       ------------------------------------------------------------------------------------------------------")

    print()
    
    print(f"       Pay            Policy             Total         Premium &           Monthly             Payment")
    print(f"       Date           Number             Payment       Fees                Due                 In Full")
    print(f"       ------------------------------------------------------------------------------------------------------")
    print(f"       {FirstPaymentDate:>10s}      {NEXT_POLICY_NUM:>5d}          {FV.FDollar2(PaidAmt):>10s}      {FV.FDollar2(TotCost_ProcessFee):>10s}        {FV.FDollar2(MonthlyPayment):>10s}          {FV.FDollar2(TotCost):>10s}")
    print(f"       ------------------------------------------------------------------------------------------------------")
    print(f"                                                                      Minimum Amount Due:   {FV.FDollar2(MonthlyPayment):>10s}")

    
    print()



    print()
    print()
    print("                                  ---------------------------------------")
    print(f"                                         Previous Claim History                ")
    print()
    print("                                  Claim #      Claim Date          Amount")
    print("                                  ---------------------------------------")
    for j in range(0, len(ClaimNumLst)):
        print(f"                                  {ClaimNumLst[j]:>5d}        {ClaimDateLst[j]:>10s}      {FV.FDollar2(ClaimAmtLst[j]):>10s}")


    print()
    print()
 

    


    # Update any values for the next claim.
    # Can place the inside to loop to update each time, or in the housekeeping
    # section below to update when the user exists in the program
    NEXT_POLICY_NUM += 1

    # Write the current values back t the default file. Note the use of “w” to overwrite and the use of
    # the \n so that each value is placed on a separate line.
   
    f = open('Const.dat', 'w')
    # Values are stored as strings, covert according
    f.write(f"{NEXT_POLICY_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")

    f.write(f"{DIS_ADD_CARS}\n")
    f.write(f"{COST_EX_LIA_COVERAGE}\n")

    f.write(f"{COST_GLASS_COVERAGE}\n")
    f.write(f"{COST_LOANER_CAR_COVERAGE}\n")

    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")
    f.close()
    
 
    print()

 
    TotalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Insurance Policy Data ..."
 
    for i in range(TotalIterations + 1):
        time.sleep(0.1)  # Simulate some work
        ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()

    
    print()
    print("Insurance Policy data has been sucessfully saved.")
    print()
    
    
    Continue = input("Do you want to process another claim (Y / N): ").upper()
    if Continue == "N":
        break



 
# Any housekeeping duties at the end of the program.
