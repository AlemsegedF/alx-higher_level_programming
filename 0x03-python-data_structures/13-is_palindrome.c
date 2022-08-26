#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a linked list is a palindrom
 * @head: poinyer to a linked list
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	int len, i;
	listint_t  *copy;

	copy = (*head);
	for (len = 0; copy->next != NULL; len++)
	{
		copy = copy->next;
	}
	if (len == 0)
		return (1);
	int array[len + 1];

	for (i = 0; i <= len; i++)
	{
		array[i] = (*head)->n;
		*head = (*head)->next;
	}
	for (i = 0; i <= len / 2; i++)
	{
		if (array[i] != array[len])
			return (0);
		len--;
	}
	return (1);
}
