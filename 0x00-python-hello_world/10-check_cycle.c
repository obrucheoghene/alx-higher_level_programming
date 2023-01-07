#include "lists.h"

/**
 * check_cycle - check is a singly linked list has a cycle in it
 * @list: pointer to the head
 *
 * Return: 0 if there is no cylce, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (!list)
		return (0);

	current = list->next;

	while (current)
	{
		if (current == list)
		{
			return (1);
		}
		current = current->next;
	}

	return (0);
}
