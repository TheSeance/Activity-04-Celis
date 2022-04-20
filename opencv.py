import cv2


def menu():
    filepath1 = "jinx.jpg"

    x = """
        I have provided an image for you :)
        Do you wish to use a different one?
        Please Press...
        1 - to use provided image
        2 - to use your own image """
    print(x)
    input1 = int(input("Input here: "))
    
    if input1 == 1:
        input2 = int(input("1 - Color \n2 - Grayscale \n3 - Unchanged \nRead image as: "))
        if input2 == 1:
            image = cv2.imread(filepath1, 1)
            cv2.imshow("Jinx in Color", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        elif input2 == 2:
            image = cv2.imread(filepath1, 0)
            cv2.imshow("Jinx in Grayscale", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        else:
            image = cv2.imread(filepath1, -1)
            cv2.imshow("Jinx Unchanged", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        
    elif input1 == 2:
        filepath2 = input("Please Enter Complete and Correct Filepath of your Image:")
        input2 = int(input("1 - Color \n2 - Grayscale \n3 - Unchanged \nRead image as: "))
        if input2 == 1:
            image = cv2.imread(filepath2, 1)
            cv2.imshow("Your Image in Color", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        elif input2 == 2:
            image = cv2.imread(filepath2, 0)
            cv2.imshow("Your Image in Grayscale", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
        else:
            image = cv2.imread(filepath2, -1)
            cv2.imshow("Your Image Unchanged", image)
            cv2.waitKey(0)
            cv2.destroyAllWindow()
    else:
        print("Please choose between 1 and 2 only")
        menu()
