# Dividing Sequences
(IARCS OPC Archive, K Narayan Kumar, CMI)
This problem is about sequences of positive integers a1,a2,…,aN. A subsequence of a sequence is anything obtained by dropping some of the elements. For example, 3,7,11,3 is a subsequence of 6,**3**,11,5,**7**,4,3,**11**,5,**3** , but 3,3,7 is not a subsequence of 6,3,11,5,7,4,3,11,5,3 .

A fully dividing sequence is a sequence a1,a2,…,aN where ai divides aj whenever i < j. For example, 3,15,60,720 is a fully dividing sequence.

Given a sequence of integers your aim is to find the length of the longest fully dividing subsequence of this sequence.

Consider the sequence 2,3,7,8,14,39,145,76,320

It has a fully dividing sequence of length 3, namely 2,8,320, but none of length 4 or greater.

Consider the sequence 2,11,16,12,36,60,71,17,29,144,288,129,432,993 .

It has two fully dividing subsequences of length 5,

**2**,11,16,**12**,**36**,60,71,17,29,**144**,**288**,129,432,993 and<br>
**2**,11,16,**12**,**36**,60,71,17,29,**144**,288,129,**432**,993<br>

and none of length 6 or greater.<br><br>

# Input format
The first line of input contains a single positive integer N indicating the length of the input sequence. Lines 2,…,N+1 contain one integer each. The integer on line i+1 is ai.<br><br>

# Output format
Your output should consist of a single integer indicating the length of the longest fully dividing subsequence of the input sequence.<br><br>

# Test Data
You may assume that N ≤ 2500.<br><br>

# Example:
Here are the inputs and outputs corresponding to the two examples discussed above.<br>

## Sample input 1:
9<br>
2 <br>
3 <br>
7 <br>
8 <br>
14 <br>
39 <br>
145 <br>
76 <br>
320<br><br>

## Sample output 1:
3<br><br>

## Sample input 2:
14<br>
2<br>
11 <br>
16 <br>
12 <br>
36 <br>
60 <br>
71 <br>
17 <br>
29 <br>
144 <br>
288 <br>
129 <br>
432 <br>
993<br><br>

## Sample output 2:
5<br>

