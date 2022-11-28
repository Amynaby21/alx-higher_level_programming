#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle
 * @list: A pointer to the list
 *
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *before;
	listint_t *after;

	if (!list)
		return (0);

	before = list->next;
	after = list->next->next;

	while (before != NULL && after != NULL)
	{
		if (before == after)
			return (1);

		before = before->next;
		after = after->next->next;
	}
	return (0);
}
