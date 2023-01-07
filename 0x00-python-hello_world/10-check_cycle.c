#include "lists.h"

/**
 * check_cycle - check is a singly linked list has a cycle in it
 * @list: pointer to the head
 *
 * Return: 0 if there is no cylce, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
