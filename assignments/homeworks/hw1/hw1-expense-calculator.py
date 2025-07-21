"""
Personal Finance Calculator
Student : [Aunnop Somocha]
Date : [21/07/2025]
Purpose : calculate monthly Gudget and saving
"""
#รับรายได้และค่าใช้จ่าย
income = float(input("User's monthly income in THB :"))
rent = float(input("Monthly rent / housing cost :"))
food = int(input("Monthly food budget in THB :"))
transportation = float(input("Monthly transportation expenses :"))
entertainment = int(input("Monthly entertainment budget :"))
emergency_percent = float(input("Percentage to save for emergency :"))
investment_percent = float(input("Percentage to invest :"))

total_fixed = rent + transportation #คำนวณค่าใช้จ่ายแบบคงที่(fixed)และแปรผัน(variable)
total_variable = food + entertainment
total_expenses = total_fixed + total_variable
remaining_income = income - total_expenses #คำนวณรายได้ที่เหลือหลังหักค่าใช้จ่าย
emergencyfund = income * (emergency_percent/100) #คำนวณเงินที่เก็บไว้เผื่อฉุกเฉิน
investment = income * (investment_percent/100)
available_saving = remaining_income - emergencyfund - investment #คำนวณเงินที่สามารถเก็บออมได้
expenses_ratio = (total_expenses/income)*100 #คำนวณอัตราส่วนค่าใช้จ่ายเมื่อเทียบกับรายได้

#สรุปงบประมาณ
print("=== MONTHLY BUDGET REPORT ===")
print(f"Income : {income : .2f}THB")
print(f"Fixed Expenses : {total_fixed : .2f}THB")
print(f"Variable Expenses : {total_variable : .2f}THB")
print(f"total Expenses : {total_expenses : .2f}THB")
print(f"Remaining : {remaining_income : .2f}THB")
print()

#แสดงรายละเอียดเงินออม
print("=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund({emergency_percent}):{emergencyfund: .2f}THB")
print(f"Investment({investment_percent}):{investment: .2f}THB")
print(f"Available for Savings . {available_saving: .2f}THB")
print()
print("=== ANALYSIS ===") #แสดงการวิเคราะห์ค่าใช้จ่าย
print(f"Expenses Ratio : {expenses_ratio: .2f}%")