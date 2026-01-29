threshold = 1000
product = 1
currentNumber = 1

while product <= threshold: #runs until product surpasses the threshold
    product =product*currentNumber #tracking current multiplier
    if product > threshold:
        print(product)
        print(currentNumber)
    currentNumber +=1 #next integer increment