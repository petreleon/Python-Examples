# never name it uuid.py
import uuid

def get_guid():
    return uuid.uuid1()

if __name__ == '__main__':
    print(get_guid())