Here are some basic facts about tennis scoring: A tennis match is made up of sets. A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker. In some cases, players go on playing till one of them wins the set with a difference of two games.

Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match (i.e., 2 out 3 sets or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first for each set. Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's score is recorded on a separate line with the following format:

Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

For example, an input line of the form

Osaka:Barty:3-6,6-3,6-3<br>
indicates that Osaka beat Barty 3-6, 6-3, 6-3 in a best of 3 set match.<br>

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following statistics for each player:

Number of best-of-5 set matches won<br>
Number of best-of-3 set matches won<br>
Number of sets won<br>
Number of games won<br>
Number of sets lost<br>
Number of games lost<br><br>
You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria <br>
1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).

For instance, given the following data

Thiem:Medvedev:2-6,6-7,7-6,6-3,6-1<br>
Barty:Osaka:6-4,6-4<br>
Medvedev:Thiem:6-3,6-3<br>
Osaka:Barty:1-6,7-5,6-2<br>
Thiem:Medvedev:6-0,7-6,6-3<br>
Osaka:Barty:2-6,6-2,6-0<br>
Medvedev:Thiem:6-3,4-6,6-3,6-4<br>
Barty:Osaka:6-1,3-6,7-5<br>
Thiem:Medvedev:7-6,4-6,7-6,2-6,6-2<br>
Osaka:Barty:6-4,1-6,6-3<br>
Medvedev:Thiem:7-5,7-5<br>
Osaka:Barty:3-6,6-3,6-3<br><br>
your program should print out the following

Thiem 3 0 10 104 11 106<br>
Medvedev 1 2 11 106 10 104<br>
Osaka 0 4 9 76 8 74<br>
Barty 0 2 8 74 9 76<br>

```diff
Eg. Test Case!!
```

Gauff:Zverev:2-6,6-7,7-6,6-3,6-1<br>
Tsitsipas:Zverev:6-3,4-6,6-4,6-3<br>
Zverev:Thiem:6-0,7-6,6-7,6-3<br>
Thiem:Zverev:6-4,6-4<br>
Gauff:Zverev:2-6,6-2,6-0<br>
Thiem:Zverev:6-3,4-6,6-3,6-4<br>
Zverev:Thiem:7-6,4-6,7-6,2-6,6-2<br>
Thiem:Tsitsipas:7-5,7-5<br>
Gauff:Tsitsipas:3-6,6-3,6-3<br>
Gauff:Thiem:0-6,0-6,6-0,6-0,7-5<br>
Tsitsipas:Thiem:6-3,4-6,7-6,0-6,7-5<br>

Gauff 2 2 10 75 6 60<br>
Zverev 2 0 11 122 16 139<br>
Tsitsipas 2 0 7 68 7 71<br>
Thiem 1 2 14 133 13 128<br>
