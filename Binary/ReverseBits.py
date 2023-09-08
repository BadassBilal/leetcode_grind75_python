
def reverseBits(bitnum: int) -> int:
    # return int(f"b0{bin(bit)[:1:-1]}", 2)
    rslt = 0
    for i in range(32):
        last_bit_of_bitnum = (bitnum >> i) & 1 # if bitnum = 101101 => 10110->1<- then last_bit = 1 on the right most.
        '''
        bitnum >> i move the i-th bit to the last. 
        i = 0, the same number is present.
        & 1 gives the last bit only (which we need in this case)
        '''
        rslt = rslt |last_bit_of_bitnum << 31-i
        '''
        now we OR with the result binary which is 32 zeroes.
        if we have 1 in the last_bit, we move it 31-i to the left and then OR it so, it can be 1 as well.
        if we have 0 in the last_bit, we ignore (altho operation is done).
        '''
    return (rslt)




def main():
    print(reverseBits(0b00000010100101000001111010011100))


if __name__ == '__main__':
    main()