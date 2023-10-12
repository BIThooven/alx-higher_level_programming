#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - a function that prints a linked list elements
 * @h: the head node pointer
 * Return: returns the number of elements
*/
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}

	return (count);
}
