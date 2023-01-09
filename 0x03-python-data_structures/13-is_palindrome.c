#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *reversed;
	listint_t *temp;

	reversed = malloc(sizeof(listint_t));
	if (!reversed)
		return (0);

	/* empty list is a palindrome */
	if (!current)
		return (1);

	/* list with one item is a palindrome */
	if (!current->next)
		return (1);

	/* created a reversed list */
	reversed = NULL;

	while (current)
	{
		temp = reversed;
		reversed = current;
		reversed->next = temp;
		current = current->next;
	}

	/*reset current */
	current = *head;
	temp = reversed;
	while (current)
	{
		if (current->n != temp->n)
			return (0);
		current = current->next;
		temp = temp->next;
	}

	return (1);
}
