#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert number into a sorted singly linked list
 * @head: pointer to beginning of list
 * @number: number to be inserted in the list
 * Return: address of the new node inserted or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	if (!current)
	{
		*head = new;
		return (new);
	}

	/* if head value is greater than the number*/
	if (current->n >= number)
	{
		*head = new;
		new->next = current;
		return (new);
	}

	while (current->next)
	{
		if (current->next->n >= number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}

		current = current->next;
	}

	current->next = new;

	return (new);
}
