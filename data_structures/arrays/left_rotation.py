def rotLeft(a, d):
    rotates = d % len(a)
    return a[rotates:] + a[:rotates]
    
if __name__ == '__main__':
    main()
