def main():
    print(rectangle(5, 10))
    print(triangle(10, 6))
    print(house(6, 10, 5))

def rectangle(l,w):
    return(l*w)

def triangle(base, height):
    return(.5*base*height)

def house(height, width, lenght):
        return(triangle(height, width) + rectangle(lenght, width))


if __name__== "__main__":
    main()