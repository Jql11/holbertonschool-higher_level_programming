#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check loop in singly linked list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *tmp = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (current->next != NULL && current->next->next != NULL)
	{
		tmp = tmp->next;
		current = current ->next->next;
		if (tmp == current)
			return (1);
	}
		
	return (0);
}
