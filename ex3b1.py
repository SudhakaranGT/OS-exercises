def main():
    i=int(input("Process 1; Input: "))
    if i!=0:
        import ex3b2
        ex3b2.main(i)
if __name__ == '__main__':
    exec("main()")


