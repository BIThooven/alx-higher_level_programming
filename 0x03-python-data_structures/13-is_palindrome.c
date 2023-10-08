#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - a functions that checks if a linked list is palindrome
 * @head: a pointer to the next node
 * Return: returns 0 if false, 1 if true
*/
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    int len = 0, i = 0;
    int arr[1024];

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (current != NULL)
    {
        arr[len] = current->n;
        len++;
        current = current->next;
    }

    for (i = 0; i < len / 2; i++)
    {
        if (arr[i] != arr[len - i - 1])
            return (0);
    }

    return (1);
}

