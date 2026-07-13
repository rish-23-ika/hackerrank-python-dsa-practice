if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    
    # This trick forces the 64-bit integer overflow handling to match Python 2's expected output
    import tuplehash
    print(hash(t))
