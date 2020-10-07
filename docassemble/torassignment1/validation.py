import re
import string
from docassemble.base.util import *

verify_one = {0:"X",1:"W",2:"U",3:"T",4:"R",5:"R",6:"P",7:"N",8:"M",9:"L",10:"K"} #for F and G
verify_two = {0:"J",1:"Z",2:"I",3:"H",4:"G",5:"F",6:"E",7:"D",8:"C",9:"B",10:"A"} #for S and T

def checksum(applicant_nric):
  check = int(applicant_nric[1]) * 2 + int(applicant_nric[2]) * 7 + int(applicant_nric[3]) * 6 + int(applicant_nric[4]) * 5 + int(applicant_nric[5]) * 4 + int(applicant_nric[6]) * 3 + int(applicant_nric[7]) * 2
  if re.match(r'[TGtg]',applicant_nric[0]):
    check += 4
  check %= 11
  return check

def check_applicant_nric(applicant_nric):
  if not re.match(r'[STFGstfg][0-9]{7}[A-z]', applicant_nric):
    validation_error('Invalid NRIC format')
  else:
    last = checksum(applicant_nric)
    if re.match(r'[FGfg]',applicant_nric[0]):
      for key,value in verify_one.items():
        temp = verify_one[last]
        if applicant_nric[8].upper() != temp:
          validation_error('Invalid NRIC format')
        else:
          return True
    elif re.match(r'[STst]',applicant_nric[0]):
      for key,value in verify_two.items(): #if last from checksum function is 6, it should map to E to be valid
        temp = verify_two[last] #assigning item in dictionary
        if applicant_nric[8].upper() != temp:
          validation_error('Invalid NRIC format')
        else:
          return True
  