import os

def test():
    print(f"testing: os {os.getenv('API_KEY')}")

if __name__ == '__main__':
    test()