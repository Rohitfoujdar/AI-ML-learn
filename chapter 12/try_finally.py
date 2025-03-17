def main():
    try:
       n= int(input("Enter your age: "))
       print(n)
    except Exception as e:
       print(e)
    finally:
       print("Hii, i am final value")
