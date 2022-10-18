#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


/**
 * infinite_while - Simulates an infinit loop
 * Return: 0 has success
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - The entry point to the code
 * Return: The status
 */
int main(void)
{
	int child_p, i;

	for (i = 0; i < 5; i++)
	{
		child_p = fork();
		if (child_p == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
