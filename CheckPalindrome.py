def Checkpalindrome(n): # Checks wether a given string can be converted into palindrome in 1 step.
    count = 0
    z = len(n) - 1
    if n ==n[::-1]:
        return "Yes"
    else:
        for i in range(len(n)//2):
            if n[i] != n[z]:
                count += 1
            if count > 1:
              return "No"
            z -= 1    
        return "Yes"
        

# Driver Code with an Example.
x = Checkpalindrome("abccaa")
print(x)
