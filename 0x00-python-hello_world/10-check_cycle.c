#include "lists.h"
/**
 * check_cycle - a function to detect a loop in a linked list
 * @list: a typedef struct (the linked list)
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *prev, *forward;

	prev  = list;
	forward = list;
	while (prev && forward && prev->next)
	{
		prev = prev->next;
		forward = forward->next->next;

		if (prev == forward)
			return (1);
	}
	return (0);
}
