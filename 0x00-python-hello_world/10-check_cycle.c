#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *tmp = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (current->next != NULL & current->next->next != NULL)
	{
		tmp = tmp->next;
		current = current ->next->next;
		if (tmp = current)
			return (1);
	}
	else
		return (0);
}
