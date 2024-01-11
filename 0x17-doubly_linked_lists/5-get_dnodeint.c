#include "lists.h"

/**
 * get_dnodeint_at_index - retrieves the nth node of a dlistint_t linked list
 * @head: pointer to the head of the list
 * @index: index of the node to retrieve
 * Return: nth node or NULL if not found
 **/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int s;
	dlistint_t *tmp;

	s = 0;
	if (head == NULL)
	return (NULL);

	tmp = head;
	while (tmp)
	{
	if (index == s)
	return (tmp);
	s++;
	tmp = tmp->next;
	}
	return (NULL);
}
