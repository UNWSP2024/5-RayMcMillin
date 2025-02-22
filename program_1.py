# Ray McMillin, Kilometer Conversion, 2/21/2025


def kilometer_conversion(kilometers):    
    miles = kilometers * 0.6214
    # Return the variable to the calling function
    return miles

def main():
    kilometers = float(input("Please enter the distance in kilometers: "))
    miles = kilometer_conversion(kilometers)
    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

if __name__ == '__main__':
    
    main()
