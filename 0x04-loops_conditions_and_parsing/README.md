# 0x04-loops_conditions_and_parsing

Learning about shell loops, condition and parsing

## TASKS

### 0. Create a SSH RSA key pair

Generating a rsa key pair..

**Files** - `0-RSA_public_key.pub`


### 1. For Best School loop

Write a Bash script that displays Best School 10 times.

Requirement:

You must use the for loop (while and until are forbidden)

**Files** - 1-for_best_school


```
sylvain@ubuntu$ head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
sylvain@ubuntu$ ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
Note that:

The first line of my Bash script starts with #!/usr/bin/env bash
The second line of my Bash scripts is a comment explaining what it is doing
```


### 2. While Best School loop


Write a Bash script that displays Best School 10 times.

Requirements:

You must use the while loop (for and until are forbidden)


**Files** - 2-while_best_school

```
sylvain@ubuntu$ ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```



### 3. Until Best School loop

Write a Bash script that displays Best School 10 times.

Requirements:

You must use the until loop (for and while are forbidden)


**Files** - 3-until_best_school


```
sylvain@ubuntu$ ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
sylvain@ubuntu$ 
```



### 4. If 9, say Hi!

Write a Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.

Requirements:

You must use the while loop (for and until are forbidden)
You must use the if statement

**Files** - 4-if_9_say_hi

```
sylvain@ubuntu$ ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School
sylvain@ubuntu$ 
```


### 5. 4 bad luck, 8 is your chance

Write a Bash script that loops from 1 to 10 and:

displays bad luck for the 4th loop iteration
displays good luck for the 8th loop iteration
displays Best School for the other iterations
Requirements:

You must use the while loop (for and until are forbidden)
You must use the if, elif and else statements

**Files** - 5-4_bad_luck_8_is_your_chance

```
sylvain@ubuntu$ ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School
sylvain@ubuntu$ 
```
