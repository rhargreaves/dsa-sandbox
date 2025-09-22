class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_bits(a: int, b: int, c_in: int) -> tuple[int, int]:  # sum, c_out
            sum = a ^ b ^ c_in
            c_out = (a & b) | (b & c_in) | (a & c_in)
            return sum, c_out

        output = []
        c_in = 0
        a_index = len(a) - 1
        b_index = len(b) - 1
        while a_index >= 0 or b_index >= 0 or c_in != 0:
            a_bit = int(a[a_index]) if a_index >= 0 else 0
            b_bit = int(b[b_index]) if b_index >= 0 else 0
            sum, c_out = add_bits(a_bit, b_bit, c_in)
            output.append(str(sum))
            c_in = c_out
            a_index -= 1
            b_index -= 1

        return "".join(reversed(output))


# you can just do...
# return format(int(a,2) + int(b,2), 'b')
# and it is the most efficient
