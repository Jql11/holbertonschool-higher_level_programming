#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	current = *head;
	while (current != NULL)
	{
		if (current->n < number && current->next->n > number)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		else if (current->n > number)
		{
			new->next = current;
			*head = new;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
