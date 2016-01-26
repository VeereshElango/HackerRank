from itertools import chain, combinations,permutations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def is_palindrome(s):
	return True if list(s) == list(reversed(s)) else False
def longest_palindrome(s):
	for x in reversed( list(map(''.join, powerset(s))) ):
		perms = [''.join(p) for p in permutations(x)]
		for val in perms:
			if is_palindrome(val):
				return val
seq = "abccdba"
seq2 = "zxdyyz"
l_seq = longest_palindrome(seq)
l_seq2 = longest_palindrome(seq2)
if l_seq % 2 ==0 :
	print(l_seq[: l_seq/2] + l_seq2 + l_seq[l_seq/2:])
elif l_seq2 %2 == 0:
	print(l_seq2[: l_seq2/2] + l_seq1 + l_seq2[l_seq2/2:])
print(len(longest_palindrome(l_seq+l_seq2)))
