# 0x06-regular_expressions

Learning about regular expressions

## TASKS

### 0. Simply matching School


Requirements:

* The regular expression must match School
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Files** - 0-simply_match_school.rb
Example:
```
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```



### 1. Repetition Token #0

Requirements:

* Find the regular expression that will match `hbttn`, `hbtttn`, `hbttttn`, `hbtttttn`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


**Files** - 1-repetition_token_0.rb


### 2. Repetition Token #1

Requirements:

* Find the regular expression that will match `htn`, `hbtn`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method


**Files** - 2-repetition_token_1.rb


### 3. Repetition Token #2

Requirements:

* Find the regular expression that will match `hbtn`, `hbttn`, `hbtttn`, `hbttttn`
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method

**Files**: 3-repetition_token_2.rb
