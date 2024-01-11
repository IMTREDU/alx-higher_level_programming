#include "lists.h"

/**
 * sum_dlistint - calculates the sum of all the data (n)
 * in doubly linked list
 *
 * @head: the starting point of the list
 * Return: sum of the data
 */
int sum_dlistint(dlistint_t *head)
{
	int s;

	s = 0;

	if (head != NULL)
	{
		while (head->prev != NULL)
			head = head->prev;

		while (head != NULL)
		{
			s += head->n;
			head = head->next;
		}
	}

	return (s);
}
