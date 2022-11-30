#include "lists.h"

/**
 * insert_node - Insert a number into a sorted listed link
 * @head: A pointer to the head of the linked list
 * @number: The number to insert
 *
 * Return: The address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr1 = *head;
	listint_t *ptr2;

	if (!head)
		return (NULL);

	ptr2 = malloc(sizeof(listint_t));
	if (ptr2 == NULL)
		return(NULL);
	ptr2->n = number;
	ptr2->next = NULL;

	if (ptr1 == NULL)
	{
		ptr1 = ptr2;
		(ptr1)->next = NULL;
		return (ptr2);
	}
	if ((ptr1)->next == NULL)
	{
		if ((ptr1)->n < ptr2->n)
			(ptr1)->next = ptr2;
		else
		{
			ptr2->next = *head;
			*head = ptr2;
		}
		return (ptr2);
	}
	while (ptr2->next != NULL)
	{
		if (ptr1 == NULL || ptr1->next == NULL)
			return (NULL);
		ptr1 = ptr1->next;
	}
	ptr2->next = ptr1->next;
	ptr1->next = ptr2;
	return (ptr2);
}
